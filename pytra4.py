### データベースに関数を適応した場合

import datetime


# 一番最初のデータベース：空のリスト、Blogクラスからインスタンスが生成されるたびにdata_setsに追加されていく。updateメソッドが行われるたびにもdata_setsが更新されていく。
data_sets = []


# Blogクラスから新しくインスタンスが生成されるたびにdata_setsにそのインスタンス=ブログの情報をdata_setsに追加する関数
def Data_set_append(data_set):
    data_sets.append(data_set)

# updateメソッドが呼び出されるたびに、data_setsの情報を書き換える関数。
def Data_set_change(data_set):
    for data in data_sets:
        if data['id'] == data_set['id']:
            for key_of_data_set in data.keys():
                data[key_of_data_set] = data_set[key_of_data_set]


# Blogクラス
class Blog():

    __counter = 0

    def __init__(self, title, body, genres):
        self.title = title
        self.body = body
        self.genres = genres
        Blog.__counter += 1
        self.id = Blog.__counter
        self.created_at = str(datetime.date.today())
        self.updated_at = None
        self.data_set = {
            'title':self.title,
            'body': self.body,
            'genres':self.genres,
            'created_at':self.created_at,
            'updated_at':self.updated_at,
            'id':self.id}
        Data_set_append(self.data_set)

    
    def update(self, title, body, genres):
        if title is None:
            pass
        elif title is not None:
            self.title = title
        if body is None:
            pass
        elif body is not None:
            self.body = body
        if  genres is None:
            pass
        elif genres is not None:
            self.genres = genres
        self.updated_at = str(datetime.date.today())
        self.data_set = {
            'title':self.title,
            'body': self.body,
            'genres':self.genres,
            'created_at':self.created_at,
            'updated_at':self.updated_at,
            'id':self.id}
        Data_set_change(self.data_set)



# 3つのブログを作成
blog_1 = Blog('how to write good code', 'who knows',['tech','python','web dev'])
blog_2 = Blog('how to be rich', 'He knows',['finance','investment','economics'])
blog_3 = Blog('how to be happy', 'my mom knows',['self-compassion','confidence','philosophy'])

#　ブログのタイトルを見る
print(blog_1.title)

#　3つのブログが作成された時点でのデータベースのデータを見る
print(data_sets)


# ブログ2のタイトルを修正
blog_2.update('how to be smart', None, None)

#　修正後のデーターベースのデータ全体を見る
print(data_sets)


