from tkinter import *
from tkinter import messagebox
window=Tk()

#Creating Window
window.title("TIC-TAC-TOE")
window.geometry("600x350")

#Adding lables
lb1 = Label(window, text='Welcome to the Game!!', font=('Times','25'))
lb1.grid(row=0,column=0)
lb1 = Label(window, text='Player 1: X', font=('Times','20'))
lb1.grid(row=1,column=0)
lb1 = Label(window, text='Player 2: O', font=('Times','20'))
lb1.grid(row=2,column=0)

#logic of game
turn=1

def click1():
    global turn
    if btn1["text"]==" ":
        if turn ==1:
            turn=2
            btn1["text"]='X'
        elif turn==2:
            turn=1
            btn1["text"]='O'
        check()
def click2():
    global turn
    if btn2["text"]==" ":
        if turn ==1:
            turn=2
            btn2["text"]='X'
        elif turn==2:
            turn=1
            btn2["text"]='O'
        check()
def click3():
    global turn
    if btn3["text"]==" ":
        if turn ==1:
            turn=2
            btn3["text"]='X'
        elif turn==2:
            turn=1
            btn3["text"]='O'
        check()
def click4():
    global turn
    if btn4["text"]==" ":
        if turn ==1:
            turn=2
            btn4["text"]='X'
        elif turn==2:
            turn=1
            btn4["text"]='O'
        check()
def click5():
    global turn
    if btn5["text"]==" ":
        if turn ==1:
            turn=2
            btn5["text"]='X'
        elif turn==2:
            turn=1
            btn5["text"]='O'
        check()
def click6():
    global turn
    if btn6["text"]==" ":
        if turn ==1:
            turn=2
            btn6["text"]='X'
        elif turn==2:
            turn=1
            btn6["text"]='O'
        check()
def click7():
    global turn
    if btn7["text"]==" ":
        if turn ==1:
            turn=2
            btn7["text"]='X'
        elif turn==2:
            turn=1
            btn7["text"]='O'
        check()
def click8():
    global turn
    if btn8["text"]==" ":
        if turn ==1:
            turn=2
            btn8["text"]='X'
        elif turn==2:
            turn=1
            btn8["text"]='O'
        check()
def click9():
    global turn
    if btn9["text"]==" ":
        if turn ==1:
            turn=2
            btn9["text"]='X'
        elif turn==2:
            turn=1
            btn9["text"]='O'
        check()

flag=1
#check() to see which player has won the match
def check():
    global flag
    #extracting text from buttons
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    flag=flag+1
    #comparing values
    if b1==b2 and b1==b3 and b1=='O' or b1==b2 and b1==b3 and b1=='X':
        win(btn1["text"])
    if b4==b5 and b4==b6 and b4=='O' or b4==b5 and b4==b6 and b4=='X':
        win(btn4["text"])
    if b7==b8 and b7==b9 and b7=='O' or b7==b8 and b7==b9 and b7=='X':
        win(btn7["text"])
    if b1==b4 and b1==b7 and b1=='O' or b1==b4 and b1==b7 and b1=='X':
        win(btn1["text"])
    if b2==b5 and b2==b8 and b2=='O' or b2==b5 and b2==b8 and b2=='X':
        win(btn2["text"])
    if b3==b6 and b3==b9 and b3=='O' or b3==b6 and b3==b9 and b3=='X':
        win(btn3["text"])
    if b1==b5 and b1==b9 and b1=='O' or b1==b5 and b1==b9 and b1=='X':
        win(btn1["text"])
    if b7==b5 and b7==b3 and b1=='O' or b7==b5 and b7==b3 and b7=='X':
        win(btn7["text"])
    if flag==10:
        messagebox.showinfo("Tie", "Match Tied!! \n Try Again :)")
        window.destroy() #termintes program
    
def win(player):
    ans= "Game Complete - "+player+" wins!";
    messagebox.showinfo("Congratulations",ans)
    window.destroy() #terminates program


#Adding buttons(3X3 grid)
btn1 = Button(window, text= " ", bg="blue", fg="white", width=5, height=2, font=('Times','20'), command=click1) 
btn1.grid(row=1,column=1)
btn2 = Button(window, text= " ", bg="blue", fg="white", width=5, height=2, font=('Times','20'), command=click2)
btn2.grid(row=1,column=2)
btn3 = Button(window, text= " ", bg="blue", fg="white", width=5, height=2, font=('Times','20'), command=click3)
btn3.grid(row=1,column=3)
btn4 = Button(window, text= " ", bg="blue", fg="white", width=5, height=2, font=('Times','20'), command=click4) 
btn4.grid(row=2,column=1)
btn5 = Button(window, text= " ", bg="blue", fg="white", width=5, height=2, font=('Times','20'), command=click5)
btn5.grid(row=2,column=2)
btn6 = Button(window, text= " ", bg="blue", fg="white", width=5, height=2, font=('Times','20'), command=click6)
btn6.grid(row=2,column=3)
btn7 = Button(window, text= " ", bg="blue", fg="white", width=5, height=2, font=('Times','20'), command=click7) 
btn7.grid(row=3,column=1)
btn8 = Button(window, text= " ", bg="blue", fg="white", width=5, height=2, font=('Times','20'), command=click8)
btn8.grid(row=3,column=2)
btn9 = Button(window, text= " ", bg="blue", fg="white", width=5, height=2, font=('Times','20'), command=click9)
btn9.grid(row=3,column=3)

window.mainloop()
