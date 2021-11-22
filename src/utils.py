import re

def number_is_valid(number):
    """
    Receive a number and check if he format is valid
    
    format should be an integer in the range from "-99999" to "99999"
    """
    return bool(re.match('^(-?\d{1,5})$', number))

def number_to_text_format(number):
    """
    Receive a string containing a number and return a string with the same number in his text format.

    :param number: A string containing a number in the range from -99999 to 99999

    :return text_format: Number in his text format

    Example:
        number_to_text_format('524')   => quinhentos e vinte e quatro
        number_to_text_format('-2102') => menos dois mil e cento e dois
    """
    TRANSLATION = {
        '-': 'menos',
        '0': '',
        '1': ['um', 'dez', 'cem'],
        '2': ['dois', 'vinte', 'duzentos'],
        '3': ['três', 'trinta', 'trezentos'],
        '4': ['quatro', 'quarenta', 'quatrocentos'],
        '5': ['cinco', 'cinquenta', 'quinhentos'],
        '6': ['seis', 'sessenta', 'seiscentos'],
        '7': ['sete', 'setenta', 'setecentos'],
        '8': ['oito', 'oitenta', 'oitocentos'],
        '9': ['nove', 'noventa', 'novecentos'],
        '10': 'dez',
        '11': 'onze',
        '12': 'doze',
        '13': 'treze',
        '14': 'quatorze',
        '15': 'quinze',
        '16': 'dezesseis',
        '17': 'dezessete',
        '18': 'dezoito',
        '19': 'dezenove',
    }
    text_format = ""
    absolute_number = number

    if not int(absolute_number):
        return text_format + 'zero'

    if number[0] == '-':
        absolute_number = number[1:]
        text_format += f"{TRANSLATION['-']} "

    number_grouped = group_number_in_three(absolute_number)
    for index, group in enumerate(number_grouped):
        is_first_group = (index == 0 and len(number_grouped) > 1)
        centena, dezena, unidade = group.zfill(3)
        text_list = []

        if int(centena):
            if centena == '1' and (int(dezena) or int(unidade)):
                text_list.append('cento')
            else:
                text_list.append(TRANSLATION[centena][2])

        if int(dezena):
            if dezena == '1' and (int(unidade)):
                text_list.append(TRANSLATION[dezena + unidade])
            else:
                text_list.append(TRANSLATION[dezena][1])

        if int(unidade) and dezena != '1':
            if unidade == '1' and is_first_group:
                pass
            else:
                text_list.append(TRANSLATION[unidade][0])

        text_format += ' e '.join(filter(None, text_list))

        if is_first_group:
            if len(text_list) == 1:
                text_format += ' '
            text_format += 'mil'
            if int(number_grouped[1]):
                text_format += ' e '

    return text_format

def group_number_in_three(number):
    return [number[::-1][i:i+3:][::-1] for i in range(0, len(number), 3)][::-1]