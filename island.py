"""
Island Detection Program

This program processes grid-based maps (from text files) to identify and analyze islands.
An island is formed by connected '1's in the grid, where connections can be made in 8 directions
(North, South, East, West, Northeast, Northwest, Southeast, Southwest).

The program:
1. Reads a grid from a text file where '1' represents land and '0' represents water
2. Constructs a graph representation where each land cell becomes a node
3. Creates edges between adjacent land cells in all 8 directions
4. Can be used to identify distinct islands and analyze their properties

The implementation uses a Graph class with Nodes that maintain directional connections
to neighboring land cells, allowing for efficient island traversal and analysis.
"""

def read_file_to_char_arrays(filename):
    """
    Read a file and convert it into a 2D array of characters.
    Each line becomes a list of characters.
    """
    char_arrays = []
    with open(filename, 'r') as file:
        for line in file:
            # Strip newline and convert string to list of chars
            char_arrays.append(list(line.strip()))
    return char_arrays

class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        # Initialize edges for 8 directions (N, S, E, W, NE, NW, SE, SW)
        self.edges = {
            'N': None,   # North
            'S': None,   # South 
            'E': None,   # East
            'W': None,   # West
            'NE': None,  # Northeast
            'NW': None,  # Northwest
            'SE': None,  # Southeast
            'SW': None   # Southwest
        }

class Graph:
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes by (row,col) coordinates
        
    def add_node(self, row, col, value):
        """Add a new node to the graph"""
        node = Node(row, col, value)
        self.nodes[(row,col)] = node
        return node
        
    def connect_nodes(self, node1, node2, direction):
        """Connect two nodes bidirectionally based on direction"""
        # Map of opposite directions
        opposites = {
            'N': 'S',
            'S': 'N',
            'E': 'W', 
            'W': 'E',
            'NE': 'SW',
            'SW': 'NE',
            'NW': 'SE',
            'SE': 'NW'
        }
        
        # Connect nodes in both directions
        node1.edges[direction] = node2
        node2.edges[opposites[direction]] = node1


def build_graph(grid):
    """Build a graph from a 2D grid where each cell becomes a node with value 0 or 1"""
    graph = Graph()
    
    # Create nodes for each cell in grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            value = int(grid[row][col])  # Convert char to int
            graph.add_node(row, col, value)
            
    # Connect nodes in all 8 directions
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            node = graph.nodes[(row,col)]
            
            # Check all 8 adjacent cells
            directions = {
                (-1,0): 'N',   # North
                (1,0): 'S',    # South
                (0,1): 'E',    # East 
                (0,-1): 'W',   # West
                (-1,1): 'NE',  # Northeast
                (-1,-1): 'NW', # Northwest
                (1,1): 'SE',   # Southeast
                (1,-1): 'SW'   # Southwest
            }
            
            for (dr,dc), direction in directions.items():
                new_row = row + dr
                new_col = col + dc
                
                # Check if adjacent cell is within grid bounds
                if (0 <= new_row < len(grid) and 
                    0 <= new_col < len(grid[0])):
                    neighbor = graph.nodes[(new_row,new_col)]
                    graph.connect_nodes(node, neighbor, direction)                    
    return graph

def traverse_n_count_islands(graph):
    def mark_all_neighbors_zero(node):
        """Mark all connected neighbors with value 1 to 0 recursively"""
        for direction, neighbor in node.edges.items():
            if neighbor is not None and neighbor.value == 1:
                neighbor.value = 0
                mark_all_neighbors_zero(neighbor)

    island_count = 0
    
    # Iterate through all nodes in normal order
    for row in range(len(graph.nodes)):
        for col in range(len(graph.nodes)):
            node = graph.nodes.get((row, col))
            if node is not None and node.value == 1:
                # Found an island
                island_count += 1
                node.value = 0
                # Mark all connected 1's as visited
                mark_all_neighbors_zero(node)
                
    return island_count


def main():
    # Read the input file
    grid = read_file_to_char_arrays('input2.txt')
    graph = build_graph(grid)

    # Print first 20 nodes traversing East
    print("\nTraversing East from starting node (2,0):")
    current = graph.nodes[(2,0)]
    count = 0

    island_count = traverse_n_count_islands(graph)
    print(f"Number of islands: {island_count}")
    
    while current and count < 20:
        print(f"Node at ({current.row},{current.col}): {current.value}")
        if 'E' not in current.edges:
            break
        current = current.edges['E']
        count += 1

    # Print first line of grid
    print("\nFirst line of grid:")
    for col in range(len(grid[4])):
        print(grid[4][col], end='')
    print()


if __name__ == "__main__":
    main()
