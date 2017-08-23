#!/usr/bin/env python
import requests
import time

url = 'https://www.mygov.in'
waiting_period = 300

with requests.Session() as web_session:
    try:
        headers = {
                  "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"
}
        proxy_dict = {}

        page_response = web_session.get(url,headers=headers,proxies=proxy_dict,verify=False)
    except Exception,e:
         print ("An Error is encountered while getting web page %s" %e.message)
while 1:
        time.sleep(waiting_period)
        try:
            headers = {
                  "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"
}
            proxy_dict = {}

            page_response_after_wait = web_session.get(url,headers=headers,proxies=proxy_dict,verify=False)
        except Exception,e:
            print ("An Error is encountered while getting web page %s" %e.message)
        
        if page_response.content == page_response_after_wait.content:
            print " No Change is detected"
            page_response = page_response_after_wait
        else:
            print " Change is detected"

