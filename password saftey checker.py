from tkinter import *
def check_password_strength():
    password = password_entry.get()
    length = len(password)
    strength = ""
    if length == 0:
        strength = "Please enter a password"
    elif length < 6:
        strength = "Very Weak"
    elif 6 <= length < 10:
        strength = "Weak"
    elif 10 <= length < 14:
        strength = "Moderate"
    elif 14 <= length < 18:
        strength = "Strong"
    else:
        strength = "Very Strong"
    strength_label.config(text=f"Password Strength: {strength}")
root = Tk()
root.title("Password Strength Checker")
root.geometry("400x150")
Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
password_entry = Entry(root, width=30, show="*")
password_entry.grid(row=0, column=1, padx=10, pady=10)
check_button = Button(root, text="Check Strength", command=check_password_strength)
check_button.grid(row=1, column=0, columnspan=2, pady=10)
strength_label = Label(root, text="")
strength_label.grid(row=2, column=0, columnspan=2, pady=5)
root.mainloop()