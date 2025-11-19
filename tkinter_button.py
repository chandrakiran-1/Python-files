from tkinter import *

def clicked():
    label.config(text="Button Clicked!")

root = Tk()
root.title("Button Example")

label = Label(root, text="Click the button!")
label.pack(pady=10)

button = Button(root, text="Click Me", command=clicked)
button.pack()

root.mainloop()
