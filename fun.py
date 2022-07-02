import tkinter as tk
import pytube
from pytube import __main__
from pytube import Playlist
from pytube import Search
from pytube import Stream

##USE THIS FOR INPUT
##p = input("Give the playlist link:")

window =tk.Tk()
window.mainloop()

##TEMPORARY
p= "https://www.youtube.com/playlist?list=PLDD2Be2ZfSPjCInDBSAID2zYE4gKBFZ1Y"
##TEMPORARY

print (p)

PL = Playlist(p)

print(f'Downloading: {PL.title}'f' --- {PL.length} videos')

print(f'{PL.title}')

#print(f'{EL.title}')

i = 1

for url in PL.video_urls:  
    print ({i})
    print (url)
    print (f'{url.title}')
    i=i+1



##for url in PL.videos:
##    print (i)+ ('yep')
##    print (f'{PL.videos}')
##
##    
##for url in PL.title:
##    print (f)
##    
##class stream:
##    for url in PL.video_urls:
##        T = (url)
##        print (f)
    
##for url in PL.video_urls:
##    print(url)
##    print(f'name: {PL.title}')
  
##print(f'{PL.videos}')

##for video in p.video_title:
##    print(title)
