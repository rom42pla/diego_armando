from dotenv import load_dotenv
import os

from classes.bot import TelegramBot

load_dotenv("secrets.env")
bot = TelegramBot(telegram_api_token=os.environ['TELEGRAM_API_TOKEN'], mongodb_api_username=os.environ["MONGODB_API_USERNAME"], mongodb_api_password=os.environ["MONGODB_API_PASSWORD"])
