from dotenv import load_dotenv
import os

# Load environment variables from .env.local
load_dotenv('.env.local')

# Fetch the API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Please ensure `.env.local` contains the key.")
