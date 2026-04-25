from tkinter import *
from datetime import date
root = Tk()
root.title('Number Product App')
root.geometry('400x300')
lbl = Label(text="Enter Two Numbers Below", fg="white", bg="#072F5F", height=1, width=300)
num1_lbl = Label(text="First number", bg="#3895D3")
num1_entry = Entry()
num2_lbl = Label(text="Second number", bg="#3895D3")
num2_entry = Entry()
def display():
	try:
		num1 = float(num1_entry.get())
		num2 = float(num2_entry.get())
		product = num1 * num2
		text_box.delete('1.0', END) 
		text_box.insert(END, f"The product of {num1} and {num2} is: {product}\n")
	except ValueError:
		text_box.delete('1.0', END)
		text_box.insert(END, "Please enter valid numbers!")
text_box = Text(height=3)
btn = Button(text="Calculate Product", command=display, height=1, bg="#1261A0", fg='white')
lbl.pack()
num1_lbl.pack()
num1_entry.pack()
num2_lbl.pack()
num2_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()