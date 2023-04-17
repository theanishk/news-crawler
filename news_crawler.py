import streamlit as st
import requests as re
import datetime
import goose3

g = goose3.Goose()

def crawler(stock_name, day_filter):
    api_key = "d18ded80e33c4c67a0fbfeda363679ea"

    today = datetime.date.today()
    day = today - datetime.timedelta(days=1)
    week = today - datetime.timedelta(days=7)
    month = today - datetime.timedelta(days=30)

    if (day_filter == 'Day'):
        date = day

    elif (day_filter == 'Week'):
        date = week
    
    elif (day_filter == 'Month'):
        date = month

    else:
        pass;

    try:
        news = re.get(f'https://newsapi.org/v2/everything?q={stock_name}&apiKey={api_key}&language=en&sortBy=publishedAt&pageSize=100&from={date}').json()
        return news
    
    except:
        return None


stock_name = st.text_input("Stock's name ")
news_day_filter = st.selectbox('Select news day range ', ['--Select--', 'Day', 'Week', 'Month'])

news = crawler(stock_name, news_day_filter)
if(news):
    for article in news['articles']:
        st.header(article['title'])
        st.subheader(article['author'])
        st.write(article['content'])
        st.write(article['url'])
        st.write("--------------------")