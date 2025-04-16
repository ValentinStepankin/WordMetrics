"""Модуль для вычисления TF-IDF всех уникальных слов в тексте."""

from collections import Counter
import math


def calculate_tfidf(words: list[str]) -> list[dict]:
    total_words = len(words)
    word_counts = Counter(words)

    tfidf_data = []
    for word, count in word_counts.items():
        tf = count / total_words
        idf = math.log(total_words / count) if count else 0
        tfidf_data.append({"word": word, "tf": round(tf, 6), "idf": round(idf, 6)})

    tfidf_data.sort(key=lambda x: x["idf"], reverse=True)
    return tfidf_data[:50]
