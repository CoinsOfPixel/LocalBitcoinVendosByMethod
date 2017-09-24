import json
import urllib2

url = 'https://localbitcoins.com/buy-bitcoins-online/USD/.json'
url2 = url

json_obj = urllib2.urlopen(url2)
offer = json.load(json_obj)

position = 0

size = len(offer['data']['ad_list'][position]['data']['profile'])


for i in range(size): 
    position += 1
    seller = offer['data']['ad_list'][position]['data']['profile']['username']
    offerID = offer['data']['ad_list'][position]['data']['ad_id']
    price = offer['data']['ad_list'][position]['data']['temp_price_usd']
    method = offer['data']['ad_list'][position]['data']['online_provider']
    if 'WU' in method: #Change the WU for the payment method you want. You can see the payment method in "online provider" on LCB
    #json:  https://localbitcoins.com/buy-bitcoins-online/US/united-states/.json
        print('Seller: %s - Offer ID: %s  - by the price: %s - for the method: %s' %(seller, offerID, price, method))

