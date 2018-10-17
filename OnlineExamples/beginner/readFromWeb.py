"""
Read and print all the headlines from new york times of today
"""

import requests
from bs4 import BeautifulSoup as bs

def read_and_display_headlines(url):
    response = requests.get(url)
    soup = bs(response.text, "html-parser")
    
    for 
    
read_and_display_headlines("https://www.nytimes.com/")