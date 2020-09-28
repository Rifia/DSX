# Лабораторная работа №2
# Input: текст и список слов (из файла и с клавиатуры)
# Задача: найти в тексте все слова, каждое из которых отличается от некоторого слова одной буквой
# и исправить такие слова на слова из списка
# FYI: 1й способ: в лоб, без стандартных встроенных функций по строкам 2й: с ними
# Output: если пользователь попросит, занести результат в файл
# TODO: нечувствительность к регистру

our_text_file = open("res/text_for_second_lab.txt")
word_list_file = open("res/word_list_for_second_lab.txt")
output = open("res/second_output.txt", "w")


def load_dictionary():

    i = -1
    j = 0

    word_list = []

    e = our_text_file.read(1)
    expr = ('a' <= e <= 'z') or ('A' <= e <= 'Z') or e == '-'

    while e != '':
        i += 1
        while expr:
            word_list[i][j] = e
            j += 1
            e = our_text_file.read(1)
            if not expr:
                break

    print(word_list)


def fix_typo():

    text_list = []
    hello_word = []

    e = our_text_file.read(1)

    while ('a' <= e <= 'z') or ('A' <= e <= 'Z') or e == '-':
        hello_word.append(e)
        e = our_text_file.read(1)
            # функция сравнения и поиска слова

    output.write(''.join(hello_word))
    output.close()

    hello_word.clear()








    # идем по файлу
    # каждое встречное слово заносится в переменную hello_word
        # слово - это набор букв, внутри которого допустим только дефис из знаков препинания
        # алгоритм выборки слова: слово - до появляения символа не буквы и не дефиса

    # и сравнивается со словами, которые есть в списке
    # если найдено различие в одной букве
    # найти эту букву в слове
    # и переписать прямо в файле
        # алгоритм: нужно также запомнить место в файле, где произведена остановка
        # чтобы потом по индексу отойти назад, заменить букву и перезаписать файл
        # TODO: как работать с файлом при перезаписи