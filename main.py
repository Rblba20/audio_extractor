import moviepy.editor
from pathlib import Path

video_name = input('Укажите путь до нужного видео'
                   '(Specify the path to the desired video):')
video_file = Path(video_name)

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio_name = input('Укажите имя аудио файла(без формата)'
                   '(Specify the name of the audio file (without format)):')
audio.write_audiofile(f'{audio_name}.mp3')

