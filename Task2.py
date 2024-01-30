from tkinter import *
window=Tk()
window.title('CALCULATOR')
window.geometry("360x520")
window.config(bg="#031cfc")
icon=PhotoImage(file="calci.png")
window.iconphoto(True,icon)
def button_press(num):
     global text_label
     text_label+=str(num)
     text_.set(text_label)
def equals():
     global text_label
     try:
          total=str(eval(text_label))
          text_.set(total)  
          text_label=total
     except SyntaxError:
          text_.set("Syntax Error")
          text_label=""
     except ZeroDivisionError:
          text_.set("Zero Division Error")
          text_label=""    
def clear():
     global text_label
     text_.set("")    
     text_label=""
               
text_label=""
text_=StringVar()
label=Label(window,textvariable=text_,font=("Arial",10,"bold"),bg="white",width=36,height=3)
label.place(x=40,y=70)
label=Label(window,text="Calculator",font=("Impact",30,"bold"),bg="#031cfc",fg="black")
label.place(x=10,y=0)
frame=Frame(window,bg="#031cfc")
frame.place(x=40,y=150)
button1=Button(frame,text="1",bg="black",font=("Impact",25),fg="white",height=1,width=4,
               command=lambda:button_press(1))
button1.grid(row=0,column=0)
button2=Button(frame,text="2",bg="black",font=("Impact",25),fg="white",height=1,width=4,
               command=lambda:button_press(2))
button2.grid(row=0,column=1)
button3=Button(frame,text="3",bg="black",font=("Impact",25),fg="white",height=1,width=4,
               command=lambda:button_press(3))
button3.grid(row=0,column=2)
button4=Button(frame,text="4",bg="black",font=("Impact",25),fg="white",height=1,width=4,
               command=lambda:button_press(4))
button4.grid(row=1,column=0)
button5=Button(frame,text="5",bg="black",font=("Impact",25),fg="white",height=1,width=4,
               command=lambda:button_press(5))
button5.grid(row=1,column=1)
button6=Button(frame,text="6",bg="black",font=("Impact",25),fg="white",height=1,width=4,
               command=lambda:button_press(6))
button6.grid(row=1,column=2)
button7=Button(frame,text="7",bg="black",font=("Impact",25),fg="white",height=1,width=4,
               command=lambda:button_press(7))
button7.grid(row=2,column=0)
button8=Button(frame,text="8",bg="black",font=("Impact",25),fg="white",height=1,width=4,
               command=lambda:button_press(8))
button8.grid(row=2,column=1)
button9=Button(frame,text="9",bg="black",font=("Impact",25),fg="white",height=1,width=4,
               command=lambda:button_press(9))
button9.grid(row=2,column=2)
button0=Button(frame,text="0",bg="black",font=("Impact",25),fg="white",height=1,width=4,
               command=lambda:button_press(0))
button0.grid(row=3,column=0)
add_button=Button(frame,text="+",bg="black",font=("Impact",25),fg="white",height=1,width=4,
                  command=lambda:button_press("+"))
add_button.grid(row=0,column=3)
minus_button=Button(frame,text="-",bg="black",font=("Impact",25),fg="white",height=1,width=4,
                    command=lambda:button_press('-'))
minus_button.grid(row=1,column=3)
multiply_button=Button(frame,text="*",bg="black",font=("Impact",25),fg="white",height=1,width=4,
                       command=lambda:button_press('*'))
multiply_button.grid(row=2,column=3)
division_button=Button(frame,text="/",bg="black",font=("Impact",25),fg="white",height=1,width=4,
                       command=lambda:button_press('/'))
division_button.grid(row=3,column=3)
decimal_button=Button(frame,text=".",bg="black",font=("Impact",25),fg="white",height=1,width=4,
                      command=lambda:button_press("."))
decimal_button.grid(row=3,column=1)
equalto_button=Button(frame,text="=",bg="black",font=("Impact",25),fg="white",height=1,width=4,
                      command=lambda:equals())
equalto_button.grid(row=3,column=2)
clear_button=Button(window,text="CLEAR",bg="black",font=("Impact",16),fg="white",height=1,width=8,
                      command=lambda:clear())
clear_button.place(x=150,y=450)

                     
window.mainloop()