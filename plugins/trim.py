import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


async def trim_video(dir_path, input_file, output_prefix, durations):
    videos = []
    video_clip = VideoFileClip(input_file)

    for i, duration in enumerate(durations):
        start_time, end_time = duration
        output_file = f"{dir_path}/{output_prefix}{i+1}.mp4"

        ffmpeg_extract_subclip(input_file, start_time,
                               end_time, targetname=output_file)
        videos.append(output_file)

    video_clip.close()
    return videos


if __name__ == "__main__":
    input_video = "video.mp4"
    output_prefix = "Anokha-Rishta-S01E0"

    # List of durations in seconds [(start_time1, end_time1), (start_time2, end_time2), ...]
    durations = [(0, 1292), (1293, 2428)]

    trim_video(input_video, output_prefix, durations)
