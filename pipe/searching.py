from data import HEADING
from state_and_node import Node


class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0


class SearchPuzzle:

    def generateNode(self, current: Node) -> list:
        '''
        Hàm sinh tất cả trạng thái có thể có và trả về dạng list.
        '''
        ans = []    
        for i in range(5):
            for j in range(5):             
                for k in HEADING:                   
                    if current.state.head[i][j]["heading"] == k:
                        continue   
                    newNode = Node(current.state.head, [i, j], current)
                    newNode.state.head[i][j]["heading"] = k
                    newNode.state.triggledAt([i, j])
                    newNode.step = current.step + 1
                    ans.append(newNode)
        return ans

    def getPath(self, end_node: Node) -> list:
        '''
        Trả về list các state từ state đầu tiên
        '''
        ans = []
        temp = end_node
        while temp:
            ans.insert(0,temp.state)
            temp = temp.previous
        return ans

    def hx(self, current: Node) -> int:
        ans = 0
        ans = ans - 5 * current.state.countBump
        if current.previous is not None:
            if current.state.countBump == current.previous.state.countBump:
                state = False
                for i in range(5):
                    for j in range(5):
                        if current.state.head[i][j]["bump"] != current.previous.state.head[i][j]["bump"]:
                            ans -= 2
                            state = not state
                        elif current.state.head[i][j]["bump"] and current.previous.state.head[i][j]["bump"]:
                            if current.state.head[i][j]["heading"] != current.previous.state.head[i][j]["heading"]:
                                ans -= 2
                                state = not state
                        if state:
                            break
                    if state:
                        break
                if state:
                    ans += 2
        
        if current.state.countBump:
            for i in [0, 4]:
                for j in range(5):
                    list1 = current.state.getAngle(current.state.head[i][j])
                    if i == 0:
                        if 90 in list1:
                            ans += 1
                            if current.state.head[i][j]["bump"]:
                                ans += 5
                        else:
                            ans -= 2
                    if i == 4:
                        if 270 in list1:
                            ans += 1
                            if current.state.head[i][j]["bump"]:
                                ans += 5
                        else:
                            ans -= 2
            
            for j in [0, 4]:
                for i in range(5):
                    list1 = current.state.getAngle(current.state.head[i][j])
                    if j == 0 and 180 in list1:
                        ans += 1
                        if current.state.head[i][j]["bump"]:
                            ans += 5
                    else:
                        ans -= 2
                    if j == 4 and 0 in list1:
                        ans += 1   
                        if current.state.head[i][j]["bump"]:
                            ans += 5
                    else:
                        ans -= 2     

        # Xem có vòng lặp không: state, oy,ox
        if current.state.checkRecursionBump(current.rotate[0], current.rotate[1]):
            ans += 2000
        return ans 

    def gx(self, current: Node):
        if current is None:
            return 0
        return current.step*2

    def fx(self, current: Node) -> int:
        return self.gx(current) + self.hx(current)

    def solve_astar(self, init_state: list):
        """
        BestFirstSearch for the path from init_state to goal_state and save in self.path
        """
        head = Node(init_state, [2, 2], None)
        head.heuristics = self.fx(head)
        head.step = 0
        openList = [[self.fx(head), head]]
        dataForPlot = {0: 1}
        closeList = []
        while len(openList) != 0:
            current_state = openList.pop(0)
            #add new step to dataForPlot if its doesn't have step key, else increase step value.
            if current_state[1].step not in dataForPlot:
                dataForPlot.update({current_state[1].step:1})
            else:
                dataForPlot[current_state[1].step] += 1
            if current_state[1] not in closeList:
                closeList.append(current_state[1])
                if current_state[1].state.countBump  == 25:
                    print("Successfully :))")
                    break
                newStateList = self.generateNode(current_state[1])
                for newNode in newStateList:
                    if newNode not in closeList and newNode not in(obj for obj in openList):
                        openList.append([self.fx(newNode), newNode]) 
                # Sắp xếp openList theo thứ tự tg nào có heuristics nhỏ hơn ưu tiên trước.
                openList.sort(key=lambda x: int(x[0]))
        print("Number of state: ", len(openList) + len(closeList))
        return dataForPlot, self.getPath(closeList.pop(len(closeList) - 1))

    def solve_dfs(self, init_state: list) -> list:
        """
        DFS for the path from init_state to goal_state and save in self.path
        """
        open_list = Stack()
        visited = []
        first_node = Node(init_state, [0, 0], None)
        open_list.push(first_node)
        while not open_list.isEmpty():
            current_node = open_list.pop()
            visited.append(current_node)
            print(len(open_list.list))
            if current_node.state.countBump == 25:
                return self.getPath(current_node)
            
            successors = self.generateNode(current_node)
            for item in successors:
                if item not in visited and item not in open_list.list:
                    open_list.push(item)     
        return self.getPath(visited[len(visited) - 1])
