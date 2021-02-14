# season = int(input("Введите числовое значения месяца: "))
my_dict_seasons = {"winter": [12, 1, 2],
                   "spring": [3, 4, 5],
                   "summer": [6, 7, 8],
                   "autumn": [9, 10, 11]
                   }
season = int(input("Введите числовое значения месяца: "))


flag = False
for key in my_dict_seasons:
    if flag:
        break
    for m in my_dict_seasons[key]:
        if flag:
            break
        if m == season:
            print(key)
            flag = True
