import yadisk
from moviepy.editor import VideoFileClip


y = yadisk.YaDisk()

def download_video(public_url, save_path) -> bool:
    try:
        y.download_public(public_url, save_path)
        return True
    except yadisk.exceptions.YaDiskError as e:
        return False


def extract_audio(input_path, output_path) -> bool:
    try:
        with VideoFileClip(input_path) as video:
            audio = video.audio
            audio.write_audiofile(output_path)
        return True
    except Exception:
        return False