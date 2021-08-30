

## 1つ目の方法
##関数を用いたお釣り計算

print("######### first try #########")

def calculate_change(total, money_paid):
    change = money_paid-total
    if change > 0:
        return "おつりは, " + "¥" + str(change) + "です。"
    elif change == 0:
        return "ちょうどいただきました。"
    else:
        return "¥" + str(abs(change)) + "だけお金が足りません。"

print(calculate_change(1340, 1500))
print(calculate_change(1500, 1500))
print(calculate_change(1800, 1500))

## 2つ目の方法
##関数を用いて、1つ1つの入力に対して返り値が辞書型で返ってくるようにした。

print("######### first try #########")

def calculate_change(total, money_paid):
    d = {}
    change = money_paid-total
    d["日本円"] = change
    return d

print(calculate_change(1340, 1500))
print(calculate_change(1500, 1500))
print(calculate_change(1800, 1500))

## 3つ目の方法
##クラス変数とクラスメソッドを用いて、それぞれのインスタンスがもつお釣りの値が
##リストとして返ってくるようにした。この方法の場合、各インスタンスのもつお釣りの値を
##まとめて扱うことができる。

print("######### second try #########")

class Allchange():
    all_changes = []
    @classmethod
    def change_append(cls, change):
            cls.all_changes.append(change)

class Change():
    def __init__(self, total, money_paid):
        self.total = total
        self.money_paid = money_paid
        self.currency = "日本円"
        change = self.money_paid - self.total
        Allchange.change_append(change)

    def change(self):
        self.change = self.money_paid - self.total
        if self.change > 0:
            return "お釣りは、 ¥"+str(self.change)
        elif self.change == 0:
            return "ちょうどいただきました。"
        else:
            return "¥"+str(abs(self.change))+"だけお金が足りません。"


change1= Change(1340,1500)
change2= Change(1500,1500)
change3= Change(1800,1500)
print(change1.change())
print(change2.change())
print(change3.change())
print(Allchange.all_changes)




## 4つ目の方法
##クラス変数とクラスメソッドを用いて、それぞれのインスタンスがもつお釣りの値が
##辞書型として返ってくるようにした。しかし、ひとまとめにお釣りを辞書型としてまとめられない。

print("######### third try #########")


class Allchange():
    all_changes = {}
    @classmethod
    def change_dictfromkeys(cls, currency, change):
            cls.all_changes[currency] = change

class Change():
    def __init__(self, total, money_paid):
        self.total = total
        self.money_paid = money_paid
        currency = "日本円"
        change = self.money_paid - self.total
        Allchange.change_dictfromkeys(currency, change)

    def change(self):
        self.change = self.money_paid - self.total
        if self.change > 0:
            return "お釣りは、 ¥"+str(self.change)
        elif self.change == 0:
            return "ちょうどいただきました。"
        else:
            return "¥"+str(abs(self.change))+"だけお金が足りません。"


change1= Change(1340,1500)
change2= Change(1500,1500)
change3= Change(1800,1500)
print(change1.change())
print(change2.change())
print(change3.change())

## この方法では、上の3つのインスタンス変数のもつchangeの値がall_changesに辞書型として反映されない。
##　最後のインスタンスのお釣りだけが辞書型として返ってきてします。どうするべきか。
print(Allchange.all_changes)
