import requests
from bs4 import BeautifulSoup
import json

# send request to baidu news to get newest news
def http_request(keywords):
    url = u"http://www.baidu.com/s?tn=news&rtt=4&wd=%s&pn=%d0" % (keywords, 1)
    data = requests.get(url)

    # decode html via bs4 and get news contents
    soup = BeautifulSoup(data.text, 'html.parser')
    news_items = soup.select('.result')

    return news_items


# extract title, time, source link from html
def extract_news(item):
    # source link location
    link = item.select('.c-title a')[0]['href']

    # source title location
    raw_title = item.select('.c-summary')[0].text

    # clean data
    raw_title = raw_title.replace('\n', ' ').lstrip().replace('\t', ' ')
    raw_title = ' '.join(raw_title.split())
    raw_title = raw_title.split()

    # whether it contains exact time
    if len(raw_title[2]) == 5:  # then it is a xx:xx like time
        news_source = raw_title[0]
        news_time = raw_title[1] + " " + raw_title[2]
        news_preview = ''.join(raw_title[3:-1])
    else:
        news_source = raw_title[0]
        news_time = raw_title[1]
        news_preview = ''.join(raw_title[3:-1])

    # put into json
    news_item = {'news_source': news_source, 'time': news_time, 'preview': news_preview, 'news_link': link}
    news_json = json.dumps(news_item, ensure_ascii=False)

    return news_json

# get one page of newest news
def construct_one_page_news(news_items):
    news_jsons = []
    for item in news_items:
        news_jsons.append(extract_news(item))

    return news_jsons

data = construct_one_page_news(http_request("香港"))



