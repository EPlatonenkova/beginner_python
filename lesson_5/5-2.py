f = open('file_two.txt', 'r+')
f.write('Homework\nFiles\nBeginner\nTask')
f.seek(0)

data = f.read()
print(data)
f.seek(0)
print(len(f.readlines()))
f.seek(0)


for i in f.readlines():
    print(len(i.strip()))




f.close()
