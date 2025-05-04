# pip install openai yt-dlp

from openai import OpenAI
import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': 'downloaded_audio.%(ext)s',
    'quiet': False,
    'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'wav',  # Using WAV for better compatibility with speech_recognition
    'preferredquality': '192',
        }],
}
# option = help(yt_dlp)
# print(option)
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    file = ydl.download(['https://www.bilibili.com/video/BV1p2RiYSEvs'])



client = OpenAI()
audio_file= open("downloaded_audio.wav", "rb")

transcription = client.audio.transcriptions.create(
    model="gpt-4o-transcribe", 
    file=audio_file
)

print(transcription.text)