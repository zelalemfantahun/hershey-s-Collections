__author__ = 'zelalem'
from Tkinter import *
import Tkinter
# from Tkinter import ttk
from Tkinter import filedialog


import re
window = Tk()
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/yon/Documents/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    try:
        with open(name,'r') as UseFile:
            #print(UseFile.read())
            txt = UseFile.read()
            txt = re.sub(r'\n\s*\n', '\n', txt)
            f2 = open(name, 'w')
            f2.write(txt)
            f2.close()
    except:
        print("No file exists")


btOK = Button(window, text = "Choose a file", fg = "red", width=30,height=30,command = OpenFile)
btOK.pack()
window.mainloop() #