# def my_func(x, y): первый вариант
#     print(x**y)
#
#
# my_func(7, -2)
#



def my_func(x, y):
     a = x
     if y == -1:
         print(x*-1)
         return
     elif y ==1:
         print(x)
         return
     elif y == 0:
         print(1)
         return
     else:
         while y > 1:
            x = x * a
            y = y-1

         while y < -1:
            x = x * a * -1
            y = y+1
     print(x)


first = int(input("Введите число: "))
second = int(input("Введите число: "))

my_func(first, second)

