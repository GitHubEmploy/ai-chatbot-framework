import spacy
import os
os.system('python -m spacy download en_core_web_sm')
spacy_tokenizer = spacy.load("en_core_web_sm")
