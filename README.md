# Tic-Tac-Toe-Game
# Classic Tic-Tac-Toe in Python

A lightweight, interactive implementation of the classic **Tic-Tac-Toe** game built using Python. This project serves as an excellent demonstration of foundational programming concepts like data structure manipulation, game state loops, and win-condition algorithms.

---

## 🎮 Features
* **Two-Player Mode:** Play locally with a friend taking alternating turns.
* **Dynamic Board Update:** The 3x3 grid refreshes seamlessly after every valid move.
* **Input Validation:** Prevents players from picking already-occupied cells or entering invalid coordinates.
* **Smart Win/Tie Detection:** Instantly checks and announces horizontal, vertical, or diagonal victories, or handles draws cleanly.

---

## 🛠️ Prerequisites
To run this game, you only need Python installed on your system.
* **Python 3.x**

*(Note: If you used external libraries like `Tkinter` for a GUI or `Pygame`, you can install them using pip. No external modules are required if this is a standard console-based version).*

---

## 🚀 How to Run the Game

Follow these quick steps to get the game running locally on your computer:

### 1. Clone the Repository
```bash
git clone https://github.com
```

### 2. Navigate to the Directory
```bash
cd YOUR_REPOSITORY_NAME
```

### 3. Execute the Script
```bash
python main.py
```
*(Replace `main.py` with your actual filename if it differs, such as `tictactoe.py`).*

---

## 🎲 How to Play
1. The game is played on a grid that's 3 squares by 3 squares.
2. Player 1 is **X** and Player 2 is **O**. 
3. Players take turns putting their marks in empty squares.
4. To make a move, enter the number matching the board position when prompted (e.g., 1–9).
5. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
6. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

---

## 📁 Project Structure
```text
├── main.py          # Main game loop and core execution logic
└── README.md        # Documentation and user guide
```

---

## 📜 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
