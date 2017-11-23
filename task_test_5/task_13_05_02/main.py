# Программирование на языке высокого уровня (Python).
# Задание task_13_05_02. Вариант !!!
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!

import vk
# https://oauth.vk.com/authorize?client_id=6104500&scope=friends&redirect_uri=http://oauth.vk.com/blank.html&display=page&response_type=token
if __name__ == "__main__":
    v = vk.vk("31908763", "a1752332c34ca17478a2938982f0ebc3e01a3cf55297c10d06ded262b098d8bcc7f9b50fbacca1033895f")
    v._load_info()
    print(v)
    v.show_plot()
