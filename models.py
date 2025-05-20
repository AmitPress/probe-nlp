from dataclasses import dataclass
from typing import List, Literal

@dataclass
class Message:
    role: Literal["User:", "AI:"]
    content: str
    vectorized_content: List[float]

@dataclass
class Corpus:
    path: str
    name: str
    raw_content: str
    tokenized_content: List[str]
    conversation: List[Message]