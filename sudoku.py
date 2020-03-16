
class Sudoku():

    def __init__(self, size):
        self.num_rows = 9
        self.grid = []
        self.square_list = []
        self.size = size
        self.generate_grid()

    def generate_grid(self):
        array = []
        for item in range(self.num_rows):
            self.grid.append(array)
            array = []
        self.generate_squares()

    def generate_squares(self):
        aux = self.size/9
        aux_width = 0
        aux_height = 0
        aux2_width = aux
        aux2_height = aux
        #width row
        count = 1
        for item2 in range(9):
            for item in range(9):
                square = Square(int(aux_width), int(aux_height), int(aux2_width), int(aux2_height),aux)
                square.num_x = aux_width+(aux/2)
                square.num_y = aux_height+(aux/2)
                self.grid[item2].append(square)
                self.square_list.append(square)
                aux_width += aux
                aux2_width += aux
            aux_width = 0
            aux2_height = aux * (item2+2)
            aux2_width = aux
            aux_height = aux*(item2+1)

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.valid(i, (row, col)):
                self.grid[row][col].num = i
                if self.solve():
                    return True
                self.grid[row][col].num = 0

        return False

    def valid(self, num, pos):
        # Check row
        for i in range(len(self.grid[0])):
            if self.grid[pos[0]][i].num == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(self.grid)):
            if self.grid[i][pos[1]].num == num and pos[0] != i:
                return False

    # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.grid[i][j].num == num and (i,j) != pos:
                    return False

        return True
    
    def find_empty(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].num == 0:
                    return (i, j)  # row, col
        return None

       
class Square():
    num = 0
    def __init__(self,s_width ,s_height ,f_width ,f_height,size,num=0):
        self.s_width = s_width
        self.s_height = s_height
        self.f_width = f_width
        self.f_height = f_height
        self.rect = None
        self.size = size
        self.num = num
        self.num_x = None
        self.num_y = None