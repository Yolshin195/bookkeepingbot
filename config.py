from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

BOOKKEEPING_API_HOST = os.environ.get("BOOKKEEPING_API_HOST")
