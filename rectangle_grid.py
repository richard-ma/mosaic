from src.cell import *
from src.grid import *


class RectangleGrid(Grid):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)


if __name__ == "__main__":
    grid = RectangleGrid(5, 5)
    grid.to_png("rectangle_grid.png", cell_size=20, wall_width=2)