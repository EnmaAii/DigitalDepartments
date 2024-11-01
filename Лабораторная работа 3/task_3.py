# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    letter_count = {}
    order_of_letters = []
    for letter in text:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
                order_of_letters.append(letter)
    return letter_count, order_of_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_count, order_of_letters):
    total_letters = sum(letter_count.values())
    frequency = {}
    for letter in order_of_letters:
        frequency[letter] = letter_count[letter] / total_letters
    return frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letter_count, order_of_letters = count_letters(main_str)
frequency = calculate_frequency(letter_count, order_of_letters)

for letter in order_of_letters:
    print(f"{letter}: {frequency[letter]:.2f}")