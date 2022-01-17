# A class that represents one cell in a sudoku puzzle
class Cell():

    # init/constructor
    def __init__(self, value):
        self.value = value
        self.options = set()

    # determine the potential values based on the size of the region
    def set_options(self, region_size):
        if self.value == 0:
            self.options = {val for val in range(1, region_size + 1)}

# For testing purposes
# if __name__ == "__main__":
#     test = Cell(0)
#     print("Value:", test.value)
#     test.set_options(9)
#     print("Options:", test.options)
