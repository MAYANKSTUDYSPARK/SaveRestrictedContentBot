#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("22657422", default=None, cast=int)
API_HASH = config("354881b0718d6f5439d8a523019ffd2e", default=None)
BOT_TOKEN = config("8284935484:AAFo0R7IzQb8icullxEwWtA9MS7X7jomwpk", default=None)
SESSION = config("BQFZuY4ALaSrRJKPtxv_eC8RD3c961-xAOBNdqCKR6Ou0dQfATf3U3V46U41dhJ16Eh1H48D66S6HeBZtA51-XqO0xjE8DmkfPqy4nwd4hgwtexneqltK65e9VpI2uH_dS-37JeOT1KebmUGMK9PkBu_c4Tz5pckQRrVRElc8hrzr46FNWIeIEfb7AzBbmc4T7EysP8MDo6No6Gvoh3oOTaR1JOJFasEzlsZ9VXH8E55LKG-6GrSa_WcAYtqMf-DOimbjo8QHR9iGOrSs_fKPUsCE76acM2xHvVdW3LjKhwV4smaEacxU7vNH0-Hlc-JS6mBkqgCjMikT_iPIkSa049oXs6OhQAAAAHp5pqMAA", default=None)
FORCESUB = config("scholarversepro_network", default=None)
AUTH = config("8219171468", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
