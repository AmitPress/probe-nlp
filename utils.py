import os
from pathlib import Path
from collections import Counter
from typing import List
def get_corpus_path(dir: str = "corpora"):
    # find current working directory
    cwd = Path.cwd()
    return [cwd.joinpath(dir, f) for f in os.listdir(dir) if f.endswith(".txt")]

def read_corpus(path: str):
    with open(path, "r") as f:
        return f.read()

def find_topk(tokens: List[str], topk: int = 5):
    tokens = Counter(tokens).most_common(topk)
    return [token[0] for token in tokens]

def save_summary(filename: str, summary: str):
    directory = "summaries"
    Path(directory).mkdir(parents=True, exist_ok=True)
    with open(f"{directory}/{filename}.txt", "w") as f:
        f.write(summary)
    
