import os
from dotenv import load_dotenv

# Explicitly specify the .env file path
load_dotenv(dotenv_path=".env")
print("KEY:", os.getenv("OPENAI_API_KEY"))