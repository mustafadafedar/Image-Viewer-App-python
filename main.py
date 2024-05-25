from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os

def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file",filetypes=(("JPG  File","* .jpg"),("PNG file","* .png"),("All file ","how are you    .txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img)
    lb1.image=img


root = Tk()

fram = Frame(root)
fram.pack(side= BOTTOM,padx=15,pady=15)

lb1 =Label(root)
lb1.pack()

btn = Button(fram,text="select image",command=showimage)
btn.pack(side=tk.LEFT)

btn2 = Button(fram,text="Exit",command=lambda:exit())
btn2.pack(side=tk.LEFT,padx=12)

root.title("Image viewer")
root.geometry("400x450")

mainloop()