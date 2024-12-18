from collections import deque

def parse_input(filename):
    corrupted = set()
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i >= 1024:  # Only first kilobyte
                break
            x, y = map(int, line.strip().split(','))
            corrupted.add((x, y))
    return corrupted

def find_shortest_path(corrupted, max_size=71):
    start = (0, 0)
    end = (max_size-1, max_size-1)
    
    # BFS queue: (position, steps)
    queue = deque([(start, 0)])
    visited = {start}
    
    # Directions: up, right, down, left
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    while queue:
        pos, steps = queue.popleft()
        x, y = pos
        
        if pos == end:
            return steps
            
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            new_pos = (new_x, new_y)
            
            if (0 <= new_x < max_size and 
                0 <= new_y < max_size and 
                new_pos not in corrupted and 
                new_pos not in visited):
                queue.append((new_pos, steps + 1))
                visited.add(new_pos)
    
    return -1  # No path found

def main():
    corrupted = parse_input('input.txt')
    steps = find_shortest_path(corrupted)
    print(f"Minimum steps needed: {steps}")

if __name__ == '__main__':
    main()
