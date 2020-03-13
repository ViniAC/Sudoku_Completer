
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
            for item in range(self.num_rows):
                array.append(0)
            self.grid.append(array)
            array = []
        self.generate_squares()

    def generate_squares(self):
        aux = self.size/9
        aux_width = 0
        aux_height = 0
        aux2_width = 100
        aux2_height = 100
        #width row
        for item2 in range(9):
            for item in range(9):
                square = Square(int(aux_width), int(aux_height), int(aux2_width), int(aux2_height),aux)
                self.square_list.append(square)
                aux_width += 100
                aux2_width += 100
            aux_width = 0
            aux2_height = aux * (item2+2)
            aux2_width = 100
            aux_height = aux*(item2+1)

    def possible(self,y,x,n):
        for i in range(0,9) :
            if self.grid[y][i] == n:
                return False
        for ia in range(0, 9) :
            if self.grid[ia][x] == n :
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for ib in range(0, 3) :
            for j in range(0, 3) :
                if self.grid[y0+1][x0+j] == n :
                    return False
        return True

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for n in range(1,10):
                        if self.possible(y,x,n) :
                            self.grid[y][x] = n
                            self.solve()
                            self.grid[y][x] = 0
                    return

       
class Square():
    def __init__(self,s_width ,s_height ,f_width ,f_height,size):
        self.s_width = s_width
        self.s_height = s_height
        self.f_width = f_width
        self.f_height = f_height
        self.rect = None
        self.size = size