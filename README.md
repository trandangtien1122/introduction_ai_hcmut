# CO3061-AI
The application solves Puzzle-pipe and Sudoku game according to https://www.puzzle-pipes.com/
## Puzzle-Pipes
We used both blind search and heuristics search to find series of action that can solve this game.
Two algorithms I use:
- Blind search: Breath-First Search
- Heuristics search: A* algorithm\n

To run this application, just run `pipe/main.py` file
```
python pipe/main.py
```

## Sudoku
We used both blind search minimum remaining values (RMV) and heuristics search to find series of action that can solve this game.
Two algorithms were used:
- Blind search: Breath-First Search
- Heuristics search

To run Sudoku application, just run `sudoku/main.py` file
```
python sudoku/main.py
```
<img src="sudoku/media/start_screen.PNG" width=50%><br>
### Make a move:
Click on a cell without a default value which will highlight the cell. Then simply enter a number with your keyboard. The number will show up as green if the move is a valid move based on the current numbers on the board or red if the move conflicts with an existing number. Note that a green number does not necessarily mean that the inputted number is the correct value for that cell. It simply means it is valid move based on the current board. Deleting a move can be done by pressing the Backspace or Delete key on a highlighted cell.<br>
<img src="sudoku/media/number_change.gif" width=50%>
### Reset the board:
The Reset button in the game will reset the board back to the staring position.<br>
<img src="sudoku/media/reset.gif" width=50%>
### Solve the board:
The Visual Solve button in the game will attempt to solve the baord from the current postion while also giving a visualization of the backtracking algorithm being used for the solver.<br>
<img src="sudoku/media/solve_start.gif" width=50%>
<img src="sudoku/media/solve_end.gif" width=50%><br>
If the board is unsolvable, the board will go back to the state it was before the button was pressed.<br>
<img src="sudoku/media/solve_invalid.gif" width=50%><br>
