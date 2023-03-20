# 9. (*) Написать функцию представления числа (до миллиона включительно) в виде строки,
# например 217045 –> "Двести семнадцать тысяч сорок пять".
ZERO = 'ноль'

ONES_FEMININE = {
    0: '',
    1: 'одна',
    2: 'две',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
}

ONES = {
    0: '',
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
}

TENS = {
    0: 'десять',
    1: 'одиннадцать',
    2: 'двенадцать',
    3: 'тринадцать',
    4: 'четырнадцать',
    5: 'пятнадцать',
    6: 'шестнадцать',
    7: 'семнадцать',
    8: 'восемнадцать',
    9: 'девятнадцать',
}

TWENTIES = {
    2: 'двадцать',
    3: 'тридцать',
    4: 'сорок',
    5: 'пятьдесят',
    6: 'шестьдесят',
    7: 'семьдесят',
    8: 'восемьдесят',
    9: 'девяносто',
}

HUNDREDS = {
    1: 'сто',
    2: 'двести',
    3: 'триста',
    4: 'четыреста',
    5: 'пятьсот',
    6: 'шестьсот',
    7: 'семьсот',
    8: 'восемьсот',
    9: 'девятьсот',
}

THOUSANDS = {
    1: ('тысяча', 'тысячи', 'тысяч'),  # 10^3
    # 2: ('миллион', 'миллиона', 'миллионов'),  # 10^6
    # 3: ('миллиард', 'миллиарда', 'миллиардов'),  # 10^9
    # 4: ('триллион', 'триллиона', 'триллионов'),  # 10^12
    # 5: ('квадриллион', 'квадриллиона', 'квадриллионов'),  # 10^15
    # 6: ('квинтиллион', 'квинтиллиона', 'квинтиллионов'),  # 10^18
    # 7: ('секстиллион', 'секстиллиона', 'секстиллионов'),  # 10^21
    # 8: ('септиллион', 'септиллиона', 'септиллионов'),  # 10^24
    # 9: ('октиллион', 'октиллиона', 'октиллионов'),  # 10^27
    # 10: ('нониллион', 'нониллиона', 'нониллионов'),  # 10^30
}


def num2words(number):
    result = ''
    if number < 0:
        result += 'минус '
        number = - number
    current_len = len(str(number))

    if current_len < 4:
        if current_len == 1 and number > 0:
            result += ONES[number]
            return result
        if current_len == 2:
            if number < 20:
                result += TENS[number % 10]
                return result
            if number >= 20:
                result += TWENTIES[number // 10] + (' ' + ONES[number % 10] if number % 10 > 0 else "")
                return result
        if current_len == 3:
            result += HUNDREDS[number // 100] + (' ' + num2words(number % 100) if number % 100 > 0 else "")
            return result
    elif 4 <= current_len <= 6:
        variant_of_thousands = find_fem(number // 1000)
        result += nums_before_thousands(number // 1000)
        result += THOUSANDS[1][
                      variant_of_thousands] + (' ' + num2words(number % 1000) if number % 1000 > 0 else "")
    return result


def find_fem(number):
    fem_nums = [2, 3, 4]
    if 10 < number % 100 < 20:
        return 2
    elif number % 10 == 1:
        return 0
    elif (number % 10) in fem_nums:
        return 1
    return 2


def nums_before_thousands(number):
    if 10 < number % 100 < 20:
        return num2words(number) + ' '
    else:
        if len(str(number)) == 1:
            return ONES_FEMININE[number % 10] + ' '
        else:
            return num2words((number // 10) * 10) + (' ' + ONES_FEMININE[number % 10] if number % 10 > 0 else '') + ' '


print(num2words(333333))

