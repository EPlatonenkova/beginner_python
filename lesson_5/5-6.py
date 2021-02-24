dict = {}

with open("file_6.txt", encoding='utf-8') as file:
    for line in file.readlines():
        val = line.split()
        name = val[0]
        sbj_row = val[1:] # 100(л) 50(пр) 20(лаб).
        count_sbj = 0
        for items in sbj_row:
           new_line =items.strip("(л)").strip("(пр)").strip("(лаб)")
           count_sbj += int(new_line)
        dict[name] = count_sbj

print(dict)


