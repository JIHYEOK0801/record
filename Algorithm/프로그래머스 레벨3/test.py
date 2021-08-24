from itertools import permutations
from copy import deepcopy
def bfs(start,end, board, i):

    def check_up(position):
        x = position[0] - 1
        y = position[1]
        if x < 0:
            return []
        else:
            return [x,y]

    def check_right(position):
        x = position[0]
        y = position[1] + 1
        if y >= len(board[0]):
            return []
        else:
            return [x,y]

    def check_down(position):
        x = position[0] + 1
        y = position[1]
        if x >= len(board):
            return []
        else:
            return [x,y]

    def check_left(position):
        x = position[0]
        y = position[1] - 1
        if y < 0:
            return []
        else:
            return [x,y]

    def check_ctrl_up(position):
        x = position[0] - 1
        y = position[1]
        for i in range(x,-1,-1):
            if board[i][y] != 0:
                x = i
                break
        else:
            x = 0
        return [x,y]

    def check_ctrl_right(position):
        x = position[0]
        y = position[1] + 1
        
        for j in range(y, len(board[0])):
            if board[x][j] != 0:
                y = j
                break
        else:
            y = len(board[0]) - 1
            
        return [x,y]

    def check_ctrl_down(position):
        x = position[0] + 1
        y = position[1]
        
        for i in range(x, len(board)):
            if board[i][y] != 0:
                x = i
                break
        else:
            x = len(board) - 1
            
        return [x,y]
        

    def check_ctrl_left(position):
        x = position[0]
        y = position[1] - 1
        
        for j in range(y, -1, -1):
            if board[x][j] != 0:
                y = j
                break
        else:
            y = 0
            
        return [x,y]

    visited = []
    count = -1
    routes = [start]
    while(routes):
        print(routes)
        count += 1
        add_route = []

        for route in routes:
            if route == end:
                if i > 1:
                    if (board[start[0]][start[1]] == board[end[0]][end[1]]):
                        board[start[0]][start[1]] = 0
                        board[end[0]][end[1]] = 0
                return count

            visited.append(route)

            up = check_up(route)
            if up:
                if up not in add_route:
                    add_route.append(up)

            right = check_right(route)
            if right:
                if right not in add_route:
                    add_route.append(right)

            down = check_down(route)
            if down:
                if down not in add_route:
                    add_route.append(down)
                
            left = check_left(route)
            if left:
                if left not in add_route:
                    add_route.append(left)

            ctrl_up = check_ctrl_up(route)
            if ctrl_up:
                if ctrl_up not in add_route:
                    add_route.append(ctrl_up)

            ctrl_right = check_ctrl_right(route)
            if ctrl_right:
                if ctrl_right not in add_route:
                    add_route.append(ctrl_right)

            ctrl_down = check_ctrl_down(route)
            if ctrl_down:
                if ctrl_down not in add_route:
                    add_route.append(ctrl_down)

            ctrl_left = check_ctrl_left(route)
            if ctrl_left:
                if ctrl_left not in add_route:
                    add_route.append(ctrl_left)
            print(up,right,down,left,ctrl_up,ctrl_right,ctrl_down,ctrl_left)
        routes = add_route

    return count

def solution(board, r, c):
    answer = float('inf')

    count = 0
    copy_board = deepcopy(board)
    
    orders = [[0, 1], [0, 0], [3, 3], [0, 3], [3, 0], [2, 1], [1, 2]]
    print(orders)
    for i in range(1, len(orders)):
        count += bfs(orders[i-1], orders[i], copy_board, i)
        print(count)
        print(copy_board,'\n')
        
    if count < answer:
        answer = count

    return answer
    


# print(solution([[1,0,0,0],[2,0,0,0],[0,0,0,2],[0,0,1,0]], 1, 0))
#print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))