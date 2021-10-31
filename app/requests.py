import urllib.request,json
from .models import Category, NewsSource,NewsArticle 
from datetime import date

api_key = None

base_url = None

articles_url = None