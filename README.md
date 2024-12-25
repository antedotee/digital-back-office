# Rover Program

This program simulates the movement of a rover on a plateau based on a series of commands. The rover can move forward and rotate left or right.

## How to Run the Program

### Prerequisites

- Python 3.x installed on your system.

### Running the Program

1. Clone the repository or download the `program.py` file to your local machine.

2. Open a terminal (Command Prompt on Windows or Terminal on Mac).

3. Navigate to the directory where `program.py` is located.

#### On Windows

```sh
cd path\to\directory
python program.py
```

### On Mac

```sh
cd /path/to/directory
python3 program.py
```

### Input Format

1. First, enter the plateau's upper-right coordinates (e.g., 5 5).
2. For each rover, enter the initial position and direction (e.g., 1 2 N).
3. Enter the commands for the rover (e.g., LMLMLMLMM).

### Example

```sh
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

### Notes

- The program will terminate if an invalid command is encountered and print an error message.
- Ensure that the input format is correct to avoid errors.
- After giving all the input, press `Ctrl + D` to get the output.

### Example output

```sh
1 3 N
5 1 E
```

This output indicates the final positions and directions of the rovers after executing the commands.
