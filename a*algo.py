import heapq

class Node:
    def __init__(self, position, g=0, h=0):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def heuristic(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def a_star(grid, start, end):
    open_list = []
    heapq.heappush(open_list, Node(start, 0, heuristic(start, end)))
    closed_set = set()
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.position == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        closed_set.add(current_node.position)
        
        for move in moves:
            neighbor_pos = (current_node.position[0] + move[0], current_node.position[1] + move[1])
            
            if (0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] != 1 and neighbor_pos not in closed_set):
                
                g_cost = current_node.g + 1
                h_cost = heuristic(neighbor_pos, end)
                
                neighbor_in_open_list = next((node for node in open_list if node.position == neighbor_pos), None)
                
                if neighbor_in_open_list:
                    if g_cost < neighbor_in_open_list.g:
                        neighbor_in_open_list.g = g_cost
                        neighbor_in_open_list.f = g_cost + h_cost
                        neighbor_in_open_list.parent = current_node
                else:
                    neighbor_node = Node(neighbor_pos, g_cost, h_cost)
                    neighbor_node.parent = current_node
                    heapq.heappush(open_list, neighbor_node)
    
    return None

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = a_star(grid, start, end)

if path:
    print("Path found:", path)
else:
    print("No path found")
