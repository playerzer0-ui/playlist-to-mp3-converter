from __future__ import unicode_literals
import yt_dlp as youtube_dl
import os
import getpass

flag = True

def cls():
    os.system('cls' if os.name=="nt" else "clear")


cls()
print("download mp3 from a youtube playlist! (or a youtube video)")
print("please make sure your playlist is set to public otherwise it won't work")
print("-------------------------------------")
print()

while flag == True:
    playlist = input("insert playlist(or youtube video link): ")

    if "https://" in playlist:
        flag = False
    else:
        print("insert a valid link")

try:
    print("creating a folder for downloads")
    user = getpass.getuser()
    path = f'C:/Users/{user}/Downloads/sOngdOwnload'
    os.mkdir(path)

except FileExistsError:
    print("folder already exists, continue with download")
    pass


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{path}/' + '%(title)s.%(ext)s',
    'addmetadata':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    },
        {
            'key': 'FFmpegMetadata'
        }
    ],
}

try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("---DOWNLOADING... DO NOT SHUT DOWN THE PROGRAM---")
        ydl.download([playlist])

except youtube_dl.utils.DownloadError:
    print("link cannot be found, did you try to make the playlist public and get the share link? or is the link itself invalid?")
    print("close the program then run it again to restart")
    input()


print("---file downloaded, it is in downloads folder, with the name 'sOngdOwnload'---")