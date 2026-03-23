import string
from typing import Dict, Union

def analyze_text(text: str) -> Dict[str, Union[int, float]]:
    # Приводим текст к нижнему регистру
    text_lower = text.lower()
    # Создаём таблицу замены: все знаки препинания заменяем на пробелы
    punct_to_space = str.maketrans({c: ' ' for c in string.punctuation})
    cleaned = text_lower.translate(punct_to_space)
    # Разбиваем строку на слова по пробелам (split удаляет пустые элементы)
    words = cleaned.split()
    # Обработка пустого текста
    if not words:
        return {
            'total_words': 0,
            'unique_words': 0,
            'avg_word_length': 0.0
        }

    total = len(words)
    unique = len(set(words))
    avg_len = sum(len(w) for w in words) / total
    avg_len_rounded = round(avg_len, 2)

    return {
        'total_words': total,
        'unique_words': unique,
        'avg_word_length': avg_len_rounded
    }
# Пример использования (для проверки)
if __name__ == "__main__":
    raw_text = "Hello, world! Hello everyone. This is a test... A TEST!"
    stats = analyze_text(raw_text)
    print(stats)
