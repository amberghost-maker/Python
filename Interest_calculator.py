import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Interest Calculator App")
root.geometry("400x400")
root.config(bg="#e6f2ff")

# Heading
title_label = tk.Label(
    root,
    text="Interest Calculator App",
    font=("Arial", 16, "bold"),
    bg="#e6f2ff"
)
title_label.pack(pady=15)

# Frame for inputs
frame = tk.Frame(root, bg="#e6f2ff")
frame.pack(pady=10)

# Principal
tk.Label(frame, text="Principal Amount:", font=("Arial", 11), bg="#e6f2ff")\
    .grid(row=0, column=0, padx=10, pady=8, sticky="e")
principal_entry = tk.Entry(frame)
principal_entry.grid(row=0, column=1)

# Time
tk.Label(frame, text="Time Period (years):", font=("Arial", 11), bg="#e6f2ff")\
    .grid(row=1, column=0, padx=10, pady=8, sticky="e")
time_entry = tk.Entry(frame)
time_entry.grid(row=1, column=1)

# Rate
tk.Label(frame, text="Rate of Interest (%):", font=("Arial", 11), bg="#e6f2ff")\
    .grid(row=2, column=0, padx=10, pady=8, sticky="e")
rate_entry = tk.Entry(frame)
rate_entry.grid(row=2, column=1)

# Function to calculate interest
def calculate():
    p = float(principal_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())

    simple_interest = (p * t * r) / 100
    compound_interest = p * (math.pow((1 + r / 100), t)) - p

    si_label.config(text=f"Simple Interest: {simple_interest:.2f}")
    ci_label.config(text=f"Compound Interest: {compound_interest:.2f}")

# Calculate Button
calc_btn = tk.Button(
    root,
    text="Calculate Interest",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    command=calculate
)
calc_btn.pack(pady=15)

# Result Labels
si_label = tk.Label(root, text="Simple Interest: ", font=("Arial", 11), bg="#e6f2ff")
si_label.pack(pady=5)

ci_label = tk.Label(root, text="Compound Interest: ", font=("Arial", 11), bg="#e6f2ff")
ci_label.pack(pady=5)

# Run application
root.mainloop()
