class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asf_massa(self, weight, count):
        self.weight = 30
        self.count = 2
        asf_massa = self._length * self._width * self.weight * self.count / 1000
        print(round(asf_massa))


mass = Road(50, 5000)
mass.asf_massa(30, 2)
