def get_num_words(text: str) -> int:
    return len(text.split())

def get_letter_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ch in text.lower():
        if 'a' <= ch <= 'z':        # count only letters
            counts[ch] = counts.get(ch, 0) + 1
    return counts
