## ⭕❌ Tic-Tac-Toe

This project is a simple console-based game written in Python. Core gameplay functionality is fully implemented, allowing two players to play Tic-Tac-Toe from the terminal.

## Overview

Tic-Tac-Toe is a classic two-player game where players take turns placing Xs and Os on a 3×3 grid. The goal is to be the first player to align three of your symbols horizontally, vertically, or diagonally. This project is designed as a beginner-friendly exercise to practice Python fundamentals such as functions, loops, conditionals, lists, and input validation.

## Key Features

Two-player gameplay (Player X vs Player O)
Console-based board display
Turn-based input handling
Validation for invalid or occupied moves
Automatic win detection (rows, columns, diagonals)
Draw detection when the board is full

## Tech Stack

Language: Python 3
Environment: Terminal / Command Line
Libraries: None (uses only built-in Python features)

## Example Gameplay Output
Game interaction includes:

Board display with row and column separators
Clear prompts for player turns
Win or draw messages at the end of the game

## Sample board view:
X | O | X
---------

## O | X | O

|   | X

## Project Structure
Single-file Python program containing:

print_board(board) – Displays the current game board
check_winner(board) – Checks for a win or draw condition
tic_tac_toe() – Controls game flow, player turns, and input

## How to Run

1. Ensure Python 3 is installed.
2. Save the file as tic_tac_toe.py.
3. Run the program from the terminal:

python tic_tac_toe.py

## Learning Goals
Practice working with 2D lists
Understand function decomposition
Apply conditionals and loops in a real program
Handle user input and basic error handling
