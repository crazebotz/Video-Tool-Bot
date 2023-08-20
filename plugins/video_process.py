from moviepy.video.io.VideoFileClip import VideoFileClip
import random
from PIL import Image


def video_data(video_path, output_path):

    try:
        video_clip = VideoFileClip(video_path)
        print(10)
        video_duration = video_clip.duration
        random_time = random.uniform(1, (round(video_duration)-1))
        print(13)
        screenshot = video_clip.get_frame(random_time)
        print(15)
        pil_image = Image.fromarray(screenshot)
        print(17)
        pil_image.save(output_path)
        width = video_clip.size[0]  # Width
        height = video_clip.size[1]  # Height
        print(21)
        return output_path, width, height, video_duration
    except Exception as e:
        print("An error occurred:", str(e))
        return None, None, None, None
