from tkinter import *

def convert_inches_to_cm():
    try:
        inches = float(inches_entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{inches} inches is equal to {centimeters:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number for inches.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

root = Tk()
root.title("Inches to Centimeters Converter")
root.geometry("300x150")

Label(root, text="Enter length in inches:").grid(row=0, column=0, padx=10, pady=10)

inches_entry = Entry(root, width=15)
inches_entry.grid(row=0, column=1, padx=10, pady=10)

convert_button = Button(root, text="Convert", command=convert_inches_to_cm)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()