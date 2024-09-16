def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}
        current_position = file.tell()
        for i, string in enumerate(strings, start=1):
            file.write(string + '\n')
            end_position = file.tell()
            strings_positions[(i, current_position)] = string
            current_position = end_position
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
