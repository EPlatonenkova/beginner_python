def user_data(**kwargs):
    print(kwargs)


user_data(name=input("Введите ваше имя"),
          surname=input("Введите фамилию"),
          year=input("Введите год рождения"),
          city=input("Ваш город рождения"),
          email=input("Ваш емэйл"),
          tel=input("Номер вашего телефона"))
