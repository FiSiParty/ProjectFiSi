from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

root = Tk()
root.title("Test Program")

root.geometry("500x500")
root.resizable(width=False, height=False)

def add():
    print("added")
    listbox1.insert(END, 5)

def reset():
    c = listbox1.size()
    print("c: ",c)
    i = 0
    listbox1.delete(ANCHOR)
##    while(c>=0):
##        listbox1.delete(c)
##        print("deleted")
##        c-=1


listbox1 = Listbox(root, width=50, heigh=20)
listbox1.pack()

b = Button(root, text="Add", width=12,bg='brown',fg='white',command=add)
b.pack()


b = Button(root, text="Reset", width=12,bg='brown',fg='white',command=reset)
b.pack()

root.mainloop()
