class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
    ORDER_URL = 'orders'
    USER_REGISTER_URL = 'auth/register'
    USER_LOGIN_URL = 'auth/login'
    USER_LOGOUT_URL = 'auth/logout'
    USER_DATA_URL = 'auth/user'


class UserData:
    base_user = {"email": "ivanov@ya.ru",
            "password": "123456",
            "name": "ivan"}

    login_base_user = {"email": "ivanov@ya.ru",
                  "password": "123456"}

    defective_create_base_user = {"email": "ivanov@ya.ru",
                                    "password": "123456"}

    defective_data_for_login_base_user_1 = {"email": "ivanov@ya.ru",
                                     "password": "123"}

    defective_data_for_login_base_user_2 = {"email": "ivanov@y.r",
                                     "password": "123456"}

    new_name_for_base_user = {"email": "ivanov@ya.ru",
                         "password": "123456",
                         "name": "sani"}

    new_password_for_base_user = {"email": "ivanov@ya.ru",
                             "password": "654321",
                             "name": "ivan"}


class OrderData:
    ORDER_DATA_1 = {"ingredients": ["61c0c5a71d1f82001bdaaa6d",
                                    "61c0c5a71d1f82001bdaaa6f",
                                    "61c0c5a71d1f82001bdaaa72"]}

    ORDER_DATA_2 = {"ingredients": ["61c0c5a71d1f82001bdaaa6c",
                                    "61c0c5a71d1f82001bdaaa78",
                                    "61c0c5a71d1f82001bdaaa7a"]}

    ORDER_DATA_WITHOUT_INGREDIENTS = {"ingredients": []}

    ORDER_DATA_DEFECTIV_HESH_INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001b"]}

