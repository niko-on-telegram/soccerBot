import logging
import os.path

from aiogram import Router, types, F, Bot
from aiogram.enums import ChatType
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from utils import format_message

router = Router()


@router.message(CommandStart(), F.chat.type == ChatType.PRIVATE)
async def start_message_private(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("Welcome to the jungle!")


@router.channel_post(F.text)
async def channel_post_handler(message: types.Message, bot: Bot, target_channel_id: int):
    logging.info(f"Forwarding message {message.message_id}")
    backed_msg = format_message(message.text)
    await bot.send_photo(
        target_channel_id,
        FSInputFile(os.path.join('imgs', backed_msg.img_path)),
        caption=backed_msg.text,
    )
