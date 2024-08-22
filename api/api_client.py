import requests
import allure
from helpers.data import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    @allure.step('Запрос на создание курьера')
    def create_courier(self, login, password, first_name):
        url = f'{self.base_url}/courier'
        data = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        response = requests.post(url, json=data)
        return response

    @allure.step('Запрос на логин курьера')
    def courier_login(self, login, password):
        url = f'{self.base_url}/courier/login'
        data = {
            'login': login,
            'password': password
        }
        response = requests.post(url, json=data)
        return response

    @allure.step('Запрос на создание заказа')
    def create_order(self, order_data):
        url = f'{self.base_url}/orders'
        response = requests.post(url, json=order_data)
        return response

    @allure.step('Запрос на получение заказов')
    def get_orders(self):
        url = f'{self.base_url}/orders'
        response = requests.get(url)
        return response