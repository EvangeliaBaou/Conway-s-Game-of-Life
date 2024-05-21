import random

# Define cell state constants
DEAD = 0
ALIVE = 1

def get_neighbors(grid, row, col):
  """
  Calculates the number of live neighbors a cell has.

  Args:
      grid: A list of lists representing the game grid.
      row: The row index of the cell.
      col: The column index of the cell.

  Returns:
      The number of live neighbors the cell has.
  """
  rows, cols = len(grid), len(grid[0])
  live_neighbors = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      # Skip checking the cell itself and out-of-bounds cells
      if (i == 0 and j == 0) or (row + i < 0 or row + i >= rows or col + j < 0 or col + j >= cols):
        continue
      live_neighbors += grid[row + i][col + j]
  return live_neighbors

def update_cell(grid, row, col):
  """
  Updates the state of a cell based on the Game of Life rules.

  Args:
      grid: A list of lists representing the game grid.
      row: The row index of the cell.
      col: The column index of the cell.

  Returns:
      The new state (DEAD or ALIVE) of the cell.
  """
  neighbors = get_neighbors(grid, row, col)
  current_state = grid[row][col]
  if current_state == ALIVE:
    if neighbors < 2 or neighbors > 3:
      return DEAD
  else:
    if neighbors == 3:
      return ALIVE
  return current_state

def update_grid(grid):
  """
  Updates the entire game grid to the next generation.

  Args:
      grid: A list of lists representing the game grid.

  Returns:
      A new grid representing the next generation.
  """
  new_grid = []
  rows, cols = len(grid), len(grid[0])
  for row in range(rows):
    new_row = []
    for col in range(cols):
      new_row.append(update_cell(grid, row, col))
    new_grid.append(new_row)
  return new_grid

def print_grid(grid):
  """
  Prints the current state of the game grid to the console.
  """
  for row in grid:
    for cell in row:
      if cell == ALIVE:
        print("*", end="")
      else:
        print(" ", end="")
    print()

def main():
  # Set grid size
  rows = 10
  cols = 10

  # Initialize grid with random cells
  grid = [[random.randint(DEAD, ALIVE) for _ in range(cols)] for _ in range(rows)]
  print(grid)
  # Print the initial generation
  print("Generation 0")
  print_grid(grid)

  # Run the simulation for a number of generations
  for i in range(1, 2):
    grid = update_grid(grid)
    print(f"Generation {i}")
    print_grid(grid)

if __name__ == "__main__":
  main()