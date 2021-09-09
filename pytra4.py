
                        ### 問題4 ###


data_sources = [
    {'title': 'how to write good code', 
    'body': 'who knows', 
    'genres_1':'tech', 
    'genres_2':'python', 
    'genres_3':'web dev', 
    'created_at':'2019-12-07', 
    'updated_at':'2020-01-14'},
    {'title': 'how to be rich', 
    'body': 'He knows', 
    'genres_1':'finance', 
    'genres_2':'investment', 
    'genres_3':'economics', 
    'created_at':'2019-12-07', 
    'updated_at':'2020-01-14'},
    {'title': 'how to be happy', 
    'body': 'my mom knows all', 
    'genres_1':'self-compassion', 
    'genres_2':'confidence', 
    'genres_3':'philosophy', 
    'created_at':'2019-12-07', 
    'updated_at':'2020-01-14'},
    ]


class Multi_Data():

    def __init__(self, data_sources, order_of_data):
        self.order_of_data = order_of_data
        self.data_sources = data_sources
        self.data_source = self.data_sources[self.order_of_data]
        self.title = self.data_source['title']
        self.body = self.data_source['body']
        self.genres_1 = self.data_source['genres_1']
        self.genres_2 = self.data_source['genres_2']
        self.genres_3 = self.data_source['genres_3']
    
    def modify_title(self, title):
        self.title = title
        self.data_sources[self.order_of_data]['title'] = self.title

    def modify_body(self, body):
        self.body = body
        self.data_sources[self.order_of_data]['body'] = self.body

    def modify_genres_1(self, genres_1):
        self.genres_1 = genres_1
        self.data_sources[self.order_of_data]['genres_1'] = self.genres_1
    
    def modify_genres_2(self, genres_2):
        self.genres_2 = genres_2
        self.data_sources[self.order_of_data]['genres_2'] = self.genres_2

    def modify_genres_3(self, genres_3):
        self.genres_3 = genres_3
        self.data_sources[self.order_of_data]['genres_3'] = self.genres_3

    def show_data_sources(self):
        return self.data_sources

    

# dictリスト全体のdata_sourcesで、変更したいデータの番号を指定する。multi_data = Multi_Data(data_sources,1)は、data_sourcesの1番目のdict内{}のデータにアクセスできる。
# 応用を効かせれば、created_atの日付を指定して取り出したいデータを指定できそう。

multi_data = Multi_Data(data_sources,1)

# data_sourcesの1番目のdict内{}の各データ title, body, genres_1, genres_2, genres_3にアクセスできる。
print(multi_data.title)
print(multi_data.body)
print(multi_data.genres_1)
print(multi_data.genres_2)
print(multi_data.genres_3)


# genres_2に変更を加えるメソッド：'how to be rich'を'how to graduate prestigeous university'に変更

multi_data.modify_genres_2('how to graduate prestigeous university')
print(multi_data.genres_2)


# 変更後のdictリスト全体を返すメソッド：'how to be rich'を'how to graduate prestigeous university'に変更された後のdictリスト全体
print(multi_data.show_data_sources())


