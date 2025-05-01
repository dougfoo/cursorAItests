import random

def create_island(grid, start_row, start_col, size):
    # Create a larger island starting from a point and growing outward
    rows, cols = len(grid), len(grid[0])
    queue = [(start_row, start_col)]
    visited = set(queue)
    
    # Add diagonal directions to allow more natural island shapes
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), 
                 (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    while queue and len(visited) < size:
        # Select random point from queue for more organic growth
        row, col = queue.pop(random.randint(0, len(queue)-1) if queue else 0)
        grid[row][col] = 1
        
        # Try multiple growth attempts from each cell for larger, more connected islands
        growth_attempts = 3  # Try to grow multiple times from each cell
        for _ in range(growth_attempts):
            # Randomize direction order for more organic growth
            random.shuffle(directions)
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    (new_row, new_col) not in visited):
                    # Higher chance to grow for more dense islands
                    if random.random() < 0.85:  # 85% chance to grow in this direction
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        if len(visited) >= size:
                            return

def generate_island_grid(rows=30, cols=80, num_islands=15):
    # Initialize grid with all zeros
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Create islands
    for _ in range(num_islands):
        # Random starting position (keep away from edges)
        start_row = random.randint(3, rows-4)
        start_col = random.randint(3, cols-4)
        
        # Random island size between 20 and 75 cells
        size = random.randint(20, 75)
        
        create_island(grid, start_row, start_col, size)
    
    return grid

# Generate the grid
grid = generate_island_grid()

# Write to file
with open('input.txt', 'w') as f:
    for row in grid:
        f.write(''.join(map(str, row)) + '\n')

print("Generated input.txt with 30x80 grid containing 15 much larger islands") 