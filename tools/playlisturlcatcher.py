# I found this script in stackoverflow and I modified it: https://stackoverflow.com/questions/63192583/get-youtube-playlist-urls-with-python 
# Shot out to noccoa0 profile: https://stackoverflow.com/users/13679127/noccoa0

from pytube import Playlist

#Replace this with your playlist url
URL_PLAYLIST = input('Url playlist: ')

# Retrieve URLs of videos from playlist
playlist = Playlist(URL_PLAYLIST)
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
for url in playlist:
    urls.append(url)
    
print(urls)

with open('urls.log', 'w') as file:
    for url in urls:
        file.write(url + '\n')
