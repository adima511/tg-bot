
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '1263605143:AAFZS7qm0x_4NS_6C8Plu-nMnEIjm5Uc7Fw'



#token = '1263605143:AAFZS7qm0x_4NS_6C8Plu-nMnEIjm5Uc7Fw'
class BotStates(StatesGroup):
    Common = State()
    waiting_for_contact = State()
    waiting_for_sticker = State()


bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())




@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="Отправить номер телефона", request_contact=True))
    await message.answer("Отправьте пожалуйста номер телефона", reply_markup=poll_keyboard)
    await BotStates.waiting_for_contact.set()

@dp.message_handler(content_types=['contact'], state=BotStates.waiting_for_contact)
async def get_contact(message: types.Message, state: FSMContext):
    if (message.from_user.id == message.contact.user_id):
        print(str(message.contact.phone_number))
        await message.answer('Ваш контакт успешно привязан!')
        await BotStates.Common.set()
    else:
        await message.answer('Вы пытаетесь отправить не свой аккаунт!')

    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)