from data import TESTCASE
from searching import SearchPuzzle
import time
import psutil
import matplotlib.pyplot as plt


class PipesPuzzle:
    def __init__(self):
        self.init_state = None
        self.level = None
        self.create_puzzle()
        self.path = []
        self.dataForPlot = []

    def create_puzzle(self):
        """
        generate level and init_state from GOAL_STATES
        """
        print("Choose level:")
        print("level 1-3: simple")
        print("level 4-5: immediate")
        print("level 6-7  : advance (take too much time (about 10 minute or more)")
        self.level = int(input())
        if self.level > 7:
            quit()
        testcase = TESTCASE[f"level{self.level}"]
        self.init_state = testcase

    def solve(self, solve_choice):
        solver = SearchPuzzle()
        start_memory = psutil.Process().memory_info().rss
        startTime = time.time()
        print("Please wait....")
        if solve_choice == "1":
            self.path = solver.solve_dfs(self.init_state)
        elif solve_choice == "2":
            temp = solver.solve_astar(self.init_state)
            self.dataForPlot = temp[0]
            self.path = temp[1]
        else:
            print("You must choose 1 for DFS or 2 for A*.")
            exit(1)
        end_memory = psutil.Process().memory_info().rss
        execution_time = time.time() - startTime
        execution_memory = (end_memory - start_memory)
        print(f"Execution time: {execution_time} seconds")
        print(f"Execution memory: {execution_memory} bytes")
        ##
        '''
        solver.append(GOAL_STATES["level3"])
        '''

    def simulatePlot(self):
        plt.bar(*zip(*self.dataForPlot.items()))
        plt.xlabel('Number of step')
        plt.ylabel('Number of searching in step')
        plt.title('Statistics')
        plt.show()
