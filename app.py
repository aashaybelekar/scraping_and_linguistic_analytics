import numpy as np
import pandas as pd

from tqdm import tqdm
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import initiate_dataingestion
from src.components.scores import BasicScore
from src.components.scores import AdvancedScore
from src.components.wordprocessor import WordProcessor



df = pd.read_excel('data\Input.xlsx')

df_positive_score = []
df_negative_score = []
df_polarity_score = []
df_subjectivity_score = []
df_avg_sentence_length = []
df_percentage_of_complex_words = []
df_fog_index = []
df_avg_number_of_words_per_sentence = []
df_complex_word_count = []
df_word_count = []
df_syllable_per_word = []
df_personal_pronouns = []
df_avg_word_length = []

list_of_lists = [df_positive_score, df_negative_score,
                df_polarity_score, df_subjectivity_score,
                df_avg_sentence_length, df_percentage_of_complex_words,
                df_fog_index, df_avg_number_of_words_per_sentence,
                df_complex_word_count, df_word_count,
                df_syllable_per_word, df_personal_pronouns,
                df_avg_word_length]



for url in tqdm(df.URL):
    text = initiate_dataingestion(url)
    temp = WordProcessor()
    temp.process_all_words()
    try:
        if text == None:
            for list in list_of_lists:
                list.append(np.nan)
        else:
            bscore = BasicScore(text)
            ascore = AdvancedScore(text)

            df_positive_score.append(bscore.positive_score())
            df_negative_score.append(bscore.negative_score())
            df_polarity_score.append(ascore.polarity_score())
            df_subjectivity_score.append(ascore.subjective_score())
            df_avg_sentence_length.append(ascore.average_sentence_length())
            df_percentage_of_complex_words.append(ascore.percentage_complex_words())
            df_fog_index.append(ascore.fog_index())
            df_avg_number_of_words_per_sentence.append(ascore.avg_number_of_words_per_sentence())
            df_complex_word_count.append(ascore.complex_word_count())
            df_word_count.append(ascore.word_count())
            df_syllable_per_word.append(ascore.syllable_count())
            df_personal_pronouns.append(ascore.pronoun_count())
            df_avg_word_length.append(ascore.average_word_length())

    except CustomException:
        for list in list_of_lists:
            list.append(np.nan)

df['POSITIVE SCORE'] = df_positive_score
df['NEGATIVE SCORE'] = df_negative_score
df['POLARITY SCORE'] = df_polarity_score
df['SUBJECTIVITY SCORE'] = df_subjectivity_score
df['AVG SENTENCE LENGTH'] = df_avg_sentence_length
df['PERCENTAGE OF COMPLEX WORDS'] = df_percentage_of_complex_words
df['FOG INDEX'] = df_fog_index
df['AVG NUMBER OF WORDS PER SENTENCE'] = df_avg_number_of_words_per_sentence
df['COMPLEX WORD COUNT'] = df_complex_word_count
df['WORD COUNT'] = df_word_count
df['SYLLABLE PER WORD'] = df_syllable_per_word
df['PERSONAL PRONOUNS'] = df_personal_pronouns
df['AVG WORD LENGTH'] = df_avg_word_length

df.to_excel('artifacts/output.xlsx', index=False)
logging.info("Execution completed successfully")