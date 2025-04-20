import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
D_ID_API_KEY = os.getenv("D_ID_API_KEY")

# Validate API keys
if not OPENAI_API_KEY or not D_ID_API_KEY:
    raise ValueError("API keys are missing! Check your .env file.")
