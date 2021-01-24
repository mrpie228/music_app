import os
from config import MUSIC_DIR

os.chdir(MUSIC_DIR)

playlists=[]
f={}
songs=''
text_file = open("text.txt", "w")
class Playlist:
    def __init__(self, name,autor, songs):
        self.name=''
        self.autor=''
        self.songs=[]
    
for root, dirs, files in os.walk(".", topdown = False):

    for name in dirs:
        playlists.append(os.path.join(root, name))
        f[name]=name
        text_file.write(name +";")
    for playlist in playlists:
        for root,dirs, files in os.walk(playlist, topdown = False):
            print(root)
            for name in files:
                print(name)
                text_file.write(name+";")
                

print(playlists,f)