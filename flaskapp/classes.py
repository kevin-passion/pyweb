# class화 하기 
class Nav:
    def __init__(self, title, url='#', children=[]):
        self.title = title
        self.url = url
        self.children = children
