
import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "vtiktok18b")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/4dfa106b54d827002535e.png")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "V3 Assistance")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "viraltiktokgroups")
PROJECT_NAME = getenv("PROJECT_NAME", "Iki Music")
OWNER = getenv("OWNER", "@graclex")
SOURCE_CODE = getenv("SOURCE_CODE", "t.me/graclex")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "8"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
PMMSG = getenv("PMMSG", f"Hi , Ini adalah music assistant service of @{BOT_USERNAME}.\n\n ❗️ Rules:\n   - Chat seperlunya \n   - SPAM langsung block/ban \n\n 👉 **Berikan LINK INVITE GROUP Kalian jika BOT ini tidak dapat bergabung dengan GROUP kalian dan Pastikan BOT ini TIDAK TER-BANNED**\n - Kemudian jadikan BOT @V18plusmusic ini **ADMIN** di group kalian \n\n ⚠️ Wajib gabung Group:\n @viraltiktokgroups\n @vtiktok18b\n @v18plusg\n\n")
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
