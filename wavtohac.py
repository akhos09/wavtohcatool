import os
import subprocess
import shutil
import yt_dlp
import re
from tkinter import filedialog as fd
from scipy.io import wavfile

# Function to validate YouTube URL
def is_valid_youtube_url(url):
    youtube_regex = r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]{11}$'
    return re.match(youtube_regex, url) is not None

# Function that downloads music in .wav format from YouTube using yt_dlp and ffmpeg
def download_music():
    down = input('Do you want to download music in .wav from multiple YouTube URLs? (y/n): ')
    
    if down.lower() == 'y':
        urls = []
        
        while True:
            url = input('Paste the YouTube URL (or press Enter to finish): ')
            if not url:
                break

            # Validate the URL
            if not is_valid_youtube_url(url):
                print("Invalid YouTube URL. Please try again.")
                continue

            urls.append(url)
        
        if not urls:
            print('No valid URLs entered.')
            return

        # Directory where the downloaded WAV files will be stored
        downloaded_wav_dir = 'wav_files'
        os.makedirs(downloaded_wav_dir, exist_ok=True)

        for url in urls:
            name_file_wav = input(f'Name for the wav file of URL {url} (without .wav): ')

            # Options for ydl
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
                'outtmpl': f'{name_file_wav}',
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                # Move the downloaded WAV file to the specified directory
                wav_file_path = f"{name_file_wav}.wav"
                shutil.move(wav_file_path, os.path.join(downloaded_wav_dir, wav_file_path))
                print(f'Music downloaded successfully as {wav_file_path} and moved to {downloaded_wav_dir}.')
            except Exception as e:
                print(f"Error downloading or moving music for {url}: {e}")
    else:
        print('No music downloaded.')

# Function to select multiple WAV files and perform necessary calculations to loop the music
def select_files_wav_and_calc():
    filetypes = [("wav files", "*.wav")]
    wav_files = fd.askopenfilenames(filetypes=filetypes)
    
    for wav_file in wav_files:
        route = os.path.abspath(wav_file)  # Get absolute path of the file
        
        # Get WAV file metadata
        fs, data = wavfile.read(route)
        
        # Calculate song duration in seconds
        duration_seconds = data.shape[0] / fs
        
        # Calculate loop number for the looping parameter needed in VGAudioCLI.exe
        loop_number = fs * duration_seconds
        
        # Get the output .hca file name for each wav file
        hca_name = input(f"Output file name for {os.path.basename(route)} (include the .hca extension): ")
        
        # Form the command to run VGAudiocli.exe
        command = f'VGAudiocli.exe -l 0-{int(loop_number)} -i "{route}" ./hca_converted/{hca_name}'
        
        try:
            # Execute the command in the terminal
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(f"Script executed successfully for {os.path.basename(route)}:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred executing the script for {os.path.basename(route)}:\n{e.stderr}")

download_music()
select_files_wav_and_calc()
