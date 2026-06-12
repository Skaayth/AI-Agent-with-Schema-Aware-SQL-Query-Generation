import os
import pickle  # for memory persistence
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from backend.utils.utils import get_llm_client, load_config
from database.schema_aware_sql import process_query
from backend.utils.logging_config import logger

# Load environment variables
load_dotenv()

class AIAgent:
    def __init__(self):
        """Initialize LLM client and memory."""
        self.llm_client = get_llm_client()  
        config = load_config()
        max_memory_length = config.get("max_memory_length", 0)  

        # 🔹 **Try to Load Previous Memory (from file if available)**
        self.memory = self._load_memory(max_memory_length)

        logger.info(f"📌 Initialized memory: {'Unlimited' if max_memory_length == 0 else f'Last {max_memory_length} exchanges'}")

    def _load_memory(self, max_memory_length):
        """Load memory from file if available, else initialize new memory."""
        try:
            with open("memory.pkl", "rb") as file:
                memory = pickle.load(file)
                logger.info("📌 Loaded conversation memory from disk.")
                return memory
        except (FileNotFoundError, EOFError):
            # **Fallback to Fresh Memory**
            if max_memory_length == 0:
                #return ConversationBufferMemory(return_messages=True, memory_key="chat_history", output_key="response")
                return ConversationBufferMemory(return_messages=True, memory_key="past_questions", output_key="response")
            else:
                return ConversationBufferWindowMemory(k=max_memory_length, return_messages=True, memory_key="chat_history", output_key="response")

    def _save_memory(self):
        """Persist memory to file."""
        with open("memory.pkl", "wb") as file:
            pickle.dump(self.memory, file)

    def chat(self, user_input, user_identity):
        """Processes user input with memory, generating SQL with historical context."""
        
        # 🔹 Load previous conversation history
        past_chat = self.memory.load_memory_variables({}).get("chat_history", [])

        # 🔹 Ensure history isn't empty before adding it
        full_input = f"Previous conversation:\n{past_chat}\n\nUser: {user_input}" if past_chat else user_input

        logger.info(f"📌 User input: {user_input}")
        logger.debug(f"📌 Full input with context: {full_input}")

        # 🔹 Process query
        response = process_query(full_input, user_identity)

        # 🔹 Store in memory
        self.memory.save_context(
            {"input": user_input}, 
            {"response": ""}
        )

        self._save_memory()  # ✅ Persist memory to disk

        return response

# ✅ Instantiate AIAgent to use in API
ai_agent = AIAgent()