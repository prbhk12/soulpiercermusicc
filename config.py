## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "AQBXUCYp8tXs63bHpi9N7mrdVh3trxHhvJhQoTnhrcayCY9T2FQrjeJTYEslXJleMmx0zFiyqZBLJ6qNbXxqoBJNki2oaVmq5Ule6X0Lny-w1SHD9G-f0eI64hjxiuGUSzN3oT0f4J4xxFsxst0xZX-7K2zyvYc7_ZT8GmM3VwHz4M2927dvcPp7onyuHLMvuxT54vsK5lVkIM_YTSu2NqSo4FZ8wVR37NfKwzVNqqfeSb9rE2HyyxxnzZK8a_WgPAJpu_GSwIvD35oOVuCQ-8KUAXlNGUhzhrEvNwiRYAbCTMrXsylLRSY-EBiL1BAeNFk6rviPSuEbm4g8-PVz01AAAAAUks8F8A":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "AQBXUCYp8tXs63bHpi9N7mrdVh3trxHhvJhQoTnhrcayCY9T2FQrjeJTYEslXJleMmx0zFiyqZBLJ6qNbXxqoBJNki2oaVmq5Ule6X0Lny-w1SHD9G-f0eI64hjxiuGUSzN3oT0f4J4xxFsxst0xZX-7K2zyvYc7_ZT8GmM3VwHz4M2927dvcPp7onyuHLMvuxT54vsK5lVkIM_YTSu2NqSo4FZ8wVR37NfKwzVNqqfeSb9rE2HyyxxnzZK8a_WgPAJpu_GSwIvD35oOVuCQ-8KUAXlNGUhzhrEvNwiRYAbCTMrXsylLRSY-EBiL1BAeNFk6rviPSuEbm4g8-PVz01AAAAAUks8F8A":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "AQBXUCYp8tXs63bHpi9N7mrdVh3trxHhvJhQoTnhrcayCY9T2FQrjeJTYEslXJleMmx0zFiyqZBLJ6qNbXxqoBJNki2oaVmq5Ule6X0Lny-w1SHD9G-f0eI64hjxiuGUSzN3oT0f4J4xxFsxst0xZX-7K2zyvYc7_ZT8GmM3VwHz4M2927dvcPp7onyuHLMvuxT54vsK5lVkIM_YTSu2NqSo4FZ8wVR37NfKwzVNqqfeSb9rE2HyyxxnzZK8a_WgPAJpu_GSwIvD35oOVuCQ-8KUAXlNGUhzhrEvNwiRYAbCTMrXsylLRSY-EBiL1BAeNFk6rviPSuEbm4g8-PVz01AAAAAUks8F8A":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "AQBXUCYp8tXs63bHpi9N7mrdVh3trxHhvJhQoTnhrcayCY9T2FQrjeJTYEslXJleMmx0zFiyqZBLJ6qNbXxqoBJNki2oaVmq5Ule6X0Lny-w1SHD9G-f0eI64hjxiuGUSzN3oT0f4J4xxFsxst0xZX-7K2zyvYc7_ZT8GmM3VwHz4M2927dvcPp7onyuHLMvuxT54vsK5lVkIM_YTSu2NqSo4FZ8wVR37NfKwzVNqqfeSb9rE2HyyxxnzZK8a_WgPAJpu_GSwIvD35oOVuCQ-8KUAXlNGUhzhrEvNwiRYAbCTMrXsylLRSY-EBiL1BAeNFk6rviPSuEbm4g8-PVz01AAAAAUks8F8A":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5784646187:AAGS50GRVmCNzqrLC2h43jl2xIM8bKF8Rg8")
BOT_NAME = getenv("BOT_NAME", "soulpiercermusic")

API_ID = int(getenv("API_ID", "2146456"))
API_HASH = getenv("API_HASH", "bc350ac036fbfd63913b7357549e2b6c")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://soul:prabhakara@cluster0.qrgenaj.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "┏━━━━━°❀•°:🎀 ❤️️🇸 🇴 🇺 🇱 🇸 🇺 🇷 🇫 🇪 🇷🏄 🎀:°•❀°━━━━━┓")
OWNER_USERNAME = getenv("OWNER_USERNAME", "SoulSurfer4u")
ALIVE_NAME = getenv("ALIVE_NAME", "┏━━━━━°❀•°:🎀 ❤️️🇸 🇴 🇺 🇱 🇸 🇺 🇷 🇫 🇪 🇷🏄 🎀:°•❀°━━━━━┓")
BOT_USERNAME = getenv("BOT_USERNAME", "@soulpiercermusic_bot")
OWNER_ID = getenv("OWNER_ID", "986458897")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Soulpiercermusic_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "soulpiercermusicsupportgroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "soulpiercermusicsupportgroup")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "986458897").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://i.postimg.cc/cHgLm6GL/rsz-photo-2022-09-30-18-16-03.jpg")
START_PIC = getenv("START_PIC", "https://i.postimg.cc/cHgLm6GL/rsz-photo-2022-09-30-18-16-03.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/prbhk12/soulpiercermusicc")
PLAY_IMG = getenv("PLAY_IMG", "https://i.postimg.cc/cHgLm6GL/rsz-photo-2022-09-30-18-16-03.jpg")
QUE_IMG = getenv("QUE_IMG", "https://i.postimg.cc/cHgLm6GL/rsz-photo-2022-09-30-18-16-03.jpg")
CMD_IMG = getenv("CMD_IMG", "https://i.postimg.cc/cHgLm6GL/rsz-photo-2022-09-30-18-16-03.jpg")
VIDEO_IMG = getenv("VIDEO_IMG", "https://i.postimg.cc/cHgLm6GL/rsz-photo-2022-09-30-18-16-03.jpg")
SKIP_IMG = getenv("SKIP_IMG", "https://i.postimg.cc/cHgLm6GL/rsz-photo-2022-09-30-18-16-03.jpg")
NEXT_IMG = getenv("NEXT_IMG", "https://i.postimg.cc/cHgLm6GL/rsz-photo-2022-09-30-18-16-03.jpg")
HEROKU_MODE = getenv("HEROKU_MODE", None)
