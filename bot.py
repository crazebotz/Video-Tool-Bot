import os
import shutil
from pyrogram import Client


# Running bot
OWNER_ID = 5294965763
API_HASH = "ca5085c3f41b16df46dbeebed6e56081"
APP_ID = 28160559
BOT_TOKEN = "6092647706:AAFsAE0KgBwJl7h8mBDPVtqILHjEr0CwnPs"


DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS")


if __name__ == "__main__":

    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    else:
        try:
            shutil.rmtree(DOWNLOAD_LOCATION)
            os.makedirs(DOWNLOAD_LOCATION)
        except:
            pass

    plugins = dict(root="plugins")
    app = Client("vid-tool-bot",
                 bot_token=BOT_TOKEN,
                 api_id=APP_ID,
                 api_hash=API_HASH,
                 plugins=plugins,
                 workers=50,
                 max_concurrent_transmissions=5)
    
    # os.system("clear")
    print("Bot Started :)")
    app.run()
