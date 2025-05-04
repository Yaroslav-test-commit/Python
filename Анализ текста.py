text = input("Введите текст: ").lower()
symbols = """#$%&*+-/=<>^|~\\[]{}();:"',.!?@`"""
new_text = "".join(char for char in text if char not in symbols)
words = new_text.split()


def word_count():
    word_count = 0
    for _ in words:
        word_count += 1
    print(f"Количество слов в тексте: {word_count}")


def longest_word():
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"Самое длинное слово: {longest_word}")


def vowels_count():
    vowels = "аеёиоуыэюя"
    vowels_count = 0
    for _ in new_text:
        if _ in vowels:
            vowels_count += 1
    print(f"Количество гласных букв в тексе: {vowels_count}")


def word_count_new():
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(f"Количество раз для слов:")
    for word in word_count:
        print(f"{word} - {word_count[word]}")


word_count()
longest_word()
vowels_count()
word_count_new()
