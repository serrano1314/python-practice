from tkinter import *
from tkinter_custom_button import TkinterCustomButton as customButton

root = Tk()
root.geometry('200x200')

testBut=customButton(text="hello",corner_radius=20)
testBut.pack(pady=10)

root.mainloop()