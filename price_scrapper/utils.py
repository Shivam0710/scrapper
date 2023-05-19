import requests
from bs4 import BeautifulSoup
import re

def get_price_of_product(product_link):
    if not product_link:
        return ""
    
    response = requests.get(product_link)
    html = BeautifulSoup(response.text, "html.parser")
    price_element_text = html.find('span', {"class": "clr6 fwb"}).get_text()
    return price_element_text