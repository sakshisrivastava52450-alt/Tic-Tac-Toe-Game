import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")
root.resizable(True, False)

board = [""] * 9
buttons = []

winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


def check_winner(player):
    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False


def is_draw():
    return "" not in board


def disable_board():
    for btn in buttons:
        btn.config(state="disabled")


def reset_game():
    global board
    board = [""] * 9

    for btn in buttons:
        btn.config(text="", state="normal")

    status_label.config(text="Your Turn (X)")


def computer_move():
    available_moves = [i for i in range(9) if board[i] == ""]

    if not available_moves:
        return

    move = random.choice(available_moves)

    board[move] = "O"
    buttons[move].config(text="O", state="disabled")

    if check_winner("O"):
        status_label.config(text="Computer Wins!")
        messagebox.showinfo("Game Over", "Computer Wins!")
        disable_board()
        return

    if is_draw():
        status_label.config(text="It's a Draw!")
        messagebox.showinfo("Game Over", "It's a Draw!")
        return

    status_label.config(text="Your Turn (X)")


def player_move(index):
    if board[index] != "":
        return

    board[index] = "X"
    buttons[index].config(text="X", state="disabled")

    if check_winner("X"):
        status_label.config(text="You Win!")
        messagebox.showinfo("Game Over", "Congratulations! You Win!")
        disable_board()
        return

    if is_draw():
        status_label.config(text="It's a Draw!")
        messagebox.showinfo("Game Over", "It's a Draw!")
        return

    status_label.config(text="Computer Thinking...")
    root.after(500, computer_move)


# Title
title_label = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

# Status
status_label = tk.Label(
    root,
    text="Your Turn (X)",
    font=("Arial", 14)
)
status_label.pack(pady=10)

# Game Board
game_frame = tk.Frame(root)
game_frame.pack()

for i in range(9):
    button = tk.Button(
        game_frame,
        text="",
        font=("Arial", 24, "bold"),
        width=5,
        height=2,
        command=lambda i=i: player_move(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=2,
        pady=2
    )

    buttons.append(button)

# Reset Button
reset_btn = tk.Button(
    root,
    text="New Game",
    font=("Arial", 14),
    command=reset_game
)
reset_btn.pack(pady=20)

root.mainloop()