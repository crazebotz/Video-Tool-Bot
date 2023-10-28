import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


async def trim_video(dir_path, input_file, output_prefix:str, durations, start=1):
    videos = []
    video_clip = VideoFileClip(input_file)
    

    for _, duration in enumerate(durations):
        start_time, end_time = duration
        ep_no = f"E0{start}"
        file_name = output_prefix.replace("E0",ep_no)
        output_file = f"{dir_path}/{file_name}.mp4"
       
        print(output_file)
        start+=1
        # continue

        ffmpeg_extract_subclip(input_file, start_time,
                               end_time, targetname=output_file)
        videos.append(output_file)

    video_clip.close()
    return videos


if __name__ == "__main__":
    pass
    # input_video = "video.mp4"
    # output_prefix = "Anokha-Rishta-S01E0"

    # # List of durations in seconds [(start_time1, end_time1), (start_time2, end_time2), ...]
    # durations = [(0, 1292), (1293, 2428)]

    # trim_video(input_video, output_prefix, durations)
