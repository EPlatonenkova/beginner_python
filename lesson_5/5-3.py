f = open('file_3.txt', 'r+', encoding="utf-8")
# data = f.read()
# print(data)
# new = data.split()
# print(new)
dict = {}
for row in f.readlines():
    data = row.split()
    name = data[0]
    salary = float(data[1])
    dict[name] = salary
print(dict)



for key, val in dict.items():
    if val < 20000.00:
        print(key, val)

count_staff = len(dict)

staff_salary = round(sum(dict.values()),2)

med_salary = staff_salary/count_staff
print(f'Средняя зарплата на предприятии: {med_salary}')



f.close()
