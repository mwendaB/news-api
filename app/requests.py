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



def get_news_source(category):
	'''
	Function that gets the json response to our url request
	'''
	get_news_source_url = base_url.format(category,api_key)

	with urllib.request.urlopen(get_news_source_url) as url:
		get_news_source_data = url.read()
		get_news_source_response = json.loads(get_news_source_data)

		news_source_results = None

		if get_news_source_response['sources']:
			news_source_results_list = get_news_source_response['sources']
			news_source_results = process_news_source(news_source_results_list)

	return news_source_results



def process_news_source(news_source_list):
	'''
	Function that processes the news sources results and turns them into a list of objects
	Args:
		news_source_list: A list of dictionaries that contain sources details
	Returns:
		news_source_results: A list of sources objects
	'''
	news_source_results = []

	for news_source_item in news_source_list:
		id = news_source_item.get('id') 
		name = news_source_item.get('name')
		description = news_source_item.get('description')
		url = news_source_item.get('url')
		
		news_source_object = NewsSource(id,name,description,url,)
		news_source_results.append(news_source_object)

	return news_source_results

def get_articles(id):
	'''
	Function that processes the articles and returns a list of articles objects
	'''
	get_articles_url = articles_url.format(id,api_key)

	with urllib.request.urlopen(get_articles_url) as url:
		news_article_results = json.loads(url.read())


		news_article_object = None
		if news_article_results['articles']:
			news_article_object = process_news_source(news_article_results['articles'])

	return news_article_object

   
def get_news_source(category):
	'''
	Function that gets the json response to our url request
	'''
	get_news_source_url = base_url.format(category,api_key)

	with urllib.request.urlopen(get_news_source_url) as url:
		get_news_source_data = url.read()
		get_news_source_response = json.loads(get_news_source_data)

		news_source_results = None

		if get_news_source_response['sources']:
			news_source_results_list = get_news_source_response['sources']
			news_source_results = process_news_source(news_source_results_list)

	return news_source_results