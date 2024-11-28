class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
    ORDER_URL = 'orders'
    USER_REGISTER_URL = 'auth/register'
    USER_LOGIN_URL = 'auth/login'
    USER_LOGOUT_URL = 'auth/logout'
    USER_DATA_URL = 'auth/user'


class UserData:
    BASE_USER = {"email": "ivanov@ya.ru",
            "password": "123456",
            "name": "ivan"}

    LOGIN_BASE_USER = {"email": "ivanov@ya.ru",
                  "password": "123456"}

    DEFECTIVE_CREATE_BASE_USER = {"email": "ivanov@ya.ru",
                                    "password": "123456"}

    DEFECTIVE_DATA_FOR_LOGIN_BASE_USER_1 = {"email": "ivanov@ya.ru",
                                     "password": "123"}

    DEFECTIVE_DATA_FOR_LOGIN_BASE_USER_2 = {"email": "ivanov@y.r",
                                     "password": "123456"}

    NEW_NAME_FOR_BASE_USER = {"email": "ivanov@ya.ru",
                         "password": "123456",
                         "name": "sani"}

    NEW_PASSWORD_FOR_BASE_USER= {"email": "ivanov@ya.ru",
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

class AnswerAPI:
    ANSWER_NO_INGREDIENT = 'Ingredient ids must be provided'
    ANSWER_NEED_LOGIN = 'You should be authorised'
    ANSWER_DOUBLE_USER = 'User already exists'
    ANSWER_DEFECT_DATA = 'Email, password and name are required fields'