import logging

from aiogram import Router, types, F, Bot
from aiogram.enums import ChatType
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import URLInputFile

from utils import format_message

router = Router()


@router.message(CommandStart(), F.chat.type == ChatType.PRIVATE)
async def start_message_private(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("Welcome to the jungle!")


@router.channel_post(~F.text.contains('Last Goal: None'))
async def channel_post_handler(message: types.Message, bot: Bot, target_channel_id: int):
    logging.info(f"Forwarding message {message.message_id}")
    backed_msg = format_message(message.text)
    await bot.send_photo(
        target_channel_id,
        URLInputFile(
            "https://img.freepik.com/free-photo/view-soccer-ball-field_23-2150995795.jpg?size=626&ext=jpg&ga=GA1.1"
            ".553209589.1715126400&semt=ais_user"
        ),
        caption=backed_msg,
    )


@router.edited_channel_post()
async def channel_post_edited_hanlder(message: types.Message, bot: Bot, target_channel_id: int):
    logging.info(f"Forwarding message {message.message_id}")
    xs = message.text.split('\n')
    target = "Powered by InPlayGuru"
    index = xs.index(target)
    parsed_text = '\n'.join(xs[index+1:]).strip()
    if not parsed_text:
        logging.debug("Parsed text empty, skipping")
        return

    if 'Hit' not in parsed_text:
        logging.debug("Hit not found, skipping")
        return

    await bot.send_photo(
        target_channel_id,
        URLInputFile(
            "https://img.freepik.com/free-photo/view-soccer-ball-field_23-2150995795.jpg?size=626&ext=jpg&ga=GA1.1"
            ".553209589.1715126400&semt=ais_user"
        ),
        caption=f"Got update from message edit:\n{parsed_text}",
    )
