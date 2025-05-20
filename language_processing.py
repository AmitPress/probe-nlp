# In this module we will do text analysis and populate the corpus with tokenized content
from models import Corpus, Message
from utils import find_topk

import nltk
# download necessary packages
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
from llm_helper import find_topic # this will make internet call, so make sure you are connected


def tokenize_message(message: Message):
    data = message.content
    tokens = nltk.word_tokenize(data)
    # remove punctuations
    tokens = [token for token in tokens if token.isalpha()]
    # remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    # lets ignore stemming or lemmatization here
    return tokens

def tokenize_corpus(corpus: Corpus):
    corpus.tokenized_content = []
    corpus.total_sentences = 0
    for message in corpus.conversation:
        message.total_sentences = len(nltk.sent_tokenize(message.content))
        corpus.total_sentences += message.total_sentences
        message.vectorized_content = tokenize_message(message)
        corpus.tokenized_content += message.vectorized_content
    corpus.total_tokens = len(corpus.tokenized_content) # we could have calculated this via message but lets not go there as of now
    corpus.topk_words = find_topk(corpus.tokenized_content)
    corpus.topic = find_topic(corpus)
    return corpus

def summarize_corpus(corpus: Corpus):
    summary = f"--------------------------------------Corpus: {corpus.name}-------------------------------------------\n"
    summary += "- Summary:\n"
    summary += f"- Number of dialogues: {len(corpus.conversation)}\n"
    summary += f"- Total messages by User: {len([message for message in corpus.conversation if message.role == 'User'])}\n"
    summary += f"- Total messages by AI: {len([message for message in corpus.conversation if message.role == 'AI'])}\n"
    summary += f"- Number of Total Sentences: {corpus.total_sentences}\n"
    summary += f"- Number of TotalTokens: {corpus.total_tokens}\n"
    summary += f"- Conversation Topic: {corpus.topic}\n"
    summary += f"- Top 5 words: {corpus.topk_words}\n"
    summary += f"---------------------------------------------------------------------------------\n"
    return summary