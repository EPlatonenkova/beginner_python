money=int(input("Ваша выручка составила:"))
costs=int(input("Ваши издержки:"))
profit=money-costs
ren=profit/money
if money>costs:
    print('У вас есть прибыль!!!')
    print("Прибыль составила:",profit)
    print('Рентабельность:',ren)
else:
    print("Вы в минусе")

count_staff=int(input("Введите численность фирмы:"))
profit_staff=profit//count_staff
print("Прибыль фирмы на одного сотрудника составила:",profit_staff)
