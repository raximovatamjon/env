import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove

API_TOKEN = '6452901767:AAEaKcoEpf4M0VbohD_LMuaaDo-VDAeylXk'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


til=ReplyKeyboardMarkup(keyboard=[
     [
          KeyboardButton(text="🇺🇿uzbek"),
          KeyboardButton(text="🇷🇺rus"),
          KeyboardButton(text="🇬🇧en")
     ],
     [
          KeyboardButton(text='📞contact',request_contact=True),
          KeyboardButton(text='📍location',request_location=True)
     ]
],resize_keyboard=True)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nПривет!\nsalom!\nI'm @Raximov_Atamjon!",reply_markup=til)

@dp.message_handler(commands=['help','setting'])
async def help(message: types.Message):
    await message.reply("qanday yordam bera olaman")

@dp.message_handler(text='salom')
async def hello(message: types.Message):
     for i in range(10):      
                        await message.answer('Assalomu alleykum')


# lang
@dp.message_handler(text='🇺🇿uzbek')
async def help(message: types.Message):
    await message.answer("salom siz o'zbek tilini tanladiz!🇺🇿 ",reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text='🇷🇺rus')
async def help(message: types.Message):
    await message.answer('Здравствуйте, вы выбрали русский язык!🇷🇺',reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text='🇬🇧en')
async def help(message: types.Message):
    await message.answer('Hello, you have selected English!🇬🇧',reply_markup=ReplyKeyboardRemove())


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)