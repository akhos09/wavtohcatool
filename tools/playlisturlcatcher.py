#-The tool playlisturlcacther is based on this script from stackoverflow 
#-[Forum Page](https://stackoverflow.com/questions/63192583/get-youtube-playlist-urls-with-python )
#-Shot out to noccoa0 profile: [Profile](https://stackoverflow.com/users/13679127/noccoa0)

from pytube import Playlist

URL_PLAYLIST = input('URL playlist from YouTube: ')

playlist = Playlist(URL_PLAYLIST)

output_lines = []

for idx, video in enumerate(playlist.videos):
    video_url = video.watch_url
    wav_name = f"wav_name{idx + 1}"
    hca_name = f"hca_name{idx + 1}"
    
    output_line = f"{video_url},{wav_name},{hca_name}.hca"
    output_lines.append(output_line)

with open('playlist_urls.txt', 'w') as f:
    f.write("\n".join(output_lines))

print(f"Extracted {len(output_lines)} video URLs into playlist_urls.txt")
