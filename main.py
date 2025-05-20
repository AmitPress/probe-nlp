from parser import parse_corpora
from language_processing import summarize_corpus, tokenize_corpus
from utils import save_summary

corpora = parse_corpora() # parse the text into objects
for corpus in corpora:
    tokenize_corpus(corpus) # tokenize the text and populate the objects
    save_summary(corpus.name,summarize_corpus(corpus)) # saves the summary to a file
