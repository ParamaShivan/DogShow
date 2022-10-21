import re
from os import environ

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
SESSION = "Media_search"
USER_SESSION = "User_Bot"
API_ID = 4534665
API_HASH = "366f7a24d64c5d6578df57e3b5b03fa0"
BOT_TOKEN = "5353888647:AAGdFBWN6rtdVuT-YhdO3xOiT0Z7gRagk8c"
USERBOT_STRING_SESSION = ""

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [1893684647]
CHANNELS = [-1001682880445]
AUTH_USERS = []
AUTH_CHANNEL = -1001617639833

# MongoDB information
DATABASE_URI = "mongodb+srv://apollo:pmshere@cluster0.0gkxnrn.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = "telegram_files"  # If you are using the same database, then use different collection name for each bot

CUSTOM_FILE_CAPTION = """<pre>{file_name}</pre>

<b>🔗 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗟𝗜𝗡𝗞 ☞
https://t.me/+9Y8n-l5IMF0zYTRl
https://t.me/+9Y8n-l5IMF0zYTRl
https://t.me/+9Y8n-l5IMF0zYTRl</b>"""
DL_TIME = 600
FILE_STORE_CHANNEL = -1001658035444
IMDB = False
LOG_CHANNEL = -1001390229228
PICS = "https://telegra.ph/file/ce2d3aae7bb7ec9dcf9f7.jpg"
P_TTI_SHOW_OFF = True
SINGLE_BUTTON = True
UPSTREAM_REPO = "https://github.com/sonofxander/dogshow"
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += (
    "IMDB Results are enabled, Bot will be showing imdb details for you queries.\n"
    if IMDB
    else "IMBD Results are disabled.\n"
)
LOG_STR += (
    "P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n"
    if P_TTI_SHOW_OFF
    else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n"
)
LOG_STR += (
    "SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n"
    if SINGLE_BUTTON
    else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n"
)
LOG_STR += (
    f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n"
    if CUSTOM_FILE_CAPTION
    else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n"
)
LOG_STR += (
    "Long IMDB storyline enabled."
    if LONG_IMDB_DESCRIPTION
    else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n"
)
LOG_STR += (
    "Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n"
    if SPELL_CHECK_REPLY
    else "SPELL_CHECK_REPLY Mode disabled\n"
)
LOG_STR += (
    f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n"
    if MAX_LIST_ELM
    else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n"
)
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
