a=float(input())
b=float(input())
n=1
print(f'{n}-й день: {a}')

while a<b:
    n+=1
    a+=a*0.1
    print(f'{n}-й день: {a}')