class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f"Скорость автомобиля {self.name} = {self.speed}"

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn(self, direction):
        return f"Машина {self.name} поворачивает на {direction}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Превышении скорости на {self.speed - 60}"
        else:
            return "Едем дальше"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Превышении скорости на {self.speed - 40}"
        else:
            return "Едем дальше"

    def __str__(self):
        return f"Name: {self.name}, Speed: {self.speed}, Color: {self.color}, IsPolice: {self.is_police}"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


auto_1 = Car(120, "black", "bmw", False)
auto_2 = TownCar(100, "blue", "toyota", False)
auto_3 = SportCar(320, "red", "ferrari", False)
auto_4 = WorkCar(90, "white", "lada", False)
auto_5 = PoliceCar(200, "military", "pol_car", True)

print(auto_1.speed, auto_1.name)
print(auto_2.show_speed())
print(auto_3.name, auto_3.is_police)
print(auto_4.name, auto_4.speed)
print(auto_4.show_speed())
print(auto_5.name)

print(auto_4)

print(auto_5.go())
print(auto_5.stop())
print(auto_5.turn("лево"))
