from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

BOOKKEEPING_API_HOST = os.environ.get("BOOKKEEPING_API_HOST")

REDIS_HOST = os.environ.get("REDIS_HOST")

TELEGRAM_BOT_USERNAME = os.environ.get("TELEGRAM_BOT_USERNAME")
TELEGRAM_BOT_PASSWORD = os.environ.get("TELEGRAM_BOT_PASSWORD")
