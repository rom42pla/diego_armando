from pymongo.server_api import ServerApi
import asyncio
import logging
import sys
from os import getenv
from datetime import date

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.fsm.storage.memory import MongoStorage

from aiogram.types import CallbackQuery
# from aiogram_dialog import DialogManager, Window
# from aiogram_dialog.widgets.kbd import Calendar
# from aiogram_dialog.widgets.kbd import Button
# from aiogram_dialog.widgets.text import Const
from aiogram.filters.state import State, StatesGroup
# from aiogram_dialog import setup_dialogs

class TelegramBot:

    def __init__(self, telegram_api_token, mongodb_api_username, mongodb_api_password):
        from pymongo.mongo_client import MongoClient

        uri = f"mongodb+srv://f{mongodb_api_username}:{mongodb_api_password}@data.skifgiq.mongodb.net/?retryWrites=true&w=majority&appName=data"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        self.dp = Dispatcher()
        self.bot = Bot(token=telegram_api_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

        @self.dp.message(Command("start"))
        async def command_start_handler(message: Message) -> None:
            pass
            # async def on_date_selected(callback: CallbackQuery, widget, manager: DialogManager, selected_date: date):
            #     await callback.answer(str(selected_date))

            # calendar = Calendar(id='calendar', on_click=on_date_selected)
            # await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=calendar)


        @self.dp.message()
        async def echo_handler(message: Message) -> None:
            try:
                # Send a copy of the received message
                await message.send_copy(chat_id=message.chat.id)
                print(message)
            except TypeError:
                # But not all the types is supported to be copied so need to handle it
                await message.answer("Nice try!")    

        async def start_polling():
            await self.dp.start_polling(self.bot)
    
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(start_polling())

        