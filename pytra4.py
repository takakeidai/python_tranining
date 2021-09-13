


import datetime


data_sets = [
    {'title': 'how to write good code', 
    'body': 'who knows', 
    'genres' : ['tech','python','web dev'],
    'created_at':'2019-07-03', 
    'updated_at':'2020-06-14',
    'id':1},
    {'title': 'how to be rich', 
    'body': 'He knows', 
    'genres' : ['finance','investment','economics'],
    'created_at':'2019-02-18', 
    'updated_at':'2020-01-20',
    'id':2},
    {'title': 'how to be happy', 
    'body': 'my mom knows all', 
    'genres' : ['self-compassion','confidence','philosophy'],
    'created_at':'2019-08-30', 
    'updated_at':'2020-11-06',
    'id':3}
    ]






class Blog():
    def __init__(self, title, body, genres, id):
        self.title = title
        self.body = body
        self.genrfes = genres
        self.created_at = str(datetime.date.today())
        self.updated_at = None
        self.id = id


    def update(self):
        id_list = [ data['id'] for data in data_sets]
        if self.id not in id_list:
            print('no data in data base')
        else:
            for data in data_sets:
                if data['id'] == self.id:
                    data['title'] = self.title
                    data['body'] = self.body
                    data['genres'] = self.genrfes
                    data['updated_at'] = str(datetime.date.today())
                else:
                    pass



# blog_1のタイトルだけかわったインスタンスを生成、idも1で同じもの
blog_1 = Blog('the best code ever','my friend knows', ['sports','tennis','racket'],1)


# blog_2で、全く新しいブログのインスタンスを生成、idは4
blog_2 = Blog('traveing in Japan', 'I know', ['travel', 'Japan', 'Japanese Food'],4)



# blog_1.update()をやってみる
blog_1.update()

# blog_2.updateをやってみる。blog_2はデータベース上にないため、上書きするものがなく no data in data beseとなるはず
blog_2.update()

# データベースが変わっているかみてみる。
print(data_sets)