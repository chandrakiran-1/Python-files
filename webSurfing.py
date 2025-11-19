from tkinter import *
root=Tk()
root.title="my frist gui "
root.geometry="300x200"
label=Label(root,text="enter your name ")
label.pack()
entry=Entry()
entry.pack()
def show():
    print("hello",entry.get())
button=Button(root,text="click me!")
button.pack()
root.mainloop()