from collections import deque

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.actions = action
        self.cost = cost


    def move_blank(state, direction):

        #find the blank
        for i, row in enumerate(state):
            if 0 in row:
                x, y = i, row.index(0)
                break
        
        #defining possible movements
        moves = {

            'up': (x - 1, y),
            'down': (x + 1, y),
            'left': (x, y - 1),
            'right': (x, y + 1)
        }

        if direction in moves:
            new_x, new_y = moves[direction]
            if 0 <= new_x < len(state) and 0 <= new_y < len(state[0]):
                # Create a copy of the state and swap positions
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                return new_state
        return None  # Invalid move



def bfs(initial_state, goal_state):
    #create the initial node 
    start_solving_node = Node(state=initial_state)

    #use a queue for bfs 
    queue = deque([start_solving_node])
    explored = set()

    while queue:
        current_node = queue.popleft()

        #goal test 
        if current_node.state  == goal_state:
            return current_node #goal found
        
        explored.add(tuple(map(tuple, current_node.state))) # mark as explored

        # Expand children
        for action in ['up', 'down', 'left', 'right']:
            new_state = Node.move_blank(current_node.state, action)
            if new_state and tuple(map(tuple, new_state)) not in explored:
                child_node = Node(state=new_state, parent=current_node, action=action, cost=current_node.cost + 1)
                queue.append(child_node)
        
    return None # No sulution found


#reconstruct the solution path 
def reconstruct_path(node):
    path = []
    while node:
        path.append(node.actions)
        node = node.parent
    return path[::-1]  # Reverse the path



#initial state of the puzzle 
initial_state = [
    [1,2,3],
    [4,0,5],
    [6,7,8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = bfs(initial_state, goal_state)
if solution:
    print("Solution found!")
    path = reconstruct_path(solution)
    print("Path to goal:", path)
else:
    print("No solution found.")


# state after moving the blank to the right 
next_state = [
    [1, 2, 3],
    [4, 5, 0],
    [6, 7, 8]
]

# state after moving the blank down 
next_next_state = [
    [1, 2, 3],
    [4, 5, 8],
    [6, 7, 0]
]

next_next_next_state = Node.move_blank(next_next_state, 'left')

next_next_next_next_state = Node.move_blank(next_next_next_state, 'left')

# creating the initial state
start_node = Node(state=initial_state)

#create the next node, with the action move right
next_node = Node(state=next_state, parent=start_node, action='move right', cost=1)

#create the next node, with the action move down
next_next_node = Node(state=next_next_state, parent=next_node, action='move down', cost=1)

# create the next node with the action move left
next_next_next_node = Node(state=next_next_next_state, parent=next_next_node, action='move left', cost=1)


# create the next node with the action move left
next_next_next_next_node = Node(state=next_next_next_next_state, parent=next_next_next_node, action='move left', cost=1)
#print the nodes
print("start Node ", start_node.state)
print("Next Node ", next_node.state)
print("next Next Node ", next_next_node.state)
print("next next Next Node ", next_next_next_node.state)
print("next next next Next Node ", next_next_next_next_node.state)
# print("Actions ", next_node.actions)
print("Cost ", next_node.cost)

