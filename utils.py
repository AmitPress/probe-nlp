import os
from pathlib import Path
def get_corpus_path(dir: str = "corpora"):
    # find current working directory
    cwd = Path.cwd()
    return [cwd.joinpath(dir, f) for f in os.listdir(dir) if f.endswith(".txt")]

def read_corpus(path: str):
    with open(path, "r") as f:
        return f.read()
