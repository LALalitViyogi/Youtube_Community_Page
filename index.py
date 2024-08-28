# #pytubefix
#tkinter
# OS 

#importting 

import pytubefix
import tkinter
import os
from pytube import YouTube
from pytube import Playlist

def vid_down(link):
    print("work is started")

    vid = YouTube(link).streams.filter(file_extension='mp4',progressive=True).first().download('D:\Development Workspace\Tube_downloader\Computer_Architecture')
    print("video has been downloaded")

def play_down(link):

    p = Playlist(link)
    i=0
    for url in p.video_urls:
        try:
            yt = YouTube(url)
        except:
            print(f'Video: {url} not available to download , skipping....')
        
        else:
            print(f'Video : {url} is downloading....')
            yt.streams.filter(progressive=True,file_extension='mp4').first().download("D:\Development Workspace\Tube_downloader\Computer_Architecture")
            i=i+1
    
    print(f'Total {i} videos has been Downloaded....')



if __name__=="__main__":
    video_link = input()
    play_down(video_link)