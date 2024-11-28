import requests
from data import Urls, OrderData
import allure


class Order:

    @allure.step("создать заказ без авторизации")
    def post_reqest_create_order_without_login(self):
        payload = OrderData.ORDER_DATA_1
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.ORDER_URL}", json=payload, headers=headers)
        return response.status_code, response.json()

    @allure.step("создать заказ с авторизацией")
    def post_reqest_create_order_with_login(self, accessToken, order_data):
        payload = order_data
        headers = {"Content-Type": "application/json", 'authorization': accessToken}
        response = requests.post(f"{Urls.BASE_URL}{Urls.ORDER_URL}", json=payload, headers=headers)
        return response.status_code, response.json()

    @allure.step("создать заказ с авторизацией, без ингридиентов")
    def post_reqest_create_order_without_igredients(self, accessToken):
        payload = OrderData.ORDER_DATA_WITHOUT_INGREDIENTS
        headers = {"Content-Type": "application/json", 'authorization': accessToken}
        response = requests.post(f"{Urls.BASE_URL}{Urls.ORDER_URL}", json=payload, headers=headers)
        return response.status_code, response.json()

    @allure.step("создать заказ с авторизацией и неверным хеш ингридиентов")
    def post_reqest_create_order_with_defectiv_hesh_ingredients(self, accessToken):
        payload = OrderData.ORDER_DATA_DEFECTIV_HESH_INGREDIENTS
        headers = {"Content-Type": "application/json", 'authorization': accessToken}
        response = requests.post(f"{Urls.BASE_URL}{Urls.ORDER_URL}", json=payload, headers=headers)
        return response.status_code

    @allure.step("получить заказы пользователя")
    def get_reqest_get_user_orders(self, accessToken):
        headers = {"Content-Type": "application/json", 'authorization': accessToken}
        response = requests.get(f"{Urls.BASE_URL}{Urls.ORDER_URL}",  headers=headers)
        return response.status_code, response.json()

    @allure.step("получить заказы пользователя без авторизации")
    def get_reqest_get_user_orders_without_login(self):
        headers = {"Content-Type": "application/json"}
        response = requests.get(f"{Urls.BASE_URL}{Urls.ORDER_URL}",  headers=headers)
        return response.status_code, response.json()

