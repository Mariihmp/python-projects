import requests
import datetime
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = 'LPGWUISAG8GIVO8O'
TWILIO_SID = ''#duo to security issues it's deleted 
TWILIO_AUTH = '' #duo to security issues it's deleted 
news_api_key = '75ad6a15a08a4c17b299593e93d975f2'

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily



stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT,params=stock_params)
response.raise_for_status()
api_data =response.json()
# [new_value for (key, value) in dictionary.items()]
yesterday_date = datetime.datetime.today() - datetime.timedelta(days=1)
yesterday = str(yesterday_date.date())
yesterday_closing_price =api_data['Time Series (Daily)'][yesterday]['4. close']

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday = (datetime.datetime.today()-datetime.timedelta(days=2)).date()
day_before_str = str(day_before_yesterday)
day_bef_yest_closing_price = api_data['Time Series (Daily)'][day_before_str]['4. close']

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difer = abs(float(yesterday_closing_price) - float(day_bef_yest_closing_price))
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
differ_percentage = (positive_difer/float(yesterday_closing_price))*100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
newsapi_endpoint ="https://newsapi.org/v2/everything"

newsapi_params = {
    'apikey':news_api_key,
    'qInTitle':COMPANY_NAME
}
if differ_percentage >1:
    news_req = requests.get(newsapi_endpoint,params=newsapi_params)
    news_req.raise_for_status()
    articles = news_req.json()['articles']
#getting the first three articles related to the companny
    first_three_articles = articles[:3]
    print(first_three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

    formatted_article = [f"Headline:{article['title']}\nBreif:{article['description']}" for article in \
        first_three_articles]
    client = Client(TWILIO_SID,TWILIO_AUTH)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_='+12052094963',#the number for your trial twilio account 
            to='' #+98 followed by the number  for Iran , for security issues it's deleted
        )



