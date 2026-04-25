import tkinter as tk
from tkinter import ttk
def check_strength(event=None):
    password = entry.get().strip()
    length = len(password)
    strength_text = "Enter a password"
    color = "gray"
    
    if length == 0:
        strength_text = "Enter a password"
        color = "gray"
    elif length <= 5:
        strength_text = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength_text = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength_text = "Strong"
        color = "light green"
    elif length > 12:
        strength_text = "Very Strong"
        color = "dark green"
    strength_label.config(text=f"Strength: {strength_text}", foreground=color)
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.resizable(False, False)
style = ttk.Style()
style.theme_use('clam') 
title_label = tk.Label(root, text="Password Strength Checker", 
                      font=("Arial", 16, "bold"), fg="#333333")
title_label.pack(pady=20)
instr_label = tk.Label(root, text="Enter your password below:", 
                      font=("Arial", 10))
instr_label.pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12), width=30, show="*")
entry.pack(pady=10)
entry.bind("<KeyRelease>", check_strength) 
strength_label = tk.Label(root, text="Strength: Enter a password", 
                         font=("Arial", 14, "bold"), fg="gray")
strength_label.pack(pady=30)
info_text = """Password Strength Rules:
• 1-5 characters  → Weak (Red)
• 6-8 characters  → Medium (Yellow)
• 9-12 characters → Strong (Light Green)
• >12 characters  → Very Strong (Dark Green)"""

info_label = tk.Label(root, text=