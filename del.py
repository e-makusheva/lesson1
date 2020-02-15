def get_sum(one, two, delimiter='&'):
    text = f'{one} {delimiter} {two}'.upper()
    return text
print(get_sum('learn', 'Python'))

