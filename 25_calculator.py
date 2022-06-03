from cgitb import grey
from logging import exception, root
from tkinter import *
from turtle import width

root = Tk()
root.geometry("600x850")
root.title("Calculator By Varaliya")
root.wm_iconbitmap("C:\\Users\\varal\\Downloads\\calculator.ico")
root.configure(background="black")
root.resizable(False, False)

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(screen.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                value = "Error"
                print(e)

        scvalue.set(value)
        screen.update()

    elif text == "AC":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvariable=scvalue, font="lucida 40 bold", borderwidth=6, relief=GROOVE, bg="orange", fg="black", insertwidth=4, bd=30)
screen.pack(fill=X, ipady=8, pady=20, padx=25)

f1 = Frame(root, bg="powder blue")

b1 = Button(f1, text="AC", font="lucida 35 bold", bg="black", fg="silver", padx=1, pady=3, borderwidth=6, relief=GROOVE)
b1.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b1.bind("<Button-1>", click)

b2 = Button(f1, text="%", font="lucida 35 bold", bg="black", fg="silver", padx=1, pady=3, borderwidth=6, relief=GROOVE)
b2.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b2.bind("<Button-1>", click)

b3 = Button(f1, text="/", font="lucida 35 bold", bg="black", fg="silver", padx=1, pady=3, borderwidth=6, relief=GROOVE)
b3.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b3.bind("<Button-1>", click)

b4 = Button(f1, text=".", font="lucida 35 bold", bg="black", fg="silver", padx=1, pady=3, borderwidth=6, relief=GROOVE)
b4.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b4.bind("<Button-1>", click)

f1.pack()

f2 = Frame(root, bg="powder blue")

b2 = Button(f2, text="7", font="lucida 35 bold", bg="black", fg="silver", padx=6, pady=3, borderwidth=6, relief=GROOVE)
b2.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b2.bind("<Button-1>", click)

b3 = Button(f2, text="8", font="lucida 35 bold", bg="black", fg="silver", padx=6, pady=3, borderwidth=6, relief=GROOVE)
b3.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b3.bind("<Button-1>", click)

b4 = Button(f2, text="9", font="lucida 35 bold", bg="black", fg="silver", padx=6, pady=3, borderwidth=6, relief=GROOVE)
b4.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b4.bind("<Button-1>", click)

b5 = Button(f2, text="*", font="lucida 35 bold", bg="black", fg="silver", padx=6, pady=3, borderwidth=6, relief=GROOVE)
b5.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b5.bind("<Button-1>", click)

f2.pack()

f3 = Frame(root, bg="powder blue")


b2 = Button(f3, text="4", font="lucida 35 bold", bg="black", fg="silver", padx=5.5, pady=3, borderwidth=6, relief=GROOVE)
b2.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b2.bind("<Button-1>", click)

b3 = Button(f3, text="5", font="lucida 35 bold", bg="black", fg="silver", padx=5.5, pady=3, borderwidth=6, relief=GROOVE)
b3.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b3.bind("<Button-1>", click)

b1 = Button(f3, text="6", font="lucida 35 bold", bg="black", fg="silver", padx=5.5, pady=3, borderwidth=6, relief=GROOVE)
b1.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b1.bind("<Button-1>", click)

b2 = Button(f3, text="-", font="lucida 35 bold", bg="black", fg="silver", padx=5.5, pady=3, borderwidth=6, relief=GROOVE)
b2.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b2.bind("<Button-1>", click)

f3.pack()

f4 = Frame(root, bg="powder blue")

b1 = Button(f4, text="1", font="lucida 35 bold", bg="black", fg="silver", padx=5, pady=3, borderwidth=6, relief=GROOVE)
b1.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b1.bind("<Button-1>", click)

b2 = Button(f4, text="2", font="lucida 35 bold", bg="black", fg="silver", padx=5, pady=3, borderwidth=6, relief=GROOVE)
b2.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b2.bind("<Button-1>", click)

b3 = Button(f4, text="3", font="lucida 35 bold", bg="black", fg="silver", padx=5, pady=3, borderwidth=6, relief=GROOVE)
b3.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b3.bind("<Button-1>", click)

b1 = Button(f4, text="+", font="lucida 35 bold", bg="black", fg="silver", padx=5, pady=3, borderwidth=6, relief=GROOVE)
b1.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b1.bind("<Button-1>", click)

f4.pack()

f5 = Frame(root, bg="powder blue")

b1 = Button(f5, text="00", font="lucida 35 bold", bg="black", fg="silver", padx=4, pady=3, borderwidth=6, relief=GROOVE)
b1.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b1.bind("<Button-1>", click)

b2 = Button(f5, text="0", font="lucida 35 bold", bg="black", fg="silver", padx=3, pady=3, borderwidth=6, relief=GROOVE)
b2.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b2.bind("<Button-1>", click)

b3 = Button(f5, text=".", font="lucida 35 bold", bg="black", fg="silver", padx=3, pady=3, borderwidth=6, relief=GROOVE)
b3.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b3.bind("<Button-1>", click)

b1 = Button(f5, text="=", font="lucida 35 bold", bg="black", fg="silver", padx=4, pady=3, borderwidth=6, relief=GROOVE)
b1.pack(side=LEFT, ipadx=8, padx=18, pady=12)
b1.bind("<Button-1>", click)

f5.pack()

root.mainloop()