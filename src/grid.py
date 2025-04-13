from PIL import Image, ImageDraw
from src.cell import *

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell() for x in range(cols)] for y in range(rows)]
        
    def __getitem__(self, pos):
        x, y = pos
        return self.cells[y][x]
    
    def each_cell(self):
        for row in self.cells:
            for cell in row:
                yield cell

    def each_row(self):
        for row in self.cells:
            yield row

    def each_column(self):
        for col in range(self.cols):
            yield [self.cells[row][col] for row in range(self.rows)]

    def to_png(self, filename, cell_size=10, wall_width=2):
        img_width = cell_size * self._columns
        img_height = cell_size * self._rows

        background = 'white'
        wall = 'black'

        img = Image.new('RGB', (img_width+1, img_height+1), color=background)
        draw = ImageDraw.Draw(img)

        for mode in ['backgrounds', 'walls']:
            for cell in self.each_cell():
                x = cell._column * cell_size
                y = cell._row * cell_size

                self.to_png_without_inset(draw, cell, mode, cell_size, wall, x, y, wall_width)

        img.save(filename)
        
    def to_png_without_inset(self, draw, cell, mode, cell_size, wall, x, y, wall_width):
        x1, y1 = x, y
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        if mode == 'backgrounds':
            color = self.background_color_for(cell)
            if color is not None:
                draw.rectangle((x1, y1, x2, y2), fill=color)
        else:
            draw.line((x1, y1, x2, y1), fill=wall, width=wall_width)
            draw.line((x1, y1, x1, y2), fill=wall, width=wall_width)
            draw.line((x2, y1, x2, y2), fill=wall, width=wall_width)
            draw.line((x1, y2, x2, y2), fill=wall, width=wall_width)
    
    def background_color_for(self, cell):
        return None