# Scraping, Sentimental Analysis and Linguistic analytics of news

***

## Scraping the news and performing sentimental analysis and Linguistic Analytics of that news
It is a project made to scrape the 'BBC news' website and give the sentiment analysis and Linguistic Analytics like:

* Positive Score
* Negative Score
* Polarity Score
* Subjective Score
* Average Sentence Length
* Percentage of Complex Words
* Fog Index
* Average Number of Words per Sentence
* Complex Word Count
* Word Count
* Syllable Count
* Pronoun Count
* Average Word Length

***

## Definitions:

#### Sentiment Analysis:
Determining if a piece of writing is favorable, negative, or neutral is known as sentiment analysis. The algorithm shown below is intended for usage in financial texts. There are several steps involved:

1. **Cleaning using Stop Words Lists**: The Stop Words Lists, which are located in the StopWords folder, are used to filter out words from the Stop Words List in order to clean up the text in preparation for sentiment analysis. 

2. **Creating a dictionary of Positive and Negative words**: To create a dictionary containing both positive and negative words, we utilize the Master Dictionary (included in the MasterDictionary folder). If a word is not included in the Stop Words Lists, we only add it to the dictionary.

3. **Extracting Derived variables**: With the help of the nltk tokenize package, we turn the text into a list of tokens, which we then utilize to compute the four variables listed below:
      + **Positive Score**: Each word that is found in the Positive Dictionary is given a value of +1, and the total of all the values is then used to determine the score.
      + **Negative Score**: To determine this score, each word that appears in the Negative Dictionary is given a value of -1. The values are then added together. To make the score a positive number, we multiply it by -1.
      + **Polarity Score**: This score indicates whether a particular text is good or negative. The following formula is used to compute it:
         - *Polarity Score* = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
Range is from -1 to +1
      + **Subjectivity Score**: This score establishes the objectivity or subjectivity of a particular text. The following formula is used to compute it: 
          - *Subjectivity Score* = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
Range is from 0 to +1

4. **Analysis of Readability**: The following formula for the Gunning Fox index is used to calculate the analysis of readability:
      + **Average Sentence Length** = the number of words / the number of sentences
      + **Percentage of Complex words** = the number of complex words / the number of words 
      + **Fog Index** = 0.4 * (Average Sentence Length + Percentage of Complex words)

5. **Average Number of Words Per Sentence**: 
      + **Average Number of Words Per Sentence** = the total number of words / the total number of sentences

6. **Complex Word Count**: Complex words are words in the text that contain more than two syllables.

7. **Word Count**: We count the total cleaned words present in the text by 
      + removing the stop words (using stopwords class of nltk package).
      + removing any punctuations like ? ! , . from the word before counting.

8. **Syllable Count Per Word**: By counting the vowels that are present in each word, we may determine how many syllables there are in each word in the text. Additionally, we do not count words that end in "es" or "ed" as syllables in order to handle certain instances.

9. **Personal Pronouns**: We utilize regular expressions to determine the counts of the words "I," "we," "my," "ours," and "us" in order to compute the Personal Pronouns stated in the text. Extra care is made to ensure that the country US is not on the list.

10. **Average Word Length**: 
Average Word Length is calculated by the formula:
      + Sum of the total number of characters in each word/Total number of words

## User Instructions:

1. Clone the project 
```
git clone https://github.com/aashaybelekar/scraping_and_linguistic_analytics.git
```
2. Install dependencies 
```
pip intall -r requirements.txt
```
3. Replace the list of BBC news list url with your own if required. make sure the file name is `Input.xlsx` 

4. Run the program 
```
python app.py
```
5. Output will be stored in location `.\artifacts\output.xlsx`

## Developer Instruction:

* web scraping code is present in `.\src\components\data_ingestion.py`
* it is required that the function `initiate_dataingestion` either return `None` or `str` object.