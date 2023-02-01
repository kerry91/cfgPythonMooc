import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk ()
root.title('Spelling Checker')
root.geometry('650x400')
root.config(background = 'white')

def check_spelling():
    word = enter_text.get()
    a = TextBlob (word)
    right =  str(a.correct())

    cs = Label(root, text="The correct spelling is:", font=("Times", 20), bg="white", fg="black")
    cs.place(x=50, y=250)
    spell.config(text=right)


heading = Label(root, text = "Spell Checker", font = ("Times", "24", "bold"), bg = 'white', fg = 'black')
heading.pack(pady = (50,0))
enter_text = Entry(root, justify="center", width=30, font=("Times", "24", "bold"), bg = "white", border=2)
enter_text.pack(pady = 10)
enter_text.focus()

Button=Button(root, text = "check", font=("Times", "24", "bold"), bg="green", fg="white", command=check_spelling)
Button.pack()

spell = Label(root, font=("Times", "24", "bold"), bg="white", fg="black")
spell.place(x=375, y=245)
root.mainloop()
