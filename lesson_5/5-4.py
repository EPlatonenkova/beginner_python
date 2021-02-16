
with open("eng.txt","r" ,encoding='utf-8') as file, open("ru_text.txt", "w" ,encoding='utf-8') as writer:
    for row in file:
        data = row.split("-")
        if int(data[1]) == 1:
            writer.writelines(f'Один - 1\n')
        elif int(data[1]) == 2:
            writer.writelines(f'Два - 2\n')
        elif int(data[1]) == 3:
            writer.writelines(f'Три - 3\n')
        elif int(data[1]) == 4:
            writer.writelines(f'Четыре - 4\n')
