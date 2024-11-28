import requests
from data import Urls, UserData
from generate_random_user import register_new_courier_and_return_login_password
import allure


class User:

    @allure.step("создать пользователя")
    def post_reqest_create_user(self):
        payload = UserData.BASE_USER
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_REGISTER_URL}", json=payload, headers=headers)
        return response.status_code, response.json()

    @allure.step("создать рандомного пользователя")
    def post_reqest_create_any_user(self):
        payload = register_new_courier_and_return_login_password()
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_REGISTER_URL}", json=payload, headers=headers)
        return response.status_code, response.json()

    @allure.step("создать пользователя с дефектными данными")
    def post_reqest_defective_create_user(self):
        payload = UserData.DEFECTIVE_CREATE_BASE_USER
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_REGISTER_URL}", json=payload, headers=headers)
        return response.status_code, response.json()

    @allure.step("вход пользователя")
    def post_reqest_login_user(self):
        payload = UserData.LOGIN_BASE_USER
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_LOGIN_URL}", json=payload, headers=headers)
        return response.status_code, response.json()

    @allure.step("вход пользователя без пароля")
    def post_reqest_login_user_with_defective_data(self, data):
        payload = data
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_LOGIN_URL}", json=payload, headers=headers)
        return [response.status_code, response.json()]

    @allure.step("выход пользователя")
    def post_reqest_logout_user(self, refreshToken):
        payload = {"token": f"{refreshToken}"}
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_LOGOUT_URL}", json=payload, headers=headers)
        return response.status_code, response.json()

    @allure.step("удалить пользователя")
    def delite_reqest_delite_user(self, accessToken):
        payload = UserData.LOGIN_BASE_USER
        headers = {"Content-Type": "application/json", 'authorization': accessToken}
        response = requests.delete(f"{Urls.BASE_URL}{Urls.USER_DATA_URL}", json=payload, headers=headers)
        return [response.status_code, response.json()]

    @allure.step("изменить данные пользователя")
    def patch_reqest_change_base_user(self, accessToken, data_for_change):
        payload = data_for_change
        headers = {"Content-Type": "application/json", 'authorization': accessToken}
        response = requests.patch(f"{Urls.BASE_URL}{Urls.USER_DATA_URL}", json=payload, headers=headers)
        return [response.status_code, response.json()]

    @allure.step("изменить данные пользователя без авторизации")
    def patch_reqest_change_base_user_without_login(self, data_for_change):
        payload = data_for_change
        headers = {"Content-Type": "application/json"}
        response = requests.patch(f"{Urls.BASE_URL}{Urls.USER_DATA_URL}", json=payload, headers=headers)
        return [response.status_code, response.json()]

