
import math
from decimal import Decimal, ROUND_HALF_UP

def amount_of_study(total_pages, periods, effort_of_pages):
    if periods is None and effort_of_pages is not None:
        if total_pages == 0 or effort_of_pages <= 0:
            return None
        total_study = {}
        if total_pages > effort_of_pages:
            total_period = 60 + math.ceil(total_pages / effort_of_pages)
            total_study["total period"] = total_period
        else:
            total_period = 60
            total_study["total period"] = total_period

        def number_of_dates(numberofdates):
            remained = total_period - (numberofdates - 1)
            total_study["remained"] = remained
            if 1 <= numberofdates <= 2:
                first_study = str((((numberofdates - 1) * effort_of_pages) + 1)) + '~' + str(
                    min(numberofdates * effort_of_pages, total_pages))
                total_study["round 1"] = first_study
            if 3 <= numberofdates <= 14:
                first_study = str((((numberofdates - 1) * effort_of_pages) + 1)) + '~' + str(
                    min(numberofdates * effort_of_pages, total_pages))
                second_study = str(((((numberofdates - 2) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 2) * effort_of_pages, total_pages))
                total_study["round 1"] = first_study
                total_study["round 2"] = second_study
            if 15 <= numberofdates <= 60:
                first_study = str((((numberofdates - 1) * effort_of_pages) + 1)) + '~' + str(
                    min(numberofdates * effort_of_pages, total_pages))
                second_study = str(((((numberofdates - 2) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 2) * effort_of_pages, total_pages))
                third_study = str(((((numberofdates - 14) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 14) * effort_of_pages, total_pages))
                total_study["round 1"] = first_study
                total_study["round 2"] = second_study
                total_study["round 3"] = third_study
            if 61 <= numberofdates:
                first_study = str((((numberofdates - 1) * effort_of_pages) + 1)) + '~' + str(
                    min(numberofdates * effort_of_pages, total_pages))
                second_study = str(((((numberofdates - 2) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 2) * effort_of_pages, total_pages))
                third_study = str(((((numberofdates - 14) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 14) * effort_of_pages, total_pages))
                fourth_study = str(((((numberofdates - 60) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 60) * effort_of_pages, total_pages))
                total_study["round 1"] = first_study
                total_study["round 2"] = second_study
                total_study["round 3"] = third_study
                total_study["round 4"] = fourth_study

            return total_study
        return number_of_dates

    elif periods is not None and effort_of_pages is None:
        if total_pages == 0 or periods == 0:
            return None

        def number_of_dates(numberofdates):
            if numberofdates > periods:
                return None
            total_study = {}
            if total_pages > periods:
                pages_for_study = total_pages / periods
                effort_of_pages = Decimal(pages_for_study).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
                total_study["effort_of_pages"] = int(effort_of_pages)
            else:
                effort_of_pages = 1

            if 1 <= numberofdates <= 2:
                first_study = str((((numberofdates - 1) * effort_of_pages) + 1)) + '~' + str(
                    min(numberofdates * effort_of_pages, total_pages))
                total_study["round 1"] = first_study
            if 3 <= numberofdates <= 14:
                first_study = str((((numberofdates - 1) * effort_of_pages) + 1)) + '~' + str(
                    min(numberofdates * effort_of_pages, total_pages))
                second_study = str(((((numberofdates - 2) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 2) * effort_of_pages, total_pages))
                total_study["round 1"] = first_study
                total_study["round 2"] = second_study
            if 15 <= numberofdates <= 60:
                first_study = str((((numberofdates - 1) * effort_of_pages) + 1)) + '~' + str(
                    min(numberofdates * effort_of_pages, total_pages))
                second_study = str(((((numberofdates - 2) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 2) * effort_of_pages, total_pages))
                third_study = str(((((numberofdates - 14) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 14) * effort_of_pages, total_pages))
                total_study["round 1"] = first_study
                total_study["round 2"] = second_study
                total_study["round 3"] = third_study
            if 61 <= numberofdates:
                first_study = str((((numberofdates - 1) * effort_of_pages) + 1)) + '~' + str(
                    min(numberofdates * effort_of_pages, total_pages))
                second_study = str(((((numberofdates - 2) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 2) * effort_of_pages, total_pages))
                third_study = str(((((numberofdates - 14) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 14) * effort_of_pages, total_pages))
                fourth_study = str(((((numberofdates - 60) - 1) * effort_of_pages) + 1)) + '~' + str(
                    min((numberofdates - 60) * effort_of_pages, total_pages))
                total_study["round 1"] = first_study
                total_study["round 2"] = second_study
                total_study["round 3"] = third_study
                total_study["round 4"] = fourth_study

            return total_study
        return number_of_dates

    elif periods is not None and effort_of_pages is not None:
        return None
    elif periods is None and effort_of_pages is None:
        return None


# 学習したい本のトータルページ数と、その本を終わらせたい日数を入力する。
# 1日に勉強するページ数はNoneとして、指定しない。
study1 = amount_of_study(450,84, None)
# 勉強開始から何日目か(あるいは何回目の勉強か)を入力すると、
# その日にどのページを学習していけばいいかが出力される。
print(study1(17))

# 学習したい本のトータルページ数と、1日に勉強可能なページ数を入力する。
# どれくらいの期間・日数で勉強を終わらせたいかはNoneとして、指定しない。
study1 = amount_of_study(450, None, 4)
# 勉強開始から何日目か(あるいは何回目の勉強か)を入力すると、全体でその本を完読する日数と残りの日数が表示され、
# またその日にどのページを学習していけばいいかが出力される。
print(study1(18))