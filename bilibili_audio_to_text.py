# pip install --upgrade google-cloud-speech
from google.cloud import speech
import yt_dlp
def download_audio():
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
    return file 

# google gcp speech to text
# configure google cli first
# in powershell enter as follow
# (New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
# & $env:Temp\GoogleCloudSDKInstaller.exe
    
def transcribe_file_with_auto_punctuation(audio_file: str) -> speech.RecognizeResponse:
    """Transcribe the given audio file with auto punctuation enabled.
    Args:
        audio_file (str): Path to the local audio file to be transcribed.
    Returns:
        speech.RecognizeResponse: The response containing the transcription results.
    """
    print("initiizing google client") 
    client = speech.SpeechClient()
    print("pass file")
    with open(audio_file, "rb") as f:
        audio_content = f.read()
    print('converting audio to text')
    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="cn-CN",
        # Enable automatic punctuation
        enable_automatic_punctuation=True,
    )

    response = client.recognize(config=config, audio=audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")

    return response

file = download_audio()
transcribe_file_with_auto_punctuation(file)