from tkinter import *
import sys, os
from distutils.dir_util import copy_tree


if os.path.exists("./bin"):
    print("Bin found")
    if os.path.exists("./bin/wwwroot/"):
        print("wwwroot found")
    if os.path.exists("./bin/index.html"):
        print("Index.html found")
    if os.path.exists("./bin/main.js"):
        print("main.js found")

if os.path.exists("./themes/"):
    print("themes found")
    allthemes = (os.listdir("./themes/"))
else:
    print("please ensure you have a themes folder")

##################################################
#           First test                           #
##################################################


def apply(Go_Thema):
    print("going")
    fromdir = "./themes/{}/".format(Go_Thema)
    todir = "./bin/"
    copy_tree(fromdir, todir)


#innit root en frame voor root
root = Tk()
frame = Frame(width=500, height=400, bg="darkgrey")

themax = 0
themaH = 10
themaW = 10
for thema in allthemes:
    print(thema)
    aLab = Label(frame, text=str(thema), bg="darkgrey")
    aLab.place(x=themaW, y=themaH)
    themax += 1
    themaH += 30
    aBut = Button(frame, text=str("apply"), command=lambda:apply(thema))
    aBut.place(x=themaW, y=themaH)
    themaH += 40

frame.pack()
#dit voorkomt dat de frame geresized kan worden verkomt lelijkheid(synoniem = ik)
root.resizable(False, False)
root.title("GO GO Themes")
# v belangrijkste van het userform
root.mainloop()
