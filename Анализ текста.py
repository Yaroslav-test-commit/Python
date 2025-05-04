def word_count(words):
    word_count = 0
    for _ in words:
        word_count += 1
    print(f"Количество слов в тексте: {word_count}")


def longest_word(words):
    longest_word_test = ""
    for word in words:
        if len(word) > len(longest_word_test):
            longest_word_test = word
    print(f"Самое длинное слово: {longest_word_test}")


def vowels_count(new_text):
    vowels = "аеёиоуыэюя"
    vowels_count = 0
    for _ in new_text:
        if _ in vowels:
            vowels_count += 1
    print(f"Количество гласных букв в тексе: {vowels_count}")


def word_count_new(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(f"Количество раз для слов:")
    for word in word_count:
        print(f"{word} - {word_count[word]}")


text = input("Введите текст: ").lower()
symbols = """#$%&*+-/=<>^|~\\[]{}();:"',.!?@`"""
new_text = "".join(char for char in text if char not in symbols)
test_words = new_text.split()

word_count(test_words)
longest_word(test_words)
vowels_count(new_text)
word_count_new(test_words)