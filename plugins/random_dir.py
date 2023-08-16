import random
import string
import os


async def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for _ in range(y))


async def create_random_dirs(chat_id):
    rendem = await random_char(5)
    download_dir = "./DOWNLOADS"
    temp_dir = f"{download_dir}/{rendem}-{str(chat_id)}"
    if not os.path.isdir(temp_dir):
        os.makedirs(temp_dir)
    status_file = f"{temp_dir}/status.json"

    return temp_dir, status_file

# "./DOWNLOADS/dsHBs-933487/status.json"



