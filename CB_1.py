from nltk.stem import WordNetLemmatizer
import nltk
import warnings
import numpy as np
import string
import io
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

nltk.download('popular', quiet=True)
with open(r"C:\Users\dell\Desktop\jay\type.txt") as fin:
    raw = fin.read().lower()

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
lemmer = WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "sup", "greetings", "what's up", "hey",)
GREETING_RESPONSES = ["hello", "hi", "*nods*",
                      "hi there", "hi", "I am glad! You are talking to me"]


def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response):
    Emma_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        Emma_response = Emma_response+"I am sorry! I don't understand you"
        return Emma_response
    else:
        Emma_response = Emma_response+sent_tokens[idx]
        return Emma_response


flag = True
print("Emma: My name is Emma. I will answer your queries. If you want to exit, type Bye!")
while(flag == True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response != 'bye'):
        if(user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("Emma: You are welcome..")
        else:
            if(greeting(user_response) != None):
                print("Emma: "+greeting(user_response))
            else:
                print("Emma: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("Emma: Bye! take care..")
