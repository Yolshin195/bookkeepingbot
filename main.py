import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message

from config import TELEGRAM_BOT_TOKEN
from service.bookkeeping_api import reference

router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


@router.message(Command(commands=["help"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/help` command
    """
    await message.answer(f"list command:"
                         f"\n\t/help - show this message"
                         f"\n\t/expense - start register new transaction expense"
                         f"\n\t/account - show your account list"
                         f"\n\t/category - show your category list")


@router.message(Command(commands=["expense"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/expense` command
    """
    await message.answer(f"Введите расход в формате: "
                         f"\n\tAccount(A)=RUB,"
                         f"\n\tExpense(E)=0.00,"
                         f"\n\tCategory(C)=Food,"
                         f"\n\tComment(M)=Купил курочку")


@router.message(Command(commands=["account"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/account` command
    """
    await message.answer(f"this will your list account")


@router.message(Command(commands=["category"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/category` command
    """
    list_category = await reference.get_all()
    await message.answer(list_category)


@router.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward received message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker and etc.)
    """
    try:
        # Send copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode="HTML")
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
