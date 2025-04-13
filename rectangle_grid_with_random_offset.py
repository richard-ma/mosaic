import random

from src.cell import *
from src.grid import *


class RectangleGridWithRandomOffset(Grid):
    def __init__(self, rows, cols, max_offset_x=0, max_offset_y=0):
        super().__init__(rows, cols)
        self.max_offset_x = max_offset_x
        self.max_offset_y = max_offset_y

    def get_offset_x(self):
        return random.randint(1, self.max_offset_x)

    def get_offset_y(self):
        return random.randint(1, self.max_offset_y)

    def to_png_without_inset(self, draw, cell, mode, cell_size, wall, x, y, wall_width):
        x1, y1 = x, y
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        point1 = (x1 + self.get_offset_x(), y1 + self.get_offset_y())
        point2 = (x2 - self.get_offset_x(), y1 + self.get_offset_y())
        point3 = (x1 + self.get_offset_x(), y2 - self.get_offset_y())
        point4 = (x2 - self.get_offset_x(), y2 - self.get_offset_y())

        if mode == 'backgrounds':
            color = self.background_color_for(cell)
            if color is not None:
                draw.rectangle((x1, y1, x2, y2), fill=color)
        else:
            draw.line((*point1, *point2), fill=wall, width=wall_width)
            draw.line((*point1, *point3), fill=wall, width=wall_width)
            draw.line((*point2, *point4), fill=wall, width=wall_width)
            draw.line((*point3, *point4), fill=wall, width=wall_width)


if __name__ == "__main__":
    grid = RectangleGridWithRandomOffset(10, 10, max_offset_x=10, max_offset_y=10)
    grid.to_png("rectangle_grid_with_random_offset.png", cell_size=100, wall_width=2)