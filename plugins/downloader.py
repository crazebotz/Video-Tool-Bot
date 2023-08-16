import requests
from tqdm import tqdm

def download_with_progress(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

    with open(save_path, 'wb') as file:
        for data in response.iter_content(chunk_size=1024):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()

if __name__ == "__main__":
    url = "https://dl1.myfilmyhub.download/download/353/Yaddasht-(2023)-Hindi-Season-01-Part-02-Hunters-WEB-Series--720p-[HdMaal].mp4"
    save_path = "Downloads/Yaddasht-2.mp4"
    download_with_progress(url, save_path)