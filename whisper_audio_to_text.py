# pip install yt-dlp openai-whisper
import whisper
import yt_dlp
import os # Import the os module to handle file paths

ydl_opts = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': 'downloaded_audio.%(ext)s',
    'quiet': True, # Keep downloads quiet for cleaner output
    'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'wav',
    'preferredquality': '192',
        }],
}

audio_filename = 'downloaded_audio.wav' # Define the expected filename

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    file = ydl.download(['https://www.bilibili.com/video/BV15ZVjzREyE'])
    

prompt = "ignore BGM"
model = whisper.load_model("turbo") # tiny, base, small, medium，turbo， Eng only: base.en
result = model.transcribe("downloaded_audio.wav",language="zh",initial_prompt=prompt)
print("Transcription with Timelines:")
for segment in result['segments']:
    start_time = segment['start']
    text = segment['text'].strip()
    print(f"{start_time:.2f} {text}")
print(result["text"])

# clear file

if os.path.exists(audio_filename):
    os.remove(audio_filename)
    print(f"Removed downloaded file: {audio_filename}")