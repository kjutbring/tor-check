#!/usr/bin/python2.7

from bs4 import BeautifulSoup
import requests

def get_page():

    url = "https://check.torproject.org/"

    # set to use socks proxy
    proxy_dict = {

        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    
    html = ""

    try:
        html = requests.get(url, proxies=proxy_dict)
    except:
        html = requests.get(url, proxies=None)

    return html

def scrape_page(page_html):
    
    result = ""

    soup = BeautifulSoup(page_html.text, 'html.parser')
    
    title = soup.title

    if "Congratulations" in str(title):
        result = 'yes ' + get_tor_ip(get_page())
    else: 
        result = 'nope'
    return result

def get_tor_ip(page_html):

    soup = BeautifulSoup(page_html.text, 'html.parser')
    tor_ip = soup.find('strong').getText()
    
    return tor_ip

if __name__ == "__main__":

    print scrape_page(get_page())
