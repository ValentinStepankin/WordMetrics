"""Модуль для предварительной обработки текста перед анализом TF-IDF."""

import re


def process_text(text: str) -> list[str]:
    text = text.lower()
    words = re.findall(r'\b[a-zа-яё]+\b', text)
    return words
