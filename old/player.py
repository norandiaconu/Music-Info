from Tkinter import *
import mp3play
import tkFileDialog
import Tkinter
def open_file():                                #Opens a dialog box to open .mp3 file
    global music                                #then sends filename to file_name_label.
    global mp3
    global play_list
    filename.set (tkFileDialog.askopenfilename(defaultextension = ".mp3", filetypes=[("All Types", ".*"), ("MP3", ".mp3")]))
    playlist = filename.get()
    playlist_pieces = playlist.split("/")
    play_list.set (playlist_pieces[-1])
    playl = play_list.get()
    play_list_display.insert(END, playl)
    mp3 = filename.get()
    print mp3
    music = mp3play.load(mp3)
    pieces = mp3.split("/")
    name.set (pieces[-1])

def play():                                     #Plays the .mp3 file
    music.play()

def stop():                                     #Stops the .mp3 file
    music.stop()                
def pause():                                    #Pauses or unpauses the .mp3 file
    if music.ispaused() == True:
        music.unpause()
    elif music.ispaused() == False:
        music.pause()

def vol(event):                                 #Allows volume to be changed with the slider
    v = Scale.get(volume_slider)
    music.volume(v)
def Exit():
    exit()
root = Tk()
root.title("EmoPlayer")
root.geometry('300x100+250+100')
filename = Tkinter.StringVar()
name = Tkinter.StringVar()
play_list = Tkinter.StringVar()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu = filemenu)
filemenu.add_command(label='Open', command = open_file)
filemenu.add_separator()
filemenu.add_command(label='Exit', command = Exit)
root.config(menu=menubar)
open_file = Button(root, width = 6, height = 1, text = 'Open file', command = open_file)
open_file.grid(row=0, column=3)
play_button = Button(root, width = 5, height = 1, text='Play', command = play)
play_button.grid(row=0, column=0, sticky = W)
stop_button = Button(root, width = 5, height = 1, text='Stop', command = stop)
stop_button.grid(row=0, column=1, sticky = W)
pause_button = Button(root, width = 5, height = 1, text='Pause', command = pause)
pause_button.grid(row=0, column=2)
volume_slider = Scale(root, label='Volume', orient = 'horizontal', fg = 'black', command = vol)
volume_slider.grid(row=0, column=4)
file_name_label = Label(root, font=('Verdana', 8), fg = 'black', wraplength = 300, textvariable=name )
file_name_label.grid(row=3, column=0, columnspan=8)
play_list_window = Toplevel(root, height = 150, width = 100)
play_list_window.title("Playlist")
play_list_display = Listbox(play_list_window, width = 50)   
play_list_display.pack()

play_list_window.mainloop()
root.mainloop()
