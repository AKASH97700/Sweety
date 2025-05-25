# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


import json
import os


def get_user_list(config, key):
    with open("{}/Mikobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 9429810 # Get this value from my.telegram.org/apps
    API_HASH = "06007846a1793a9883596434b299d0ed"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgresql://leothebadass_user:MUO2pxmgRnZ6FRm7KIncrJAMu7hcOvs0@dpg-d08paqp5pdvs739oghig-a.oregon-postgres.render.com/leothebadass"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002350016913
    MESSAGE_DUMP = -1002350016913

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://demonxyonko:<db_password>@rickycyan.fswqzgl.mongodb.net/?retryWrites=true&w=majority&appName=rickycyan"

    # Support chat and support ID
    SUPPORT_CHAT = "MaeveBot69"
    SUPPORT_ID = -1002350016913

    # Database name
    DB_NAME = "leothebadass"

    # Bot token
    TOKEN = "7570720829:AAF4iaaGsw5Iy448iRD40PgZKcXLfxRMols"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 7039652738
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DEMONS = get_user_list("elevated_users.json", "supports")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True
    BAN_STICKER = (
        "CAACAgUAAxkBAAEGWC5lloYv1tiI3-KPguoH5YX-RveWugACoQ4AAi4b2FQGdUhawbi91DQE"
    )

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
