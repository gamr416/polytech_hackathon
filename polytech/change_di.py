def change_di(key, value):
    file = open('di.py', 'r', encoding='utf-8')
    default_di = file.read()[:-1]
    file.close()
    new_str = f"\n'{key}': '{value}\\n',"
    new_str = new_str + '}'
    result = default_di + new_str
    file = open('di.py', 'w', encoding='utf-8')
    file.write(result)
    file.close()