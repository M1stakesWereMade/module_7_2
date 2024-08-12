def custom_write(file_name, strings):
    with open(file_name, 'wb') as file:
        strings_positions = {}
        for i, string in enumerate(strings, start=1):
            byte_position = file.tell()
            bytes_string = string.encode('utf-8')
            file.write(bytes_string)
            strings_positions[(i, byte_position)] = string
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