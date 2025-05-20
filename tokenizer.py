# In this module we will do text analysis and populate the corpus with tokenized content
from models import Corpus, Message

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')


def tokenize_message(message: Message):
    data = message.content
    tokens = nltk.word_tokenize(data)
    # remove punctuations
    tokens = [token for token in tokens if token.isalpha()]
    # remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def tokenize_corpus(corpus: Corpus):
    corpus.tokenized_content = []
    for message in corpus.conversation:
        message.vectorized_content = tokenize_message(message)
        corpus.tokenized_content += message.vectorized_content
    return corpus