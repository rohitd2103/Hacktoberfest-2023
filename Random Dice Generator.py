import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry("400x400")
root.title("Roll Dice!")
root.configure(bg="#C0C0C0")


top_line = tkinter.Label(root, text = "Welcome to Dice Simulator",fg = "black", bg = "#C0C0C0" , font = "Lucida 8 bold italic")
top_line.pack()

sec_line = tkinter.Label(root, text = "Let's Roll the Dice",fg = "black", bg = "#C0C0C0" , font = "Lucida 25 bold italic")
sec_line.pack()

dice = ["die1.jpg","die2.png","die3.png","die4.png","die5.png","die6.png"]

image2 = ImageTk.PhotoImage(file = "dice.jpg")
label1 = tkinter.Label(root, image =image2 )
label1.image = image2
label1.pack(expand = True)


def rollingdice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    label1.configure(image=image1,bg="#C0C0C0")

    label1.image = image1

button = tkinter.Button(root, text = "Roll The Dice", font=("Arial 12 bold"), width = 20, height = 2, bg="#C0C0C0", fg = "white", command = rollingdice)
button.pack(expand = True)





root.mainloop()


