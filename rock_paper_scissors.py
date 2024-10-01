import random
import tkinter as tk
from tkinter import messagebox


# Function to determine the winner
def determine_winner(user_choice):
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    comp_choice = random.randint(1, 3)
    comp_choice_name = choices[comp_choice]

    user_choice_name = choices[user_choice]

    result_label.config(text=f"Computer chose: {comp_choice_name}")

    # Determine the outcome
    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == 1 and comp_choice == 3) or (user_choice == 2 and comp_choice == 1) or (
            user_choice == 3 and comp_choice == 2):
        result = "User wins!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer chose: {comp_choice_name}\n{result}")


# Function to reset the game
def reset_game():
    result_label.config(text="Make your choice!")


# Function to exit the game
def exit_game():
    window.quit()


# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x300")

# Game title
title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 20))
title_label.pack(pady=10)

# Instructions label
instruction_label = tk.Label(window, text="Select one of the options below:", font=("Arial", 14))
instruction_label.pack(pady=10)

# Result label
result_label = tk.Label(window, text="Make your choice!", font=("Arial", 14))
result_label.pack(pady=20)

# Buttons for Rock, Paper, and Scissors
rock_button = tk.Button(window, text="Rock", width=15, height=2, command=lambda: determine_winner(1))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=15, height=2, command=lambda: determine_winner(2))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=15, height=2, command=lambda: determine_winner(3))
scissors_button.pack(pady=5)

# Reset button
reset_button = tk.Button(window, text="Reset", width=10, command=reset_game)
reset_button.pack(pady=10)

# Exit button
exit_button = tk.Button(window, text="Exit", width=10, command=exit_game)
exit_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
