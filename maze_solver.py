# Name - Yukta Batra
# G Number - G01489018
from pyamaze import maze, agent, textLabel
from queue import PriorityQueue
import math

# Function to calculate Euclidean distance between two nodes
def euclidean_distance(node1, node2):
    return math.sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)

# Function to calculate Manhattan distance between two nodes
def manhattan_distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

# A* Search Algorithm implementation
def a_star(m):
    start = (m.rows, m.cols)# Define start position (bottom-right corner)
    goal = (1, 1) # Define goal position (top-left corner)
    
    open_set = PriorityQueue()
    open_set.put((0, start))# Initialize priority queue with start node
    
    g_score = {node: float('inf') for node in m.grid} # Initialize g(n) costs
    g_score[start] = 0 # Cost to reach start node is 0
    
    f_score = {node: float('inf') for node in m.grid} # Initialize f(n) costs
    f_score[start] = manhattan_distance(start, goal) # Compute initial heuristic estimate
    
    came_from = {} # Dictionary to store the optimal path
    
    while not open_set.empty():
        _, current = open_set.get() # Get node with lowest f(n) value
        
        if current == goal: # If goal is reached, reconstruct path
            path = {}
            while current in came_from:
                prev = came_from[current]
                path[prev] = current
                current = prev
            return path # Return the shortest path
        
        for direction in 'ESNW':  #  # Iterate through possible movements (East, South, North, West)
            if m.maze_map[current][direction]: # Check if movement is allowed
                if direction == 'E':
                    neighbor = (current[0], current[1] + 1)
                elif direction == 'W':
                    neighbor = (current[0], current[1] - 1)
                elif direction == 'N':
                    neighbor = (current[0] - 1, current[1])
                else:
                    neighbor = (current[0] + 1, current[1])
                
                temp_g_score = g_score[current] + euclidean_distance(current, neighbor) # Compute new cost
                
                if temp_g_score < g_score[neighbor]: # If new cost is lower, update scores
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + manhattan_distance(neighbor, goal)
                    open_set.put((f_score[neighbor], neighbor)) # Push neighbor to priority queue
    
    return None # Return None if no path is found

# Function to create and solve the maze
def main(rows, cols):
    m = maze(rows, cols) # Create a maze with specified dimensions
    m.CreateMaze()  # Generate a solvable maze
    
    path = a_star(m) # Solve the maze using A* algorithm
    
    a = agent(m, footprints=True) # Create an agent to traverse the maze
    if path:
        m.tracePath({a: path}) # Visualize the shortest path
    
    textLabel(m, 'Path Length', len(path) + 1 if path else 'No Path Found')
    m.run()

if __name__ == "__main__":
    main(10, 10)  # Change the maze size as needed
