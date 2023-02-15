from tkinter import *
import random
root = Tk()
root.geometry('700x500+380+160')
root.resizable(False,False)
root.configure(bg="black")
root.title('Roll Dice Simulator')
label2 = Label(root,text="",font=("times",260))
def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1 = Label(root,text="Dice-1",bg="black",fg="cyan",font="Cambria 15 bold")
    l1.place(x=180,y=380)
    l2 = Label(root,text="Dice-2",bg="black",fg="cyan",font="Cambria 15 bold")
    l2.place(x=450,y=380)
    label2.configure(text=f'{random.choice(dice)} {random.choice(dice)}',bg="black",bd=2,fg="lime")
    label2.pack()

btn1 = Button(root,text="Let's Roll",bg="black",fg="white",bd=4,width=30,height=3,font="Cambria 10 bold",command=roll,activebackground="black",activeforeground="white")
btn1.pack(padx=10,pady=10) 
root.mainloop()