import tkinter as tk
import random

class PuzzleGame:
    def __init__(self, root, initial_state=None):
        self.root = root
        self.root.title("8-Puzzle Game")
        self.tiles = [[None] * 3 for _ in range(3)]
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.empty_row, self.empty_col = 2, 2
        self.create_tiles()
        self.create_input_field()
        if initial_state:
            self.set_initial_state(initial_state)
        else:
            self.shuffle()

    def create_tiles(self):
        for row in range(3):
            for col in range(3):
                value = self.goal[row][col]
                tile = tk.Button(self.root, text=str(value) if value else "", width=18, height=8, command=lambda row=row, col=col: self.tile_click(row, col))
                tile.grid(row=row, column=col)
                self.tiles[row][col] = tile

    def create_input_field(self):
        self.input_var = tk.StringVar()
        entry = tk.Entry(self.root, textvariable=self.input_var, width=20)
        entry.grid(row=3, column=0, columnspan=2)
        apply_button = tk.Button(self.root, text="Apply", command=self.apply_input_state)
        apply_button.grid(row=3, column=2)

    def shuffle(self):
        values = list(range(1, 9))
        random.shuffle(values)
        values.insert(8, 0)
        self.set_initial_state(values)

    def set_initial_state(self, state):
        state = state[:9]  # Ensure state has exactly 9 values
        for row in range(3):
            for col in range(3):
                value = state.pop(0)
                self.tiles[row][col].config(text=str(value) if value else "")
                self.goal[row][col] = value
                if value == 0:
                    self.empty_row, self.empty_col = row, col

    def apply_input_state(self):
        input_state = self.input_var.get()
        state_list = [int(x.strip()) for x in input_state]
        self.set_initial_state(state_list)

    def tile_click(self, row, col):
        if (abs(row - self.empty_row) + abs(col - self.empty_col) == 1):
            tile_text = self.tiles[row][col]['text']
            if tile_text != "":
                self.tiles[row][col].config(text="")
                self.tiles[self.empty_row][self.empty_col].config(text=tile_text)
                self.empty_row, self.empty_col = row, col

def main():
    root = tk.Tk()
    root.geometry("410x425")  # Set the window size to 400x400 pixels
    initial_state = [1, 2, 3, 4, 0, 5, 7, 8, 6]  # Example initial state (customize as needed)
    game = PuzzleGame(root, initial_state)
    root.mainloop()

if __name__ == "__main__":
    main()
