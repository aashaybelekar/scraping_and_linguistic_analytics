import re
import os
import sys
import pandas as pd

from nltk.corpus import stopwords

from src.exception import CustomException
from src.logger import logging



def remove_stopwords(text):
    try:
        stop_words = pd.read_csv(os.path.join('artifacts','stopwords.csv'))
        word_tokens = text.split()
        filtered_text_1 = [word for word in word_tokens if word not in stop_words]
        filtered_text_2 = []
        for word in filtered_text_1:
            if word != 'US' and word.lower() not in stop_words:
                filtered_text_2.append(word)

        logging.info("removed the custome stopwords")
        return ' '.join(filtered_text_2)
    except Exception as e:
       raise CustomException(e, sys)

def text_to_word_list(text):
    try:
        sentences = text.replace("\n", "").replace("\xa0","").split(".")
        words = [words.replace("\n", "").replace("\xa0","").split(" ") for words in sentences]
        words = [[word for word in lists if word != '']for lists in words ]

        logging.info("converted the text to a list")
        return sentences, words
    except Exception as e:
       raise CustomException(e, sys)

def complex_syllable_words(sentence):
    try:
        syllable = []
        complex_word = 0
        letters = 0
        syllable_count = 0
        vowels = "aeiou"
        for words in sentence:
            for word in words:
                if not(word.endswith('es') or word.endswith('ed')):
                    syllable_count += 1
                for letter in word:
                    letters += 1
                    if letter in vowels:
                        syllable.append(letter)
                if len(set(syllable))>=2:
                    complex_word+=1
                    syllable = []

        logging.info("counted the complex words, syllables and letters.")
        return (complex_word,syllable_count,letters)
    except Exception as e:
        raise CustomException(e, sys)

def word_count_function(text):
    try:
        stop_words = stopwords.words('english')
        word_token = text.split()
        filtered_text = []
        for word in word_token:
            if word not in stop_words:
                filtered_text.append(word)
        
        logging.info("counted the clean words (nltk stopwords used)")
        return len(filtered_text)
    except Exception as e:
        CustomException(e, sys)

def return_no_pronoun(text):
    try:
        pronoun_regex = re.compile(r"\b(I|we|my|ours|(?<!U)us)\b", re.IGNORECASE)
        matches = pronoun_regex.findall(text)

        logging.info("counted the number of pronoun")
        return len(matches)
    except Exception as e:
        CustomException(e, sys)

