from tkinter import *

window = Tk()
window.geometry("500x500")
window.resizable(False, False)

# def print_n():
#     txt = input1.get()
#     print(txt)

def print2():
    txt = input1.get()
    lbl1.configure(text=txt, bg = '#45fc03')

lbl1 = Label(window, text="Hello", bg="red", width=10, height=5)
lbl1.pack()
# lbl1.grid(row=1, column=6)
lbl2 = Label(window, text="dfghjk", bg="yellow", width=10, height=5 )
# lbl2.grid(row=20, column = 3)
lbl2.pack()

input1 = Entry(window, bg = "blue")
input1.pack()

btn1 = Button(window, text="click", bg = 'green', command=print2)
btn1.pack()
window.mainloop()
