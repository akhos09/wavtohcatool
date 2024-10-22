import os
import subprocess
import yt_dlp
import re
from tkinter import filedialog as fd
from scipy.io import wavfile



# Function that checks if the URL is a valid link
def is_valid_youtube_url(url):

    youtube_regex = r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]{11}$'
    return re.match(youtube_regex, url) is not None

# Function that downloads music in .wav format with only a URL. uses ffmpeg and yt_dlp
def download_music():
    down = input('Do you want to download music in .wav from YouTube? (y/n): ')
    
    if down.lower() == 'y':
        url = input('Paste the URL: ')
        
        while url.startswith("https"):
            if not is_valid_youtube_url(url):
                print("Invalid YouTube URL. Please try again.")
                url = input('Paste a valid URL: ')
                continue

            name_file_wav = input('Name of the wav file to save (only the name and not with the .wav): ')

            # Prepare download options
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
                print(f'Music downloaded successfully as {name_file_wav}.wav')
            except Exception as e:
                print(f"Error downloading music: {e}")

            # Ask for another URL
            url = input('Paste another URL (or press Enter to stop): ')
    else:
        print('No music downloaded.')

# Function to select multiple WAV files and perform necessary calculations to loop the music.
def select_files_wav_and_calc():

    filetypes = [("wav files", "*.wav")]
    wav_files = fd.askopenfilenames(filetypes=filetypes)
    
    for wav_file in wav_files:
        route = os.path.abspath(wav_file)  # Get absolute path of the file
        
        # Get WAV file metadata
        fs, data = wavfile.read(route)
        
        # Calculate song duration in seconds
        duration_seconds = data.shape[0] / fs
        
        loop_number = fs * duration_seconds
        
        # Get the output .hca file name for each wav file
        hca_name = input(f"Output file name for {os.path.basename(route)} (type also the .hca): ")
        
        # Form the command to run VGAudiocli.exe
        command = f'VGAudiocli.exe -l 0-{int(loop_number)} -i "{route}" ./hca_converted/{hca_name}'    
        try:
            # Execute the command in the terminal
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(f"Script executed successfully for {os.path.basename(route)}:\n", result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred executing the script for {os.path.basename(route)}:\n", e.stderr)

# Call the function to select WAV files and perform the conversion
is_valid_youtube_url
download_music()
select_files_wav_and_calc()
