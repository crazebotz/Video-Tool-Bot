from moviepy.video.io.VideoFileClip import VideoFileClip
import random
from PIL import Image


def video_data(video_path, output_path):

    try:
        video_clip = VideoFileClip(video_path)
        video_duration = video_clip.duration
        random_time = random.uniform(1, (round(video_duration)-1))
        screenshot = video_clip.get_frame(random_time)
        pil_image = Image.fromarray(screenshot)
        pil_image.save(output_path)
        width = video_clip.size[0]  # Width
        height = video_clip.size[1]  # Height
        return output_path, width, height, video_duration
    except Exception as e:
        print("An error occurred:", str(e))
        return None, None, None, None
