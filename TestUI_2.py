from tkinter import *
import configparser
import os
from tkinter.ttk import Combobox
from tkinter import messagebox


root = Tk()
root.title("SDM20 Program")

root.geometry('640x400')
root.resizable(width=False, height=False)

label0= Label(root, text="ID Slave", width=20, font=("arial",10,"bold"))
label0.place(x=140,y=110)

label1= Label(root, text="SDM20", relief="solid", width=20, font=("arial",19,"bold"))
label1.place(x=165,y=53)

label2= Label(root,text="Register Address",width=20,font=("arial",10,"bold"))
label2.place(x=140,y=150)
##
##label2= Label(root,text="Data type",width=20,font=("arial",10,"bold"))
##label2.place(x=140,y=190)
##
##label2= Label(root,text="Read type",width=20,font=("arial",10,"bold"))
##label2.place(x=140,y=230)

##label2= Label(root,text="Refresh time",width=20,font=("arial",10,"bold"))
##label2.place(x=140,y=270)

#register address
e = Entry(root, width=21) #Register
e.place(x=340, y=150)

e1 = Entry(root, width=21) #Slave
e1.place(x=340, y=110)

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
##e3 = Entry(root, width=21)
##e3.place(x=340, y=190)

    
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
##       else:
##            temp2 = 2
##
        item = str(e1.get())
        ID = "ID"+item
##        temp3 = e3.get()
        a1 = [ID,temp]
        print(a1)

         
        if(os.path.isfile('config.ini')==False):
            
            config[a1[0]] = {"Register": a1[1]}
            with open('config.ini','w') as configfile:
                config.write(configfile)
        else:
            config.read('config.ini')
            config[a1[0]] = {"Register": a1[1]}
            with open('config.ini','w') as configfile:
                config.write(configfile)
            
        messagebox.showinfo("Message", "Add register successful!!")

        return a1
    else:
        messagebox.showinfo("Message", "Please try again")

    
    
        

def show_data():
    import show_data
    show_data.main()
    path = 'Get_data.ini'
    path1 = 'config.ini'
    section = get_section(path)
    #print(section)
    #a = get_setting(path, section[0],"Answer")
    #messagebox.showinfo(title='Register data', message="Report Result!" '\n' 'Id slave: %s' '\n' 'The result from register %s \n = %s' %(b[0],b[1], a))
    conta = len(section)
    i=0
    while i < conta:
        a = get_setting(path, section[i],"Answer")
        messagebox.showinfo(title='Register data', message="Report Result!" '\n' 'Id slave: %s' '\n' ' = %s' %(section[i], a))
        i+=1

   

##def new_P():
##    os.remove("config.ini")
##    os.remove("Get_data.ini")
    
        
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
b1= Button(root, text="Add", width=12,bg='brown',fg='white',command=myClick)
b1.place(x=220,y=195)

b2=Button(root, text="Quit",width=12,bg='brown',fg='white',command=exit1)
b2.place(x=320,y=195)

b3= Button(root, text="Scan", width=12,bg='brown',fg='white',command=show_data)
b3.place(x=260,y=250)

##btn = Button(root,  
##             text ="Show",width=12,bg='brown',fg='white',  
##             command = NewWindow)
##btn.place(x=270,y=450)
##b3= Button(root, text="Reset", width=12,bg='brown',fg='white',command=new_P)
##b3.place(x=260,y=300)

root.mainloop()
