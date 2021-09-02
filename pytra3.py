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

food_orders4 = [{'name':'french fries','wait_time':5},
               {'name':'hamburger ','wait_time':8},
               {'name':'wine','wait_time':2},
               {'name':'orange juice','wait_time':4},
                {'name':'gyoza','wait_time':14},
                {'name':'poteto','wait_time':11},
                {'name':'pasta','wait_time':9},
                {'name':'pizza','wait_time':6},
                {'name':'salad','wait_time':7},
                {'name':'ramen','wait_time':7}]


def calculate_wait_time(orders):
    ## 同時に料理できる数をnumber_of_cookingに入れると、それに従った最短の料理時間が出てくる。
    number_of_cooking = 2
    list_wait_time = []
    for order in orders:
        list_wait_time.append(order['wait_time'])
        list_wait_time.sort(reverse=True)

    higher_numbers = [list_wait_time[i] for i in range(0, number_of_cooking)]

    for temporary_low_number in range(0, (len(list_wait_time) - number_of_cooking)):
        low_num = higher_numbers[number_of_cooking-1] + list_wait_time[number_of_cooking + temporary_low_number]
        higher_numbers.pop(number_of_cooking-1)
        higher_numbers.append(low_num)
        higher_numbers.sort(reverse=True)

    waiting_time = max(higher_numbers)

    return waiting_time

wait_time_1 = calculate_wait_time(food_orders1)
print(wait_time_1)

wait_time_2 = calculate_wait_time(food_orders2)
print(wait_time_2)

wait_time_3 = calculate_wait_time(food_orders3)
print(wait_time_3)

wait_time_4 = calculate_wait_time(food_orders4)
print(wait_time_4)




