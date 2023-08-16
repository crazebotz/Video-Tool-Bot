#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | @AbirHasan2005 / @Rahul_Thakor

# the logging things
import logging
import math
import os
import time
import json
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS")


async def progress_for_pyrogram(current, total, bot, ud_type, message, start, status_file):
    now = time.time()
    random_text = status_file.split('/')[-2].split('-')[0]
    diff = now - start
    cancel_btn = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                'cancel', callback_data=f'cancel_up#{random_text}')  # Nice Call 🤭
        ]]
    )
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        if os.path.exists(status_file):
            with open(status_file, 'r+') as f:
                statusMsg = json.load(f)
                if not statusMsg["running"]:
                    bot.stop_transmission()
        speed = current / diff
      
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000

        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        time_to_completion = TimeFormatter(milliseconds=time_to_completion)
        # print(elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "[{0}{1}] \n<b>Progress :</b> {2}%\n".format(
            ''.join(["◾" for i in range(math.floor(percentage / 10))]),
            ''.join(["◽" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))

        tmp = progress + "<b>Completed :</b> {0} of {1}\n<b>Speed :</b> {2}/s\n<b>ETA :</b> {3}\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            time_to_completion if time_to_completion != '' else "0 s")

        try:
            if not message.photo:
                await message.edit_text(text="{}\n{}".format(ud_type, tmp), reply_markup=None)
            else:
                await message.edit_caption(caption="{}\n {}".format(ud_type, tmp))
        except:
            pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "")
    return tmp[:-2]
