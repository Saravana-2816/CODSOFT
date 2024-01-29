#importing required librariea
from tkinter import *
from tkinter import messagebox

#create an instance for Tk()
window=Tk()
window.title("Todo List") 
window.geometry("990x1090")
icon=PhotoImage(file='images.png') #upload an icon image
window.iconphoto(True,icon)
window.config(bg="#eb344c")  #add a background color

 
def add():              #add task in the listBox
    tasks=entry.get()
    if(len(entry.get())==0):
        messagebox.showinfo('Empty','No Tasks Added')
    else:
        list_box.insert(list_box.size(),tasks) 
        clear()


def clear():       #clear the entries
    entry.delete(0,END) 

def delete():     #delete the task in listBox
    if (list_box.size()!=0):
        list_box.delete(list_box.curselection()) 
    else:
        messagebox.showinfo('Empty','No Tasks to Delete') 


def deleteAll(): #delete all the tasks in listBox
    list_box.delete(0,END) 

def clear1(): #exits the application
    window.destroy()    

label_photo=PhotoImage(file='picture.png',
                       height=200)
label=Label(window,text="To Do List ",   
            font=("Impact",70),
            bg="#eb344c",
            image=label_photo,
            compound='right')  #create a label for the "To do List"
label.place(x=240,y=10)
entry=Entry(window,font=("Calibri",28,"bold"),bg="white",fg="black",width=17)
entry.place(x=80,y=280)       #adds a entry box to enter the task
label2=Label(window,text="Enter the Task:",
             font=("Impact",20),
             bg="#eb344c")
label2.place(x=80,y=240)
add_button=Button(window,text="ADD",
                  font=("Calibri",24,"bold"),
                  bg="black",
                  fg="white",
                  command=add,
                  activebackground="black",
                  activeforeground="white")  #creates a add button to add the task
add_button.place(x=80,y=350)
delete_button=Button(window,text="DELETE",
                     font=("Calibri",24,"bold"),
                     bg="black",
                     fg="white",
                     command=delete,
                     activebackground="black",
                     activeforeground="white")  #creates a delete button to delete the task
delete_button.place(x=80,y=420)
deleteAll_button=Button(window,text="DELETE ALL",
                        font=("Calibri",24,"bold"),
                        bg="black",
                        fg="white",
                        command=deleteAll,
                        activebackground="black",
                        activeforeground="white")
deleteAll_button.place(x=80,y=490)   #create a delete all button to clear the listBox
clear_button=Button(window,text="EXIT",command=clear1 ,font=("Calibri",24,"bold"),bg="black",fg="white",activebackground="black",activeforeground="white")
clear_button.place(x=80,y=560)

list_box=Listbox(window,font=("Calibri",16,"bold"),width=30,bg="black",height=15,fg="white")
list_box.place(x=640,y=280)    #create a listBox to store the task

label3=Label(window,text="TASKS",font=("Impact",20),bg="#eb344c")
label3.place(x=640,y=240)
window.mainloop()