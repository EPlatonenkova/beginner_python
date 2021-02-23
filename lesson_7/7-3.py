class Cell:
    def __init__(self, count_cell):
        self.count_cell = count_cell


    def __add__(self, other):
        return self.count_cell + other.count_cell

    def __sub__(self, other):
        res = self.count_cell - other.count_cell
        if res > 0:
            return Cell(res)
        else:
            print("Error")

    def __mul__(self, other):
        res_1 = self.count_cell * other.count_cell
        return Cell(res_1)

    def __truediv__(self, other):
        res_3 = self.count_cell / other.count_cell
        return Cell(res_3)

    def make_order(self, row):
        count_1 = self.count_cell // row
        res_4 = self.count_cell % row
        total = "*" * row + "\n"
        return total * count_1 + "*" * res_4


    def __str__(self):
        return f"{self.count_cell}"

c_1 = Cell(100)
c_2 = Cell(20)
a = 10
print(c_1.make_order(a))



print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)


