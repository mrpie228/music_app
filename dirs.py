import os
from config import MUSIC_DIR

os.chdir(MUSIC_DIR)
songs=[]
playlists=[]

for root, dirs, files in os.walk(".", topdown = False):
    
    
    for name in dirs:
        playlists.append(os.path.join(root, name))
    
    for playlist in playlists:
        for root,dirs, files in os.walk(playlist, topdown = False):
            for name in files:
                songs.append(os.path.join(root, name)) 

print(songs,playlists)