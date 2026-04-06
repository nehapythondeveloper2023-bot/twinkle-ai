import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
SERPER_API_KEY    = os.getenv("SERPER_API_KEY")
APP_HOST          = os.getenv("HOST", "0.0.0.0")
APP_PORT          = int(os.getenv("PORT", 8000))