import random
import string

# метод генерации нового пользователя
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя пользователя
    login = f'{generate_random_string(8)}@ya.ru'
    password = generate_random_string(8)
    first_name = f'{generate_random_string(8)}'

    payload = {
        "email": login,
        "password": password,
        "name": first_name
    }
    # возвращаем список
    return payload

