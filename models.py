from dataclasses import dataclass
from typing import List, Literal

@dataclass
class Message:
    role: Literal["User:", "AI:"] = None
    content: str = None
    vectorized_content: List[float] = None

@dataclass
class Corpus:
    path: str = None
    name: str = None
    raw_content: str = None
    tokenized_content: List[str] = None
    conversation: List[Message] = None