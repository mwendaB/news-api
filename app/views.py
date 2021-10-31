from flask import render_template
from app import app

# Views
@app.route('/news/<news_id>')
def news(news_id):

    
    return render_template('news.html',id = news_id)

def index():

    title = 'Top of the story'
    return render_template('index.html', title = title)