import pytest
from metods.user_metods import User
from data import UserData, AnswerAPI
import allure


class TestUserCreate:

    @allure.description("Тест по регистрации пользователя")
    @allure.title("Создать рандомного пользователя")
    def test_create_any_user(self):
        user = User()
        status_code, response_context = user.post_reqest_create_any_user()
        assert status_code == 200 and str(response_context.get("success")) == 'True'

    @allure.description("Тест по регистрации пользователя с дефектными данными")
    @allure.title("Зарегистрировать пользователя с дефектными данными")
    def test_defective_create_user(self):
        user = User()
        status_code, response_context = user.post_reqest_defective_create_user()
        assert status_code == 403 and str(response_context.get("message")) == AnswerAPI.ANSWER_DEFECT_DATA

    @allure.description("Тест по созданию пользователя с одинаковыми логинами")
    @allure.title("Создать пользователя с одинаковыми логинами")
    def test_double_create_user(self, user):
        status_code, response_context = user.post_reqest_create_user()
        assert status_code == 403 and str(response_context.get("message")) == AnswerAPI.ANSWER_DOUBLE_USER


class TestLoginUser:

    @allure.description("Тест по входу пользователя")
    @allure.title("Вход пользователя")
    def test_login_user(self, user):
        status_code, response_context = user.post_reqest_login_user()
        user.delite_reqest_delite_user(response_context['accessToken'])
        assert status_code == 201 and str(response_context.get("success")) == 'True'

    @allure.description("Тест по дефектному входу пользователя")
    @allure.title("Дефектный вход пользователя")
    @pytest.mark.parametrize('data', [UserData.DEFECTIVE_DATA_FOR_LOGIN_BASE_USER_1,
                                      UserData.DEFECTIVE_DATA_FOR_LOGIN_BASE_USER_2])
    def test_login_user(self, user, data):
        status_code, response_context = user.post_reqest_login_user_with_defective_data(data)
        assert status_code == 401 and str(response_context.get("success")) == 'False'


class TestLogoutUser:

    @allure.description("Тест по выходу пользователя")
    @allure.title("Выход пользователя")
    def test_logout_user(self, user):
        status, token_user = user.post_reqest_login_user()
        status_code, response_context = user.post_reqest_logout_user(token_user['refreshToken'])
        assert status_code == 200 and str(response_context.get("success")) == 'True'


class TestChangeUser:

    @allure.description("Тест по изменению данных пользователя")
    @allure.title("Изменение данных пользователя")
    @pytest.mark.parametrize('data', [UserData.NEW_NAME_FOR_BASE_USER,
                                      UserData.NEW_PASSWORD_FOR_BASE_USER])
    def test_change_data_user(self, user, data):
        status, access_token_user = user.post_reqest_login_user()
        status_code, response_context = user.patch_reqest_change_base_user(access_token_user['accessToken'], data)
        assert status_code == 201 and str(response_context.get("success")) == 'True'

    '''Неавторизованный пользователь, это тот что не знает свой accessToken, 
    значит и пытается изменить данные без него, так и построен тест'''

    @allure.description("Тест по изменению данных пользователя, без авторизации")
    @allure.title("Изменение данных пользователя, без авторизации")
    @pytest.mark.parametrize('data', [UserData.NEW_NAME_FOR_BASE_USER,
                                      UserData.NEW_PASSWORD_FOR_BASE_USER])
    def test_change_data_user(self, user, data):
        status_code, response_context = user.patch_reqest_change_base_user_without_login(data)
        assert status_code == 401 and str(response_context.get("success")) == 'False'

