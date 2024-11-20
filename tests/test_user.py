import pytest
from metods.user_metods import User
from data import UserData
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
        assert status_code == 403 and str(response_context.get("message")) == ('Email, password and name are required '
                                                                               'fields')

    @allure.description("Тест по созданию пользователя с одинаковыми логинами")
    @allure.title("Создать пользователя с одинаковыми логинами")
    def test_double_create_user(self, user):
        status_code, response_context = user.post_reqest_create_user()
        status, access_token_user = user.post_reqest_login_user()
        user.delite_reqest_delite_user(access_token_user['accessToken'])
        assert status_code == 403 and str(response_context.get("message")) == 'User already exists'


class TestLoginUser:

    @allure.description("Тест по входу пользователя")
    @allure.title("Вход пользователя")
    def test_login_user(self, user):
        status_code, response_context = user.post_reqest_login_user()
        user.delite_reqest_delite_user(response_context['accessToken'])
        assert status_code == 201 and str(response_context.get("success")) == 'True'

    @allure.description("Тест по дефектному входу пользователя")
    @allure.title("Дефектный вход пользователя")
    @pytest.mark.parametrize('data', [UserData.defective_data_for_login_base_user_1,
                                      UserData.defective_data_for_login_base_user_2])
    def test_login_user(self, user, data):
        status_code, response_context = user.post_reqest_login_user_with_defective_data(data)
        status, access_token_user = user.post_reqest_login_user()
        user.delite_reqest_delite_user(access_token_user['accessToken'])
        assert status_code == 401 and str(response_context.get("success")) == 'False'


class TestLogoutUser:

    @allure.description("Тест по выходу пользователя")
    @allure.title("Выход пользователя")
    def test_logout_user(self, user):
        status, token_user = user.post_reqest_login_user()
        status_code, response_context = user.post_reqest_logout_user(token_user['refreshToken'])
        user.delite_reqest_delite_user(token_user['accessToken'])
        assert status_code == 200 and str(response_context.get("success")) == 'True'


class TestChangeUser:

    @allure.description("Тест по изменению данных пользователя")
    @allure.title("Изменение данных пользователя")
    @pytest.mark.parametrize('data', [UserData.new_name_for_base_user,
                                      UserData.new_password_for_base_user])
    def test_change_data_user(self, user, data):
        status, access_token_user = user.post_reqest_login_user()
        status_code, response_context = user.patch_reqest_change_base_user(access_token_user['accessToken'], data)
        user.delite_reqest_delite_user(access_token_user['accessToken'])
        assert status_code == 201 and str(response_context.get("success")) == 'True'

    '''Неавторизованный пользователь, это тот что не знает свой accessToken, 
    значит и пытается изменить данные без него, так и построен тест'''

    @allure.description("Тест по изменению данных пользователя, без авторизации")
    @allure.title("Изменение данных пользователя, без авторизации")
    @pytest.mark.parametrize('data', [UserData.new_name_for_base_user,
                                      UserData.new_password_for_base_user])
    def test_change_data_user(self, user, data):
        status, access_token_user = user.post_reqest_login_user()
        status_code, response_context = user.patch_reqest_change_base_user_without_login(data)
        user.delite_reqest_delite_user(access_token_user['accessToken'])
        assert status_code == 401 and str(response_context.get("success")) == 'False'

