def get_count_char(str_):
    letters_dict = {}
    str_ = "".join(str_.lower().split())

    for letter in str_:
        if letter.isalpha():
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
    return letters_dict


def percentage(letters_dict):  # 5 пункт
    total = 0
    for letter in letters_dict:
        total += letters_dict[letter]
    for letter in letters_dict:
        letters_dict[letter] = round(letters_dict[letter]/total * 100, 1)
    return letters_dict


...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percentage(get_count_char(main_str)))
