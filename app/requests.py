import urllib.request,json
from .models import Category, NewsSource,NewsArticle 
from datetime import date

api_key = None

base_url = None

articles_url = None

def configure_request(app):
        global api_key,base_url,articles_url
        api_key = app.config['NEWS_API_KEY']  
        base_url = app.config['SOURCE_BASE_URL']
        articles_url = app.config['ARTICLE_BASE_URL']