
class NewsSource:
        '''
        News source class to define the newsSource object 
        '''
        def __init__(self,id,name,description,url):
                self.id = id
                self.name = name
                self.description = description
                self.url = url

class Category:
        '''
        Class that instantiates objects of the news categories objects of the news sources
        '''
        def __init__(self,author,description,time,url,image,title):
                self.author = author
                self.description = description
                self.time = time
                self.url = url
                self.image = image
                self.title = title  

class NewsArticle:
        '''
        News article class to define the newsArticle object 
        '''
        def __init__(self,author,description,time,url,image,title):
                self.id = id
                self.author = author
                self.description = description
                self.time = time
                self.url = url
                self.image = image
                self.title = title

