#!/usr/bin/env python
# encoding: utf=8
"""
music_info.py

Search for information on a song or artist.

By Noran Diaconu, 2015-05-08.
"""

usage = """
Usage: 
    python music_info.py

Example (in GUI):
    pink floyd
    pink floyd - money
"""

from pyechonest import song, artist, track
from Tkinter import *
from PIL import ImageTk, Image
import AnalysisVisualization as av
import os
#import glob

global bio, blog, songType, s_hot, a_hot, duration, numResults, search_words, text, panel, root, img2
bio = False
blog = False
songType = False
s_hot = False
a_hot = False
duration = False
numResults = 5
search_words = ''
text = None
root = Tk()
img = ImageTk.PhotoImage(Image.open('nest.png'))
panel = Label(root, image = img)
img2 = Image.open('pic.png')

def main():
    global text
    root.geometry('550x410')
    panel.pack(side = 'bottom', expand = 'no')

    text2 = Message(root, width = 200, text = 'Please enter a search in the text box to the right in either of the following formats:\n\nartist name\nartist name - song title\n\nYou can also use the artist and song buttons to choose if you would like to see any of those options.\n\n\n\n\nPlease choose the number of results you would like to see.')
    text2.pack(side = LEFT)

    text = Entry()
    text.pack()
    text.delete(0, END)
    text.insert(0, 'Search_Words')
    text.config(width = 100)

    app = Music(root)
    root.mainloop()

def parse():
    global search_words, a_search_item
    search_words = text.get()
    print search_words
    if '-' in search_words:
        lis = search_words.split('-')
        a_results = artist.search(name=lis[0])
        replaced = [l.replace('+', ' ') for l in lis[1]]
        new_song = ''
        new_song = ''.join(replaced)
        new_combined = lis[0] + new_song
        results = song.search(combined=new_combined)
        print 'Song Name: ', new_song
    else:
        results = song.search(title=search_words)
        print results[1]
        a_results = artist.search(name=search_words)
        #print a_results
    x = 0
    try:
        for x in range(0, numResults):
            if x == 1:
                print '-----Other Possible Artists-----'
                print
            print 'Result ', x+1
            search_item = results[x]
            print 'Song: ', search_item
            print 'here'
            print str(search_item)

            if os.path.isfile('MP3Songs/' + str(search_item) + '.mp3'):
                picc()
            a_search_item = a_results[x]
            print 'Artist Name: ', a_search_item.name
            print 'Artist Location: ', search_item.artist_location
            print 'Danceability: ', search_item.audio_summary['danceability']
            print 'Tempo: ', search_item.audio_summary['tempo']
            print 'Loudness: ', search_item.audio_summary['loudness']
            print
            if x == 0:
                a_search_item = a_results[x]
                search_item = results[x]

                if bio == True:
                    print 'Biography:'
                    print a_search_item.biographies[0]
                    print
                if blog == True:
                    print 'Blog:'
                    print a_search_item.blogs[0]
                    print
                if a_hot == True:
                    print 'Artist Hotness:'
                    print a_search_item.hotttnesss
                    print
                if songType == True:
                    print 'Song Type:'
                    print search_item.song_type
                    print
                if duration == True:
                    print 'Duration:'
                    print search_item.audio_summary['duration']
                    print
                if s_hot == True:
                    print 'Song Hotness:'
                    print search_item.song_hotttnesss
                    print
            if (x+1) == numResults:
                print 'Search complete!'

            x += 1
            try:
                search_item = results[x]
                a_search_item = a_results[x]
            except IndexError:
                print 'Search complete!'
                break
            print

    except IndexError:
        print 'Search complete!'

def bioChoice():
    global bio, a_search_item
    bio = not bio
    print 'Biography: ', bio

def blogChoice():
    global blog
    blog = not blog
    print 'Blog: ', blog

def a_hotChoice():
    global a_hot
    a_hot = not a_hot
    print 'Artist Hotness: ', a_hot

def songTypeChoice():
    global songType
    songType = not songType
    print 'Song Type: ', songType

def s_hotChoice():
    global s_hot
    s_hot = not s_hot
    print 'Song Hotness: ', s_hot

def durationChoice():
    global duration
    duration = not duration
    print 'Duration: ', duration

def r1Choice():
    global numResults
    numResults = 1
    print 'Results: ', numResults

def r2Choice():
    global numResults
    numResults = 2
    print 'Results: ', numResults

def r3Choice():
    global numResults
    numResults = 3
    print 'Results: ', numResults

def r4Choice():
    global numResults
    numResults = 4
    print 'Results: ', numResults

def r5Choice():
    global numResults
    numResults = 5
    print 'Results: ', numResults

def picc():
    global panel, img2
    img2 = Image.open('pic.png')
    img2 = img2.resize((460, 140), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    panel.config(image = img2)

class Music(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = '#24A9E4')
        self.parent = parent
        self.initUI()

    def initUI(self):
        var = IntVar()
        self.parent.title('Music Info')
        picButton = Button(self, text = 'PIC', command = picc)
        picButton.config(height = 4, width = 10)
        picButton.place(x = 240, y = 130)
        continueButton = Button(self, text = 'Search', command = parse)
        continueButton.config(height = 4, width = 10)
        continueButton.place(x = 240, y = 50)
        artistLabel = Label(self, text = 'Artist Options', bg = 'red')
        artistLabel.place(x = 10, y = 0)
        songLabel = Label(self, text = 'Song Options', bg = 'red')
        songLabel.place(x = 120, y = 0)
        bioButton = Checkbutton(self, text = 'Biography?', command = bioChoice)
        bioButton.config(height = 3, width = 10)
        bioButton.place(x = 10, y = 30)
        blogButton = Checkbutton(self, text = 'Blogs?', command = blogChoice)
        blogButton.config(height = 3, width = 10)
        blogButton.place(x = 10, y = 90)
        a_hotButton = Checkbutton(self, text = 'Artist\nHotness?', command = a_hotChoice)
        a_hotButton.config(height = 3, width = 10)
        a_hotButton.place(x = 10, y = 150)
        songTypeButton = Checkbutton(self, text = 'Song Type?', command = songTypeChoice)
        songTypeButton.config(height = 3, width = 10)
        songTypeButton.place(x = 120, y = 30)
        durationButton = Checkbutton(self, text = 'Duration?', command = durationChoice)
        durationButton.config(height = 3, width = 10)
        durationButton.place(x = 120, y = 90)
        s_hotButton = Checkbutton(self, text = 'Song\nHotness?', command = s_hotChoice)
        s_hotButton.config(height = 3, width = 10)
        s_hotButton.place(x = 120, y = 150)
        r1 = Radiobutton(self, text = '1', variable = var, value = 1, command = r1Choice)
        r1.place(x = 10, y = 220)
        r2 = Radiobutton(self, text = '2', variable = var, value = 2, command = r2Choice)
        r2.place(x = 50, y = 220)
        r3 = Radiobutton(self, text = '3', variable = var, value = 3, command = r3Choice)
        r3.place(x = 90, y = 220)
        r4 = Radiobutton(self, text = '4', variable = var, value = 4, command = r4Choice)
        r4.place(x = 130, y = 220)
        r5 = Radiobutton(self, text = '5', variable = var, value = 5, command = r5Choice)
        r5.place(x = 170, y = 220)
        self.pack(fill = BOTH, expand = 1)

if  __name__ == '__main__':
    import sys
    try:
        #main()
        av.play_music()
    except:
        #print usage
        sys.exit(-1)
