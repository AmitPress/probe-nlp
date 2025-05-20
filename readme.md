# Conversation Summarization
In this excercise I have showed how to take dialogues from the text files kept inside `corpora` folder. And parse them into usable python objects and extract summary of the conversation.

#### Work Process
- First I have made the models to persist the corpus informations
- Then I made sure the models can be used as in memory databases (sort of) via dataclasses
- I have created the parser that will parse the lexemes or words into tokens. I have first thought of writing a handwritten recursive decent parser but later realized it will be an overkill and unnecessary
- I have kept all nlp related task inside `language_processing` module
- I have used gemini to summarize the topic in one sentence, I have tried gensim and sumy, and found both of them to be not up to the mark

#### Running the project
> You must have `uv` installed [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Just do `uv sync`
- Make sure you have placed your gemini api from `aistudio.google.com` (It's Free*!)
- Then do `uv run main.py`

#### Important!
- Make sure you have seen the demo inside summaries
- Clean up them after you have checked them
- Newly created summaries will be created there