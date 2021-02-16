import json

dict = {}
ave_dict = {}

with open('firms_7.txt.', "r") as f:
    for row in f.readlines():
        data = row.split()
        name = data[0]
        profits = data[2]
        costs = data[3]
        firm_costs = int(profits) - int(costs)
        dict[name] = firm_costs

    print(dict)

    count = 0
    sum = 0


    for key in dict:
        count += 1
        sum += dict[key]
        ave_sum = sum/count
    ave_dict["average_profit"] = ave_sum
    print(ave_dict)

    with open('7_task_result.json', "w") as write:
        json.dump(dict, write)
        json.dump(ave_dict, write)








