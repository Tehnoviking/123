from django.conf import settings
from aiogram import Bot,Dispatcher,types
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils import  executor
from django.core.management.base import BaseCommand
import logging
import time
from ...models import Category,Producer
from asgiref.sync import sync_to_async

logging.basicConfig(level=logging.INFO)


bot = Bot(token=settings.TELEGRAMBOT_API_TOKEN)

dp = Dispatcher(bot)

button = KeyboardButton("Categories")

button_producers = KeyboardButton("Producers")


keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)
keyboard.add(button)
keyboard.add(button_producers)

@dp.message_handler(commands=["help","start"])
async def command_help(message:types.Message):
    await message.answer("Input Some Message",reply_markup=keyboard)


@sync_to_async()
def get_categories():
    return list(Category.objects.all())


@dp.message_handler(lambda message:message.text == "Categories")
async def certain_message(msg:types.Message):
    categories = await get_categories()

    msg_to_answer = ''
    for cat in categories:
        msg_to_answer += f"Category:{cat.name}\n{cat.description}\n"
    await bot.send_message(msg.from_user.id,msg_to_answer)

@dp.message_handler()
async def query_telegram(msg:types.Message):
    print(msg.text)
    await bot.send_message(msg.chat.id,'have a nice day')

class Command(BaseCommand):
    help = 'Test TG Bot'

    def handle(self,*args,**options):
        executor.start_polling(dp)



@sync_to_async()
def get_producers():
    return list(Producer.objects.all())


@dp.message_handler(lambda message:message.text == "Producers")
async def producers_callback(msg:types.Message):
    producers = await get_producers()

    msg_to_answer = ''
    for prod in producers:
        msg_to_answer += f"Producer:{prod.name}\n"

    await bot.send_message(msg.from_user.id,msg_to_answer)