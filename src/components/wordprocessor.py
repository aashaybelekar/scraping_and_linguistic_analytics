import os
import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException

from dataclasses import dataclass

@dataclass
class stopwordsConfig:
    stop_words_path:str = os.path.join('artifacts', 'stopwords.csv')
    positive_words_path:str = os.path.join('artifacts', 'positivewords.csv')
    negative_words_path:str = os.path.join('artifacts', 'negativewords.csv')
    
    stopwords_txt_path:str = os.path.join('StopWords','StopWords')
    masterdictionary_path:str = 'MasterDictionary'

class WordProcessor:
    def __init__(self):
        self.stopwords_config = stopwordsConfig()

    def get_stopwords(self):
        try:
            folder_path = self.stopwords_config.stopwords_txt_path
            os.makedirs(os.path.dirname(self.stopwords_config.stop_words_path), exist_ok=True)

            content_list = []
            # Replace with the actual path to your fileRead the content of the text file into a list
            for filename in os.listdir(folder_path):
                if filename.endswith('.txt'):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, 'r', errors='replace') as file:
                        file_content = file.readlines()
                        content_list.extend(file_content)

            content_list = [line.replace("\n", "").strip() for line in content_list]
            content_list = [line.replace("|", "").strip() for line in content_list]
            content_list = [line.split(" ") for line in content_list]
            new_content_list = []

            for content in content_list:
                if type(content) == list:
                    for line in content:
                        if line == '':
                            pass
                        elif line.startswith('http'):
                            pass
                        else:
                            new_content_list.append(line.strip())
                else:
                    new_content_list.append(content)
            df_stopwords = pd.DataFrame(new_content_list)
            df_stopwords.to_csv(self.stopwords_config.stop_words_path, index=False, header=False)
            logging.info("created stopwords")
            return self.stopwords_config.stop_words_path
        
        except Exception as e:
            raise CustomException(e, sys)

    def get_positivewords(self):
        try:
            stop_words = pd.read_csv(self.stopwords_config.stop_words_path)
            file_path = os.path.join(self.stopwords_config.masterdictionary_path, 'positive-words.txt')
            positive_list = []
            
            with open(file_path, 'r', errors='replace') as file:
                file_content = file.readlines()
                positive_list.extend(file_content)

            positive_list = [a.replace("\n", "") for a in positive_list]
            positive_list = [word for word in positive_list if word not in stop_words]

            df_positive = pd.DataFrame(positive_list)
            df_positive.to_csv(self.stopwords_config.positive_words_path, index=False, header=False)
            logging.info("created positivewords")
            return self.stopwords_config.positive_words_path


        except Exception as e:
            raise CustomException(e, sys)

    def get_negativewords(self):
        try:
            stop_words = pd.read_csv(self.stopwords_config.stop_words_path)
            file_path = os.path.join(self.stopwords_config.masterdictionary_path, 'negative-words.txt')
            negative_list = []

            with open(file_path, 'r', errors='replace') as file:
                file_content = file.readlines()
                negative_list.extend(file_content)
            negative_list = [a.replace("\n", "") for a in negative_list]
            negative_list = [word for word in negative_list if word not in stop_words]

            df_negative = pd.DataFrame(negative_list)
            df_negative.to_csv(self.stopwords_config.negative_words_path, index=False, header=False)
            logging.info("created negativewords")
            return self.stopwords_config.negative_words_path
        except Exception as e:
            raise CustomException(e, sys)

    def process_all_words(self):
        self.get_stopwords()
        self.get_positivewords()
        self.get_negativewords()
        
