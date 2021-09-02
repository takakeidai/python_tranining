


import math
from decimal import Decimal, ROUND_HALF_UP

def get_pages_to_study(total_pages_of_book, total_days_to_study, num_of_pages_to_study_at_once):
    total_study = {}
    round = {'round1': 1, 'round2': 2, 'round3': 14, 'round4': 60}
    finalround = next(reversed(round), None)
    num_of_pages_to_study1 = total_pages_of_book / total_days_to_study
    num_of_pages_to_study_decimal = Decimal(num_of_pages_to_study1).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    total_study['number of pages to study'] = int(num_of_pages_to_study_decimal)

    if total_days_to_study != 0 and total_pages_of_book < total_days_to_study:
        num_of_pages_to_study = 1
        total_study['number of pages to study'] = num_of_pages_to_study

    elif num_of_pages_to_study_at_once != 0 and total_pages_of_book < num_of_pages_to_study_at_once:
        total_days = round[finalround]
        total_study['total days to finish'] = total_days



    def isDateswithin(num_of_dates):
        if 1 <= num_of_dates <= 2:
            return 1
        if 3 <= num_of_dates <= 14:
            return 2
        if 15 <= num_of_dates <= 60:
            return 3
        if 61 <= num_of_dates:
            return 4

    def mapping(index):
        if index == 1:
            return 1
        if index == 2:
            return 2
        if index == 3:
            return 14
        if index == 4:
            return 60

    def indicator_function(num_of_pages_to_study_at_once):
        if num_of_pages_to_study_at_once == 0:
            return num_of_pages_to_study_decimal
        else:
            return num_of_pages_to_study_at_once


    def get_total_study(num_of_dates):
        if total_pages_of_book <= 0 and total_days_to_study <= 0 and num_of_pages_to_study_at_once <= 0:
            return None

        elif total_pages_of_book == 0 or (total_days_to_study == 0 or num_of_pages_to_study_at_once != 0) and (
                total_days_to_study != 0 or num_of_pages_to_study_at_once == 0):
            return None

        if num_of_pages_to_study_at_once != 0 and total_days_to_study == 0 and total_pages_of_book > num_of_pages_to_study_at_once:
            total_days = round[finalround] + math.ceil(total_pages_of_book / num_of_pages_to_study_at_once)
            total_study['total days to finish'] = total_days
            remained = total_days - (num_of_dates - 1)
            total_study['remained days'] = remained


        for i in range(1, (isDateswithin(num_of_dates)) + 1):
            x = str((((num_of_dates - mapping(i)) * indicator_function(num_of_pages_to_study_at_once)) + 1)) + '~' + str(min(num_of_dates * indicator_function(num_of_pages_to_study_at_once), total_pages_of_book))
            total_study['round' + str(i)] = x



        return total_study


    return get_total_study


study_1 = get_pages_to_study(450, 84, 0)
print(study_1(3))

"""
study_2 = get_pages_to_study(450, 0, 0)
print(study_2(3))
"""

"""
study_3 = get_pages_to_study(450,0,4)
print(study_3(3))
"""

study_4 = get_pages_to_study(450,84,4)
print(study_4(3))

"""
study_5 = get_pages_to_study(0,0,4)
print(study_5(3))
"""

study_6 = get_pages_to_study(0,84,0)
print(study_6(3))

study_7 = get_pages_to_study(0,84,4)
print(study_7(3))

study_8 = get_pages_to_study(450, 500, 0)
print(study_8(3))

"""
study_9 = get_pages_to_study(450, 0, 900)
print(study_9(3))
"""



##########

i = 1
num_of_dates = 3
num_of_pages_to_study_decimal = 1
num_of_pages_to_study_at_once = 0
total_pages_of_book = 450
total_study = {}


def num_of_review(num_of_dates):
    if 1 <= num_of_dates <= 2:
        return 1
    if 3 <= num_of_dates <= 14:
        return 2
    if 15 <= num_of_dates <= 60:
        return 3
    if 61 <= num_of_dates:
        return 4


def mapping(index):
    if index == 1:
        return 1
    if index == 2:
        return 2
    if index == 3:
        return 14
    if index == 4:
        return 60


def indicator_function(num_of_pages_to_study_at_once):
    if num_of_pages_to_study_at_once == 0:
        return num_of_pages_to_study_decimal
    else:
        return num_of_pages_to_study_at_once

###  A :  num_of_pages_to_study_at_once == 0 or num_of_pages_to_study_decimal == 1 or num_of_pages_to_study == 1
if A:
    list_of_review = [0,2,14,60]
    for i in range(1, (num_of_review(num_of_dates))+1):
        x = str(num_of_dates-list[i])
        total_study['round' + str(i)] = x
else:
    for i in range(1, (isDateswithin(num_of_dates)) + 1):
        x = str((((num_of_dates - mapping(i)) * indicator_function(num_of_pages_to_study_at_once)) + 1)) + '~' + str(
            min(num_of_dates * indicator_function(num_of_pages_to_study_at_once), total_pages_of_book))
        total_study['round' + str(i)] = x

