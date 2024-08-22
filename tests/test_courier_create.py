import random
import allure
from helpers.data import login_existing, password_existing, first_name


@allure.feature('Создание курьера')
@allure.story('Проверка создания курьеров')
class TestCourierCreation:

    @allure.title('Создание курьера: корректный код ответа')
    def test_create_courier_correct_response_code(self, api_client):
        sffx = str(random.randint(0, 1000))
        resp = api_client.create_courier(login_existing + sffx, password_existing + sffx, first_name + sffx)
        assert resp.status_code == 201
        assert resp.json()['ok']


    @allure.title('Создание курьера: пользователь уже создан')
    def test_create_courier_double(self, api_client):
        resp = api_client.create_courier(login_existing, password_existing, first_name)
        assert resp.status_code == 409 
        assert 'Этот логин уже используется. Попробуйте другой.' in resp.json()['message']


    @allure.title('Создание курьера: пропущено поле логина')
    def test_create_courier_missing_login(self, api_client):
        resp = api_client.create_courier('', password_existing, first_name)
        assert resp.status_code == 400 
        assert 'Недостаточно данных для создания учетной записи' in resp.json()['message']

    @allure.title('Создание курьера: пропущено поле пароля')
    def test_create_courier_missing_password(self, api_client):
        resp = api_client.create_courier(login_existing, '', first_name)
        assert resp.status_code == 400 
        assert 'Недостаточно данных для создания учетной записи' in resp.json()['message']