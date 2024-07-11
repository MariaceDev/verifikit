from bs4 import BeautifulSoup
import requests
import spacy
from collections import Counter
from spacy.matcher import PhraseMatcher

# Load the spaCy model outside of functions to avoid reloading it every time a function is called
  # Load Spanish language model once

def extract_bold_words(url):
    """
    Extract bold words from a given URL using Beautiful Soup.
    """
    try:
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        bold_words = []
        for tag in soup.find_all(['b', 'strong']):
            bold_words.extend(tag.get_text().split())
        return bold_words
    except Exception as e:
        print(f"Error extracting bold words from URL: {e}")
        return []

def extract_web_text(url):
    """
    Extracts text from a given URL using Beautiful Soup.
    
    Parameters:
    - url (str): The URL to extract text from.
    
    Returns:
    str: The extracted text from the webpage.
    """
    try:
        response = requests.get(url, verify=False)  # Disable SSL verification for local testing
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except Exception as e:
        # Log the error instead of printing it
        print(f"Error extracting text from URL: {e}")
        return ""
    
nlp = spacy.load('es_core_news_sm')

def recognize_keywords(text, num_keywords=10):
   
    doc = nlp(text)

    #keywords counter
    keyword_counter = Counter()

    # Identify and add relevant named entities

    for ent in doc.ents:
        if ent.label_ in ['PER', 'ORG', 'LOC']:  # Filter SEO-relevant entities
            keyword_counter[ent.text.lower()] += 1

    # Count relevant nouns and adjectives

    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN', 'ADJ'] and not token.is_stop:
            keyword_counter[token.lemma_.lower()] += 1
    

    #Get the most frequent keywords

    keywords = [keyword for keyword, count in keyword_counter.most_common(num_keywords)]
    return keywords

