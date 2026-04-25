import tkinter as tk
from tkinter import messagebox
import random

def play_round(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = ""
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    messagebox.showinfo("Result", f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")

instruction_label = tk.Label(root, text="Choose your move:", font=("Arial", 12))
instruction_label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_round("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_round("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_round("Scissors"))
scissors_button.pack(pady=5)

root.mainloop()