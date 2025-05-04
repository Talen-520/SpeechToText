# 安装: pip install yt-dlp SpeechRecognition
import yt_dlp
import speech_recognition as sr
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
    file = ydl.download(['https://www.bilibili.com/video/BV15ZVjzREyE'])


# Initialize recognizer
recognizer = sr.Recognizer()

# Load audio file
audio_file = sr.AudioFile('downloaded_audio.wav')  # or .aiff, .flac, etc.

with audio_file as source:
    audio_data = recognizer.record(source)  # read the entire file
    
    # Recognize using Google Web Speech API (free but requires internet)
    # recognize speech using Sphinx, en only
    try:
        print("Sphinx thinks you said " + recognizer.recognize_sphinx(audio_data))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))