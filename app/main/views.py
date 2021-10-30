from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news , get_article



@main.route('/', methods=['GET'])
def index():

    '''
    view news page function that returns the news details  and its data
    '''
    
    news = get_news()
    # print(news)
    title = "News"
    
    return render_template('index.html', news = news, title=title)





@main.route('/source/<id>')
def article(id):
    '''
    view news page function that returns the news details  and its data
    '''
    
    articles = get_article(id)
    title = "News"
    
    return render_template('article.html', articles = articles, title=title)