from english_words import get_english_words_set
import random
import tqdm
import spacy
words = list(get_english_words_set(["web2"]))

nlp = spacy.load("fi_core_news_md")
def score_words(words, topic):
    scores = []
    base = nlp(topic)
    for word in tqdm.tqdm(words, desc="Scoring words"):
        scores.append(base.similarity(nlp(word)))
    scored_words = zip(words, scores)
    scored_words = sorted(scored_words, key=lambda x: x[1], reverse=True)
    return scored_words

def generate_name(_numWords=2, _topic="code"):
    _words = []
    for i in range(len(words)):
        if random.choice([True, False] + [False] * 128):
            _words.append(words[i])
    _scores = score_words(_words, _topic)
    _name = ""
    for i in range(_numWords):
        _name += _scores[random.randint(0, len(_scores))][0].title()
    return _name
    
while True:
    _topic = input("What is your project about? ")
    _numWords = input("How many words? ")
    print(generate_name(int(_numWords), _topic) + " is your new project's name!")