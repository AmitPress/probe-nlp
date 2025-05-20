from parser import parse_corpora
from language_processing import summarize_corpus, tokenize_corpus
from utils import save_summary

corpora = parse_corpora()
for corpus in corpora:
    tokenize_corpus(corpus)
    save_summary(corpus.name,summarize_corpus(corpus))
