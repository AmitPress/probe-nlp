from dataclasses import dataclass
from typing import List, Literal

@dataclass
class Message:
    role: Literal["User:", "AI:"] = None
    content: str = None
    total_sentences: int = None
    vectorized_content: List[float] = None

@dataclass
class Corpus:
    path: str = None
    name: str = None
    total_sentences: int = None
    total_tokens: int = None
    topk_words: List[str] = None # which are most frequent tokens
    topic: str = None # this is determined by user query, as we see in many gpt websites like chatgpt or le chat
    raw_content: str = None
    tokenized_content: List[str] = None
    conversation: List[Message] = None
