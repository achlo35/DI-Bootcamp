import time
import copy
import os

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        # Initialize grid with all dead cells
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        if initial_state:
            for r, c in initial_state:
                if 0 <= r < rows and 0 <= c < cols:
                    self.grid[r][c] = 1

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.grid:
            print(' '.join(['■' if cell else ' ' for cell in row]))
        print()

    def count_live_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]
        return count

    def next_generation(self):
        new_grid = copy.deepcopy(self.grid)
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_live_neighbors(r, c)
                if self.grid[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[r][c] = 0
                    elif live_neighbors in [2, 3]:
                        new_grid[r][c] = 1
                else:
                    if live_neighbors == 3:
                        new_grid[r][c] = 1
        self.grid = new_grid

    def is_stable(self, prev_grid):
        return self.grid == prev_grid

    def run(self, generations=50, delay=0.5):
        prev_grid = None
        for gen in range(generations):
            self.display()
            if prev_grid is not None and self.is_stable(prev_grid):
                print("Game ended: Stable state reached.")
                break
            prev_grid = copy.deepcopy(self.grid)
            self.next_generation()
            time.sleep(delay)

if __name__ == "__main__":
    # Example initial states:
    # Blinker (oscillator)
    blinker = [(1,2), (2,2), (3,2)]
    # Glider
    glider = [(1,2), (2,3), (3,1), (3,2), (3,3)]
    # Block (still life)
    block = [(1,1), (1,2), (2,1), (2,2)]

    print("Blinker pattern:")
    game = GameOfLife(5, 5, blinker)
    game.run(generations=10, delay=0.5)

    print("Glider pattern:")
    game = GameOfLife(10, 10, glider)
    game.run(generations=20, delay=0.2)

    print("Block pattern:")
    game = GameOfLife(5, 5, block)
    game.run(generations=10, delay=0.5)