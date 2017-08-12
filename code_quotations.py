import requests
import json
from collections import OrderedDict
import urllib.request as request
from xml.etree import ElementTree



"""
Documentation: http://www.quotes.net/quotes_api.php
"""




def get_quotes(q):
    #authentication
    params_gd = OrderedDict({
        "uid": "5434",
        "tokenid": "yGPd1otwYxejzgsw",
        #programmatically look up IP address
        #"userip": json.loads(request.urlopen("http://ip.jsontest.com/").read().decode('utf-8'))['ip'],
        #"userip": "userip=2001:569:bddb:4900:79d4:a3b8:f459:b37d",
        "searchtype": "SEARCH",
        "query": q
    })
    #URL
    basepath_gd = "http://www.stands4.com/services/v2/quotes.php"

    #request the API
    data = requests.get(basepath_gd,
                           params=params_gd
                           #headers={
                            #   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"
                           #}
                           )


    #request = requests.get(url + "?" + version + "&" + format + "&" + t_p + "&" + t_k + "&" + 
    #	action + "&" + q + "&" + user_ip + "&" + useragent)
    
    #request = (url + "?" + version + "&" + format + "&" + t_p + "&" + t_k + "&" + 
    #	action + "&" + q + "&" + user_ip + "&" + useragent)
    #data =json.get(request)
   
    return data

