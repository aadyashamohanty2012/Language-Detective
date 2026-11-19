import math
import sys
import unicodedata
from collectiond import Counter
from samples import SAMPLES

THRESHOLD = 0.15

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    
def char_trigrams(text):
    cleaned = []
    for ch in text.lower():
        if ch.isalpha() or unicodedata.category(ch).startswith("M"):
            cleaned.append(ch)
        else:
            cleaned.append(" ")
    padded = " " + " ".join("".join(cleaned).split()) + " "
    return Counter(padded[i:i +3] for i in range(len(padded) - 2))
PROFILES = {language: char_trigrams(text) for language, text in SAMPLES.items()}
def cosine(p , q):
    dot = sum(p[gram] * q[gram] for gram in p if gram in q)  
    size_p = math.sqrt(sum(count * count for count in p.values()))
    size_q = math.sqrt(sum(count * count for count in q.values()))
    if size_p == 0 or size_q == 0:
        return 0.0
    return dot / (size_p * size_q)

def rank_languages(text):
    mystery