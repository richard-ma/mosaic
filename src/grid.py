from src.cell import *

class Grid:
    def __init__(self, cell_width, cell_height, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(cell_width, cell_height) for x in range(cols)] for y in range(rows)]
        
    def getitem(self, row, col):
        return self.cells[row][col]
    
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