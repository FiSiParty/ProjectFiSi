from tkinter import *
import configparser
import os
from tkinter.ttk import Combobox
from tkinter import messagebox


root = Tk()
root.title("SDM20 Program")

root.geometry('640x600')
root.resizable(width=False, height=False)

label1= Label(root, text="SDM20", relief="solid", width=20, font=("arial",19,"bold"))
label1.place(x=160,y=53)

label2= Label(root,text="Register Address",width=20,font=("arial",10,"bold"))
label2.place(x=140,y=150)
##
##label2= Label(root,text="Data type",width=20,font=("arial",10,"bold"))
##label2.place(x=140,y=190)
##
##label2= Label(root,text="Read type",width=20,font=("arial",10,"bold"))
##label2.place(x=140,y=230)

label2= Label(root,text="Refresh time",width=20,font=("arial",10,"bold"))
label2.place(x=140,y=270)

#register address
e = Entry(root, width=21)
e.place(x=340, y=150)

###data type
##e1 = Combobox(root, width=18)
##e1['values'] = ("Coil status (0xxxx)","Input status (1xxxx)","Input register (3xxxx)", "Holding register (4xxxx)")
##e1.current(0)
##e1.place(x=340, y=190)
##
###read type
##e2 = Combobox(root, width=18)
##e2['values'] = ("Float", "Uint",)
##e2.current(0)
##e2.place(x=340, y=230)

#time refresh
e3 = Entry(root, width=21)
e3.place(x=340, y=270)

def checkError():
    a=0
    string = e.get()
    
    if(string.isnumeric()==False):
            messagebox.showinfo("Message", "The register should be number!!")
            a+=1
    else:
        b = int(e.get())
        if(b>225 or b<0):
            messagebox.showinfo("Message", "Register number should be 0-225!!")
            a+=1
    return a


def NewWindow():
    newWindow = Toplevel(root)

    newWindow.title("New Window")

    newWindow.geometry("600x600")

    Label(newWindow,
          text = "Number Device").pack()
    
    e = Entry(newWindow, width=10)
    e.place(x=72, y=50)

def myClick():
    a=checkError()
    if(a<1):
        config = configparser.ConfigParser()
        temp = e.get()
##        temp1 = e1.get()
##        if(e1.get()== "Input status (1xxxx)"):
##            temp1 = 1
##        elif(e1.get()=="Holding register (4xxxx)"):
##            temp1 = 4
##        elif(e1.get()=="Coil status (0xxxx)"):
##            temp1 = 0
##        else:
##            temp1 = 3
##            
##        temp2 = e2.get()
##        if(e2.get()=="Float"):
##            temp2 = 1
##        else:
##            temp2 = 2
##        
        temp3 = e3.get()
        config['Register NO...'] = {"Register": temp,"Time": temp3}
        with open('config.ini','w') as configfile:
            config.write(configfile)
        messagebox.showinfo("Message", "Add register successful!!")
        print(temp,temp3)

        import show_data
        show_data.main()
        path = 'result.ini'
        section = get_section(path)
        #print(section)
        a = get_setting(path, section[0],"Answer")
        messagebox.showinfo(title='Register Data', message="Report Result!" '\n' 'The result from register %s \n = %s' %(temp, a))
    else:
        messagebox.showinfo("Message", "Please try again")
        
    
def exit1():
    root.destroy()

def get_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, sett):
   
    config = get_config(path)
    value = config.get(section, sett)
    msg = "{section} {sett} = {value}".format(
        section=section, sett=sett, value=value)
    return value

def get_section(path):
    config = get_config(path)
    sect = config.sections()
    return sect


##myButton = Button(root, text="Click Me", command=myClick)
b1= Button(root, text="OK", width=12,bg='brown',fg='white',command=myClick)
b1.place(x=220,y=400)

b2=Button(root, text="Quit",width=12,bg='brown',fg='white',command=exit1)
b2.place(x=320,y=400)

btn = Button(root,  
             text ="Show",width=12,bg='brown',fg='white',  
             command = NewWindow)
btn.place(x=270,y=450)


root.mainloop()
