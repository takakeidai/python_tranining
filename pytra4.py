


import datetime
import random

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


def generateUniqueId():
    id = random.random()
    for data in data_sets:
        if data['id'] == id:
            return generateUniqueId()
    return id


class Blog():
    def __init__(self, title, body, genres, id = None):
        self.title = title
        self.body = body
        self.genres = genres
        self.id = id

    

    def create_1(self):
        id = generateUniqueId()
        self.created_at = str(datetime.date.today())
        new_data = {
            'title': self.title, 
            'body': self.body,
            'genres' : self.genres,
            'created_at': self.created_at,
            'updated_at': None,
            'id':id
            }
        data_sets.append(new_data)
    

    def create_2(self):
        self.id = self.generateUniqueId()
        self.created_at = str(datetime.date.today())
        new_data = {
            'title': self.title, 
            'body': self.body,
            'genres' : self.genres,
            'created_at': self.created_at,
            'updated_at': None,
            'id':self.id
            }
        data_sets.append(new_data)
    

    def generateUniqueId(self):
        self.id = random.random()
        for data in data_sets:
            if data['id'] == id:
                return self.generateUniqueId()
        return self.id

        
    
    def delete(self):
        for data in data_sets:
            if data['id'] == self.id:
                data_sets.remove(data)


    def update(self):
        for data in data_sets:
            if data['id'] == self.id:
                 data['title'] = self.title
                 data['body'] = self.body
                 data['genres'] = self.genres
                 data['updated_at'] = str(datetime.date.today())
        

    @staticmethod
    def get_by_id(id):
        for data in data_sets:
            if data['id'] == id:
                return data

    

blog_1 = Blog('writing good codes', 'my friends know',['tech','python','web dev'],1)
blog_2 = Blog('traveing in Japan', 'I know', ['travel', 'Japan', 'Japanese Food'])

blog_1.update()
blog_2.create()

print(data_sets)

blog_1.delete()
blog_2.create()
print(data_sets)


