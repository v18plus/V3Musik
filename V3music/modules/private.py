# V3music (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from V3music.config import (
    BOT_USERNAME,
    PROJECT_NAME,
    SOURCE_CODE,
    SUPPORT_GROUP,
    OWNER,
    ASSISTANT_NAME,
    UPDATES_CHANNEL,
)
from V3music.modules.msg import Messages as tr

logging.basicConfig(level=logging.INFO)


@Client.on_message(filters.private & filters.incoming & filters.command(["start"]))
def _start(client, message):
    client.send_message(
        message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [[
               InlineKeyboardButton("➕ Add me to your Group 🙋‍♀️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
               InlineKeyboardButton("📲 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"),
               InlineKeyboardButton("💬 Support", url=f"https://t.me/{SUPPORT_GROUP}")
            ],
            [
               InlineKeyboardButton("🛠 Source Code 🛠", url=f"https://{SOURCE_CODE}")
           ]]
        ),
        reply_to_message_id=message.message_id,
    )


@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""<b>┗┓ Haii {message.from_user.first_name} saya adalah {PROJECT_NAME} ┏┛\n
Saya Bot Music Group, Yang dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah
Saya Memiliki Banyak Fitur Praktis Seperti :
┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Lagu.
┣• Mencari Lagu Yang ingin di Putar atau di Download.
┣• Gunakan Perintah » /help « untuk Mengetahui Fitur Lengkap saya
┗━━━━━━━━━━━━━━
❃ Managed With ❤ By {OWNER}
❃ Thanks To [Grace](https://t.me/graclex)
━━━━━━━━━━━━━━━
Join Groups
❃ Groups Mutualan [VTG](https://t.me/viraltiktokgroups)
❃ Groups 18+ 🔞  [V18Plus](https://t.me/v18plusg)
❃ Channel 18+ 🔞  [V18Plus](https://t.me/vtiktok18b)
━━━━━━━━━━━━━━━
Ingin Menambahkan Saya ke Grup Anda? Tambahkan Saya Ke Group Anda!

nb: **Agar BOT Music Dapat berjalan, Pastikan @v18plusm_bot dan @v18plusmusic Telah menjadi admin di group anda.**
Lebih lengkap ketik /help 
</b>""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan saya ke Grup Anda 🙋‍♀️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "🔞 Channel 18+ 🔞", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        "💬 Group Support", url=f"https://t.me/{SUPPORT_GROUP}")
                ],[
                    InlineKeyboardButton(
                        "🥰 OWNER ", url=f"https://{SOURCE_CODE}")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )


@Client.on_message(filters.private & filters.incoming & filters.command(["help"]))
def _help(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text=tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup=InlineKeyboardMarkup(map(1)),
        reply_to_message_id=message.message_id,
    )


help_callback_filter = filters.create(
    lambda _, __, query: query.data.startswith("help+")
)


@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split("+")[1])
    client.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=tr.HELP_MSG[msg],
        reply_markup=InlineKeyboardMarkup(map(msg)),
    )


def map(pos):
    if pos == 1:
        button = [[InlineKeyboardButton(text="▶️", callback_data="help+2")]]
    elif pos == len(tr.HELP_MSG) - 1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [[
                    InlineKeyboardButton("➕ Tambahkan saya ke Grup Anda 🙋‍♀️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],
                  [
                    InlineKeyboardButton(text="📲 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"),
                    InlineKeyboardButton(text="💬 Support", url=f"https://t.me/{SUPPORT_GROUP}")
                  ],
                  [
                    InlineKeyboardButton(text="🛠 Source Code 🛠", url=f"https://{SOURCE_CODE}")
                  ],
                  [
                    InlineKeyboardButton(text="◀️", callback_data=f"help+{pos-1}")
                 ]]
    else:
        button = [
            [
                InlineKeyboardButton(text="◀️", callback_data=f"help+{pos-1}"),
                InlineKeyboardButton(text="▶️", callback_data=f"help+{pos+1}"),
            ],
        ]
    return button


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍♀️ Hello there! I can play music in the voice chats of telegram groups & channels.**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🟡 Click here for help 🟡", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )
