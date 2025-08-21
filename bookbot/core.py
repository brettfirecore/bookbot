from collections import Counter
from pathlib import Path

# only plain ASCII punctuation here
PUNCT = '.,;:!?\"\'()[]{}<>-'

def _load(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

def analyze(path: str) -> dict:
    text = _load(path)
    words = text.split()
    cleaned = [w.lower().strip(PUNCT) for w in words if w.strip(PUNCT)]
    return {
        "characters": len(text),
        "words": len(words),
        "unique_words": len(set(cleaned)),
    }

def top_words(path: str, n: int = 10):
    text = _load(path)
    words = [w.lower().strip(PUNCT) for w in text.split()]
    ctr = Counter(w for w in words if w)
    return ctr.most_common(n)
