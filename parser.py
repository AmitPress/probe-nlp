from models import Corpus, Message
from utils import get_corpus_path, read_corpus
from typing import List
def parse_corpora(dir: str = "corpora") -> List[Corpus]:
    corpora = []
    for path in get_corpus_path(dir):
        corpus = Corpus()
        corpus.path = path
        corpus.name = path.stem
        corpus.raw_content = read_corpus(path)
        corpus.conversation = []
        for line in corpus.raw_content.split("\n"):
            match line.split(":", 1):
                case [user, content] if user == "User":
                    corpus.conversation.append(Message(role=user, content=content))
                case [user, content] if user == "AI":
                    corpus.conversation.append(Message(role=user, content=content))
        corpora.append(corpus)
    return corpora
