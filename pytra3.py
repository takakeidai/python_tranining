####### 完成品

food_orders1 = [{'name':'french fries','wait_time':5},
               {'name':'hamburger ','wait_time':8},
               {'name':'salad','wait_time':2},
               {'name':'orange juice','wait_time':2}]

food_orders2 = [{'name':'french fries','wait_time':5},
               {'name':'hamburger ','wait_time':8},
               {'name':'salad','wait_time':2},
               {'name':'orange juice','wait_time':2},
                {'name':'ice cream','wait_time':2}]

food_orders3 = [{'name':'french fries','wait_time':5},
               {'name':'hamburger ','wait_time':8},
               {'name':'salad','wait_time':2},
               {'name':'orange juice','wait_time':4},
                {'name':'ice cream','wait_time':2}]


def calculate_wait_time(orders):
    list_wait_time = []
    for i in orders:
        list_wait_time.append(i['wait_time'])
        list_wait_time.sort(reverse=True)

    higher_num = list_wait_time[0]
    lower_num = list_wait_time[1]
    for i in range(2, len(list_wait_time)):
        sum = lower_num + list_wait_time[i]
        lower_num = min(higher_num, sum)
        higher_num = max(higher_num, sum)

    wait_time = higher_num
    return wait_time

w_1 = calculate_wait_time(food_orders1)
print(w_1)

w_2 = calculate_wait_time(food_orders2)
print(w_2)

w_3 = calculate_wait_time(food_orders3)
print(w_3)



