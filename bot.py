import tweepy
import sys
import requests
import json
import time


API_KEY = ""
SECRET_KEY =  ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

auth_handler = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=SECRET_KEY)
auth_handler.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth_handler, wait_on_rate_limit=True)


print('logged in succesfully')

while True:
    bitcoinprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    price = bitcoinprice.json()
    btcusd = price['bitcoin'] ['usd']
    print(btcusd)

    ethereumprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
    price = ethereumprice.json()
    ethusd = price['ethereum'] ['usd']
    print(ethusd)

    dogecoinprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd')
    price = dogecoinprice.json()
    dogeusd = price['dogecoin'] ['usd']
    print(dogeusd)

    message = 'Crypto prices:''\nBTC price is now ' + str(btcusd) + ' USD' '\nETH price is now ' + str(ethusd) + ' USD' ' \nDOGECOIN price is now ' + str(dogeusd) + ' USD'
    api.update_status(message)
    print('nice')
    time.sleep(3600)