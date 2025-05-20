import os
from dotenv import load_dotenv

from models import Corpus
load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API")) # make sure you have added your api key

model = genai.GenerativeModel("gemini-2.0-flash") # this model performs well in this case

def find_topic(corpus: Corpus):
    # find user prompts
    prompt = " ".join([message.content for message in corpus.conversation if message.role == "User"]) # The topic will be  based on user inputs
    system_prompt = "What is this conversation about? Summarize in one sentence: " # this prompt will guide the model
    response = model.generate_content(system_prompt + prompt) # this does not retain context as they mentioned which is what we want
    return response.text # just gives me the text