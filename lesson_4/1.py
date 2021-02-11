

from sys import argv
result, hours_work, per_hour, bonus = argv

print("Рабочие часы: ", hours_work)
print("Ставка в час: ", per_hour)
print("Премия: ", bonus)
print(f"Заработная плата сотрудника - {int(hours_work)*int(per_hour)+int(bonus)}")

