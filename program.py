def move_rover(plateau, start_position, commands):
    x, y, direction = start_position
    left_turn = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    right_turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    direction_dict = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)} 

    for command in commands:
        if command == 'L':
            direction = left_turn[direction]
        elif command == 'R':
            direction = right_turn[direction]
        elif command == 'M':
            dx, dy = direction_dict[direction]
            if 0 <= x + dx <= plateau[0] and 0 <= y + dy <= plateau[1]:
                x += dx
                y += dy
            else:
                raise ValueError(f"Move ignored: ({x + dx}, {y + dy}) is outside plateau boundaries.")
        else:
            raise ValueError(f"Invalid command '{command}' ignored.")

    return x, y, direction


def main():
    plateau = tuple(map(int, input().strip().split()))

    results = []
    try:
        while True:
            position_input = input().strip()
            if not position_input:
                break
            x, y, direction = position_input.split()
            x, y = int(x), int(y)

            commands = input().strip()

            final_position = move_rover(plateau, (x, y, direction), commands)
            results.append(f"{final_position[0]} {final_position[1]} {final_position[2]}")
    except ValueError as e:
        print(e)
    except EOFError:
        pass

    print("\n".join(results))


if __name__ == "__main__":
    main()
