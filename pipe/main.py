import puzzle as pl
import ui


if __name__ == "__main__":
  solve_choice = input("Solve by DFS or BestFirstSearch? \n1: DFS \n2: A*)")
  puzzle_pipes = pl.PipesPuzzle()
  puzzle_pipes.solve(solve_choice)
  puzzle_interface = ui.PuzzleInterface(puzzle_pipes)
  puzzle_interface.running()
  if len(puzzle_pipes.dataForPlot) != 0:
    show_statistic: str = input("Shall we show statistics about heuristic searching ?? (Y: Yes, other: No)")
    if show_statistic in ['Y', 'y']:
      puzzle_pipes.simulatePlot()
