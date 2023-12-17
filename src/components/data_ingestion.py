import sys
import requests

from bs4 import BeautifulSoup
from src.exception import CustomException
from src.logger import logging



def initiate_dataingestion(url):
    try:
        logging.info("reading url")
        try:
            response = requests.get(url)
        except ConnectionError:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            tags = soup.find_all('div', {'data-component': 'text-block'})
            tag = [tag.get_text() for tag in tags]
            return ''.join(tag)
        except AttributeError:
            return None
        
    except Exception as e:
        raise CustomException(e, sys)
    

if __name__ == '__main__':
    print(initiate_dataingestion('https://www.bbc.com/news/world-middle-east-67740329'))