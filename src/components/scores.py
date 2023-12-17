import os
import sys
import pandas as pd
from nltk.corpus import stopwords

from src.exception import CustomException
from src.logger import logging
from src.components.utils import (
    remove_stopwords,
    text_to_word_list,
    complex_syllable_words,
    word_count_function,
    return_no_pronoun
)


class BasicScore:
    def __init__(self, text):
        self.positive_list = pd.read_csv(os.path.join(os.path.abspath('.'),'artifacts','positivewords.csv'), header=None)[0].tolist()
        self.negative_list = pd.read_csv(os.path.join(os.path.abspath('.'),'artifacts','negativewords.csv'), header=None)[0].tolist()
        self.stopwords = pd.read_csv(os.path.join(os.path.abspath('.'),'artifacts','stopwords.csv'), header=None)[0].tolist()
        self.text = text

    def filtered_text(self):
        try:
            return remove_stopwords(self.text)
        except Exception as e:
            raise CustomException(e, sys)

    def positive_score(self):
        try:
            filtered_text = self.filtered_text()
            return sum([1 if word in self.positive_list else 0 for word in filtered_text.split()])
        except Exception as e:
            raise CustomException(e, sys)

    def negative_score(self):
        try:
            filtered_text = self.filtered_text()
            return sum([1 if word in self.negative_list else 0 for word in filtered_text.split()])
        except Exception as e:
            raise CustomException(e, sys)

class AdvancedScore:
    def __init__(self,text):
        self.positive_score = BasicScore(BasicScore(text).filtered_text()).positive_score()
        self.negative_score = BasicScore(BasicScore(text).filtered_text()).negative_score()
        self.filtered_text = BasicScore(BasicScore(text).filtered_text()).filtered_text()
        self.text = text
        self.sentences, self.words = text_to_word_list(self.text)
    
    def polarity_score(self):
        try:
            return ((self.positive_score - self.negative_score)/((self.positive_score + self.negative_score)+1**-6))
        except Exception as e:
            raise CustomException(e, sys)

    def subjective_score(self):
        try:
            return (self.positive_score + self.negative_score)/ ((len(self.filtered_text)+1**-6))
        except Exception as e:
            raise CustomException(e, sys)
    
    def average_sentence_length(self):
        try:
            return sum(len(self.words[i]) for i in range(len(self.sentences)))/len(self.sentences)
        except Exception as e:
            raise CustomException(e, sys)

    def percentage_complex_words(self): #prb
        try:
            complex_word_count,_,_ = complex_syllable_words(self.words)
            return (complex_word_count/sum(len(self.words[i]) for i in range(len(self.sentences))))
        except Exception as e:
            raise CustomException(e, sys)

    def fog_index(self):
        try:
            average_sentence_length = sum(len(self.words[i]) for i in range(len(self.sentences)))/len(self.sentences)
            percentage_complex_words = self.percentage_complex_words()
            return (0.4 * (average_sentence_length + percentage_complex_words))
        except Exception as e:
            raise CustomException(e, sys)
    
    def avg_number_of_words_per_sentence(self):
        try:
            return sum(len(self.words[i]) for i in range(len(self.sentences)))/len(self.sentences)
        except Exception as e:
            raise CustomException(e, sys)
    
    def complex_word_count(self): #prb
        try:
            complex_word_count,_,_ = complex_syllable_words(self.words)
            return complex_word_count
        except Exception as e:
            raise CustomException(e, sys)

    def word_count(self): #prb
        try:
            return word_count_function(self.text)
        except Exception as e:
            raise CustomException(e, sys)
    
    def syllable_count(self):
        try:
            _,syllable_count,_ = complex_syllable_words(self.words)
            return syllable_count
        except Exception as e:
            raise CustomException(e, sys)
    
    def pronoun_count(self):
        try:
            return return_no_pronoun(self.text)
        except Exception as e:
            raise CustomException(e, sys)
    
    def average_word_length(self):
        try:
            _,_,no_letters = complex_syllable_words(self.words)
            return no_letters/sum(len(self.words[i]) for i in range(len(self.sentences)))
        except Exception as e:
            raise CustomException(e, sys)