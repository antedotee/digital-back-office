def move_rover(plateau, start_position, commands):
    x, y, direction = start_position
    directions = ['N', 'E', 'S', 'W']  # Order of directions to handle rotation
    dx_dy = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}  # Movement deltas

    for command in commands:
        if command == 'L':
            direction = directions[(directions.index(direction) - 1) % 4]
        elif command == 'R':
            direction = directions[(directions.index(direction) + 1) % 4]
        elif command == 'M':
            dx, dy = dx_dy[direction]
            new_x, new_y = x + dx, y + dy
            # Ensure the rover stays within plateau boundaries
            if 0 <= new_x <= plateau[0] and 0 <= new_y <= plateau[1]:
                x, y = new_x, new_y

    return x, y, direction


def main():
    # Read input
    plateau_coords = list(map(int, input().strip().split()))
    plateau = (plateau_coords[0], plateau_coords[1])

    rovers_data = []
    while True:
        try:
            position = input().strip()
            commands = input().strip()
            rovers_data.append((position, commands))
        except EOFError:
            break

    # Process each rover
    for rover in rovers_data:
        start_position = rover[0].split()
        x, y, direction = int(start_position[0]), int(start_position[1]), start_position[2]
        commands = rover[1]
        final_position = move_rover(plateau, (x, y, direction), commands)
        print(*final_position)


if __name__ == "__main__":
    main()
