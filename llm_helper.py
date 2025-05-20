import os
from dotenv import load_dotenv

from models import Corpus
load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API"))

model = genai.GenerativeModel("gemini-2.0-flash")

def find_topic(corpus: Corpus):
    # find user prompts
    prompt = " ".join([message.content for message in corpus.conversation if message.role == "User"])
    system_prompt = "What is this conversation about? Summarize in one sentence: "
    response = model.generate_content(system_prompt + prompt)
    return response.text