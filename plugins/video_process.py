import random
from moviepy.video.io.VideoFileClip import VideoFileClip
from PIL import Image


def video_data(video_path, output_path):
    video_clip = VideoFileClip(video_path)
    video_duration = video_clip.duration
    random_time = random.uniform(1, video_duration)

    screenshot = video_clip.get_frame(random_time)
    pil_image = Image.fromarray(screenshot)
    pil_image.save(output_path)
    # screenshot.save_frame(output_path)
    width = video_clip.size[0]  # Width
    height = video_clip.size[1]  # Height
    return output_path, width, height, video_duration


# async def get_vid_info(image_path):
#     try:
#         with Image.open(image_path) as img:
#             width, height = img.size
#             return width, height
#     except Exception as e:
#         return 320, 320
