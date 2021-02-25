class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        # protected
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"Полное имя сотрудника = {self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


w = Position("Толик", "Иванов", "дворник", "5000", "100")

print(w.name)
print(w.surname)
print(w.position)
print(w._income)

print(w.get_full_name())
print(w.get_total_income())

