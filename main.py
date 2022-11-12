# import tkinter as tk
from tkinter import *

root = Tk()  # main box window.
root.title("Standard Calculator")  # Title shown at the title bar
root.config(bg="sky blue")
root.resizable(True, True)

result_e = Entry(root,          # window shown as the result screen.
             width= 50,     # Creating an entry field (variable) as 'e' object (result screen)
             bg='#f0ffff',  # The Entry widget is used to accept single-line text strings from a user.
             fg='black',
             borderwidth=5,
             justify='right',
             font='Calibri 15')
result_e.grid(row=0, column=0, columnspan=4, padx=12, pady=12)
    # put e (result) on 0th grid row&column ; cover 9 grid columns; start position:12,12


def click (num):         #  Show the number/. on the result screen that has clicked
    temp = result_e.get()      # store current(last) input accessed by result_e.get().  (type: str)
    result_e.delete(0, END)     # clear 'e' Entry field (output screen) from index0 to end
    result_e.insert(0, temp + num)   # inserting at index 0 (rightmost)

def clear():              # clear result screen
    result_e.delete(0, END)

def get(operator):      # get num1 & pass operator
    global num1, math
    num1 = result_e.get()      # num1: string on result (e)
    math = operator
    result_e.insert(END, math)
    try:
        num1 = float(num1)      # type casting to float
    except ValueError:          # character other than numerals
        clear()

def equal():
    input_ = result_e.get()        # input_: current string in entry field e
    num2 = float(input_[input_.index(math) + 1:len(input_)] )    # second number: input just after math-operator stored in input_ string
    result_e.delete(0, END)                     #   clear e

    if math == "+":
        result_e.insert(0, str(num1 + num2))       # convert addition and insert the "string" to result_e (result screen)
    elif math == "-":
        result_e.insert(0, str(num1 - num2))
    elif math == "*":
        result_e.insert(0, str(num1 * num2))
    elif math == "/":
        try:
            result_e.insert(0, str(num1 / num2))
        except ZeroDivisionError:
            result_e.insert(0, "Undefined")



#  defining buttons on screen
b1 = Button(root,        # main window
               text= "1",
               padx= 40,        # button length
               pady= 10,        # button width
               command= lambda : click("1"),        # call to Click() if clicked.
               font= "Calibri 12" )

b2 = Button(root,        # main window
               text= "2",
               padx= 40,
               pady= 10,
               command= lambda : click("2"),        # call to Click()
               font= "Calibri 12" )

b3 = Button(root,        # main window
               text= "3",
               padx= 40,
               pady= 10,
               command= lambda : click("3"),        # call to Click()
               font= "Calibri 12" )
b4 = Button(root,        # main window
               text= "4",
               padx= 40,
               pady= 10,
               command= lambda : click("4"),        # call to Click()
               font= "Calibri 12" )

b5 = Button(root,        # main window
               text= "5",
               padx= 40,
               pady= 10,
               command= lambda : click("5"),        # call to Click()
               font= "Calibri 12" )
b6 = Button(root,        # main window
               text= "6",
               padx= 40,
               pady= 10,
               command= lambda : click("6"),        # call to Click()
               font= "Calibri 12" )
b7 = Button(root,        # main window
               text= "7",
               padx= 40,
               pady= 10,
               command= lambda : click("7"),        # call to Click()
               font= "Calibri 12" )
b8 = Button(root,        # main window
               text= "8",
               padx= 40,
               pady= 10,
               command= lambda : click("8"),        # call to Click()
               font= "Calibri 12" )
b9 = Button(root,        # main window
               text= "9",
               padx= 40,
               pady= 10,
               command= lambda : click("9"),        # call to Click()
               font= "Calibri 12" )
b0 = Button(root,        # main window
               text= "0",
               padx= 40,
               pady= 10,
               command= lambda : click("0"),        # call to Click()
               font= "calibri 12" )
bDot = Button(root,        # main window
               text= ".",
               padx= 40,
               pady= 10,
               command= lambda : click("."),        # call to Click()
               font= "calibri 12" )

bAdd  = Button(root,
                  text="+",
                  padx=40,
                  pady=10,
                  command= lambda : get("+"),
                  font="calibri 12")
bSub = Button(root,
                 text="-",
                 padx=40,
                 pady=10,
                 command= lambda : get("-"),
                 font='calibri 12')
bMult = Button(root,
                 text="x",
                 padx=40,
                 pady=10,
                 command= lambda : get("*"),
                 font='calibri 12')
bDiv = Button(root,
                 text="/",
                 padx=40,
                 pady=10,
                 command= lambda : get('/'),
                 font='calibri 12')
bEqual = Button(root,        # main window
               text= "=",
               padx= 40,
               pady= 10,
               command= equal,        # call to equal()
               font= "calibri 12" )

#   putting the buttons on the screen
b1.grid( row=3, column=0 )
b2.grid( row=3, column=1 )
b3.grid( row=3, column=2 )

b4.grid( row=2, column=0 )
b5.grid( row=2, column=1 )
b6.grid( row=2, column=2 )

b7.grid( row=1, column=0 )
b8.grid( row=1, column=1 )
b9.grid( row=1, column=2 )

b0.grid( row=4, column=0 )
bDot.grid( row=4, column=1 )
bEqual.grid( row=4, column=2)

bAdd.grid( row=4, column=3 )
bSub.grid( row=3, column=3 )
bMult.grid( row=2, column=3 )
bDiv.grid( row=1, column=3 )

root.mainloop()