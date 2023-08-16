import shutil
import re
import json
import time
from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.trim import trim_video
from plugins.random_dir import create_random_dirs
from plugins.display_progress import progress_for_pyrogram
from plugins.video_process import video_data

message_pattern = r'\(\d+,\s*\d+\)(?:,\(\d+,\s*\d+\))*'

pattern = r'\((\d+),\s*(\d+)\)'


@Client.on_message(filters.video & filters.incoming)
async def send_back_video(_, msg: Message):
    await msg.copy(msg.from_user.id, msg.caption)
    await msg.delete()


@Client.on_message(filters.incoming & filters.command('edit'))
async def edit_caption(_, msg: Message):
    text = msg.text.split('/edit ')[1]
    await msg.reply_to_message.edit_caption(text)
    await msg.delete()


@Client.on_message(filters.text & filters.regex(message_pattern))
async def trim_vid_cmd(bot: Client, msg: Message):
    if not msg.reply_to_message.caption:
        return await msg.reply_text("`/edit Name`")
    file_name = msg.reply_to_message.caption
    matches = re.findall(pattern, msg.text)

    result_list = [(int(match[0]), int(match[1])) for match in matches]
    user_id = msg.from_user.id

    dir_path, status_file = await create_random_dirs(user_id)
    sent_message = await msg.reply_text("Downloading")

    with open(status_file, 'w') as f:
        statusMsg = {'running': True, 'message': sent_message.id}
        json.dump(statusMsg, f, indent=2)
    d_start = time.time()

    input_video = await msg.reply_to_message.download(f"{dir_path}/{file_name}.mp4", progress=progress_for_pyrogram, progress_args=(bot, "Downloading...", sent_message, d_start, status_file))

    videos_path = await trim_video(dir_path, input_video, file_name, result_list)
    index = 1

    for video in videos_path:
        await sent_message.edit_text("Uploading")
        time.sleep(1)
        ss_path = f"{dir_path}/{index}.jpg"
        ss_path, width, height, video_duration = video_data(video, ss_path)
        u_start = time.time()

        await msg.reply_video(video, caption=f"{file_name}{index}", quote=True, duration=round(video_duration), width=width, height=height, thumb=ss_path, progress=progress_for_pyrogram, progress_args=(bot, "Uploading...", sent_message, u_start, status_file))
        index += 1

    shutil.rmtree(dir_path)
    await sent_message.delete()


@Client.on_message(filters.text & filters.regex(message_pattern))
async def trim_vid_cmd(bot: Client, msg: Message):
    try:
        if not msg.reply_to_message.caption:
            return await msg.reply_text("`/edit Name`")

        file_name = msg.reply_to_message.caption
        matches = re.findall(pattern, msg.text)

        result_list = [(int(match[0]), int(match[1])) for match in matches]
        user_id = msg.from_user.id

        dir_path, status_file = await create_random_dirs(user_id)
        sent_message = await msg.reply_text("Downloading")

        with open(status_file, 'w') as f:
            statusMsg = {'running': True, 'message': sent_message.id}
            json.dump(statusMsg, f, indent=2)

        d_start = time.time()

        input_video = await msg.reply_to_message.download(f"{dir_path}/{file_name}.mp4", progress=progress_for_pyrogram, progress_args=(bot, "Downloading...", sent_message, d_start, status_file))

        videos_path = await trim_video(dir_path, input_video, file_name, result_list)
        index = 1

        for video in videos_path:
            await sent_message.edit_text("Uploading")
            time.sleep(1)
            ss_path = f"{dir_path}/{index}.jpg"
            ss_path, width, height, video_duration = video_data(video, ss_path)
            u_start = time.time()

            await msg.reply_video(video, caption=f"{file_name}{index}", quote=True, duration=round(video_duration), width=width, height=height, thumb=ss_path, progress=progress_for_pyrogram, progress_args=(bot, "Uploading...", sent_message, u_start, status_file))
            index += 1

        shutil.rmtree(dir_path)
        await sent_message.delete()

    except Exception as e:
        error_message = f"An error occurred: {e}"
        await msg.reply_text(error_message)
    finally:
        try:shutil.rmtree(dir_path)
        except:pass

