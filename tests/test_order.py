import pytest
from metods.user_metods import User
from metods.order_metods import Order
from data import OrderData
import allure


class TestOrderCreate:

    """Думаю тесты по созданию заказа с авторизацией и тест по созданию заказа с ингредлиентами должны быть одним
    тестом (так как они положительные)"""
    @allure.description("Тест по созданию заказа с авторизацией и ингредиентами")
    @allure.title("Создать заказ с авторизацией")
    @pytest.mark.parametrize('data', [OrderData.ORDER_DATA_1, OrderData.ORDER_DATA_2])
    def test_create_order_with_login_user(self, data):
        user = User()
        user.post_reqest_create_user()
        status, access_token_user = user.post_reqest_login_user()
        order = Order()
        status_code, response_context = order.post_reqest_create_order_with_login(access_token_user['accessToken'], data)
        user.delite_reqest_delite_user(access_token_user['accessToken'])
        assert status_code == 200 and str(response_context.get("success")) == 'True'

    @allure.description("Тест по созданию заказа без авторизации")
    @allure.title("Создать заказ без авторизации")
    def test_create_order_without_login_user(self):
        order = Order()
        status_code, response_context = order.post_reqest_create_order_without_login()
        assert status_code == 200 and str(response_context.get("success")) == 'True'

    @allure.description("Тест по созданию заказа с авторизацией без ингредиентов")
    @allure.title("Создать заказ с авторизацией и без ингредиетов")
    def test_create_order_without_ingredients(self):
        user = User()
        user.post_reqest_create_user()
        status, access_token_user = user.post_reqest_login_user()
        order = Order()
        status_code, response_context = order.post_reqest_create_order_without_igredients(access_token_user['accessToken'])
        user.delite_reqest_delite_user(access_token_user['accessToken'])
        assert status_code == 400 and str(response_context.get("message")) == 'Ingredient ids must be provided'

    @allure.description("Тест по созданию заказа с авторизацией и неверным номером ингредиента")
    @allure.title("Создать заказ с авторизацией и неверным номером ингредиета")
    def test_create_order_with_defectiv_hash_ingredients(self):
        user = User()
        user.post_reqest_create_user()
        status, access_token_user = user.post_reqest_login_user()
        order = Order()
        status_code = order.post_reqest_create_order_with_defectiv_hesh_ingredients(access_token_user['accessToken'])
        user.delite_reqest_delite_user(access_token_user['accessToken'])
        assert status_code == 500


class TestGetOrder:

    @allure.description("Тест по получению заказов пользователя с авторизацией")
    @allure.title("Получить заказы пользователя с авторизацией")
    def test_get_user_orders_with_login(self):
        user = User()
        user.post_reqest_create_user()
        status, access_token_user = user.post_reqest_login_user()
        order = Order()
        status_code, response_context = order.get_reqest_get_user_orders(access_token_user['accessToken'])
        user.delite_reqest_delite_user(access_token_user['accessToken'])
        assert status_code == 200 and str(response_context.get("success")) == 'True'

    @allure.description("Тест по получению заказов пользователя без авторизации")
    @allure.title("Получить заказы пользователя без авторизации")
    def test_get_user_orders_without_login(self):
        user = User()
        user.post_reqest_create_user()
        status, access_token_user = user.post_reqest_login_user()
        order = Order()
        status_code, response_context = order.get_reqest_get_user_orders_without_login()
        user.delite_reqest_delite_user(access_token_user['accessToken'])
        assert status_code == 401 and str(response_context.get("message")) == 'You should be authorised'

