import tkinter as tk
from pytube import YouTube


def downloadVid():
    global E1
    string = E1.get()
    yt = YouTube(str(string))
    videos = yt.get_videos()
    s = 1
    for video in videos:
        print(str(s) + '.' + str(v))
        s += 1
    n = int(input("Enter your choice"))
    video = videos[n - 1]
    destination = str(input("Enter your destination"))
    video.download(destination)
    print(yt.filename+"\n has been downloaded")


root = tk.Tk()

w = tk.Label(root, text="Youtube Downloader")
w.pack()

"""
The Tkinter Pack Geometry Manager. The Pack geometry manager packs widgets in rows or columns. You can use options like fill, expand, and side to control this geometry manager. The manager handles all widgets that are packed inside the same master widget. ... It then repeats the process for all widgets."""

E1 = tk.Entry(root, bd=8)
E1.pack(side=tk.TOP)

button = tk.Button(root, text="Download", fg="red", command=downloadVid)
button.pack(side=tk.BOTTOM)

root.mainloop()
