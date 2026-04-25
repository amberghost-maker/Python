from tkinter import *
from datetime import date
def calculate_age():
    try:
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())
        today = date.today()
        dob = date(birth_year, birth_month, birth_day)
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result_label.config(text=f"Your current age is: {age} years")
    except ValueError:
        result_label.config(text="Please enter valid numbers for day, month, and year.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")
root = Tk()
root.title("Age Calculator")
root.geometry("400x250")
Label(root, text="Enter your Date of Birth").grid(row=0, column=0, columnspan=3, pady=10)
Label(root, text="Day:").grid(row=1, column=0, padx=5, pady=5)
day_entry = Entry(root, width=5)
day_entry.grid(row=1, column=1, padx=5, pady=5)
Label(root, text="Month:").grid(row=2, column=0, padx=5, pady=5)
month_entry = Entry(root, width=5)
month_entry.grid(row=2, column=1, padx=5, pady=5)
Label(root, text="Year:").grid(row=3, column=0, padx=5, pady=5)
year_entry = Entry(root, width=5)
year_entry.grid(row=3, column=1, padx=5, pady=5)
calculate_button = Button(root, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=4, column=0, columnspan=3, pady=10)
result_label = Label(root, text="")
result_label.grid(row=5, column=0, columnspan=3, pady=5)
root.mainloop()