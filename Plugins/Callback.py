#By @coderzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client
from script import script  # pylint:disable=import-error

elif query.data == "start_data":

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("HELP", callback_data="help_data"),
                    InlineKeyboardButton("ABOUT", callback_data="about_data"),
                ],
                [
                    InlineKeyboardButton(
                        "⭕ JOIN OUR CHANNEL ⭕", url="https://t.me/CoderzHEX"
                    )
                ],
            ]
        )

        await query.message.edit_text(
            script.START_MSG.format(query.from_user.mention),
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )
    elif query.data == "help_data":
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("BACK", callback_data="start_data"),
                    InlineKeyboardButton("ABOUT", callback_data="about_data"),
                ],
                [
                    InlineKeyboardButton(
                        "⭕ JOIN OUR CHANNEL ⭕", url="https://telegram.me/CoderzHEX"
                    )
                ],
            ]
        )
        await query.message.edit_text(
            script.HELP_MSG, reply_markup=keyboard, disable_web_page_preview=True
        )
    elif query.data == "about_data":
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("BACK", callback_data="help_data"),
                    InlineKeyboardButton("START", callback_data="start_data"),
                ],
                [
                    InlineKeyboardButton(
                        "⭕ JOIN OUR CHANNEL ⭕", url="https://telegram.me/CoderzHEX"
                    )
                ],
            ]
        )
        await query.message.edit_text(
            script.ABOUT_MSG, reply_markup=keyboard, disable_web_page_preview=True
        )
