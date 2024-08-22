import allure
from helpers.courier import register_new_courier_and_return_login_password
from helpers.data import login_existing, password_existing, login_error, password_error

@allure.feature('Логин курьера')
@allure.story('Проверка авторизации курьеров')
class TestCourierLogin():

    @allure.title('Логин курьера')
    def test_courier_login_success(self, api_client):
        new_courier_info = register_new_courier_and_return_login_password()
        login, password = new_courier_info[0], new_courier_info[1]
        resp = api_client.courier_login(login, password)
        assert resp.status_code == 200 
        assert 'id' in resp.json()

    @allure.title('Логин курьера: некорректный логин')
    def test_courier_login_error_login(self, api_client):
        resp = api_client.courier_login(login_error, password_existing)
        assert resp.status_code == 404
        assert resp.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Логин курьера: некорректный пароль')
    def test_courier_login_error_password(self, api_client):
        resp = api_client.courier_login(login_existing, password_error)
        assert resp.status_code == 404 
        assert resp.json()['message'] == 'Учетная запись не найдена'

    @allure.title('некорректный: пустой пароль и логин')
    def test_courier_login_missing_login_and_password(self, api_client):
        resp = api_client.courier_login('', '')
        assert resp.status_code == 400 
        assert resp.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('некорректный: пустой логин')
    def test_courier_login_missing_login(self, api_client):
        resp = api_client.courier_login('', password_existing)
        assert resp.status_code == 400
        assert resp.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('некорректный: пустой пароль')
    def test_courier_login_missing_password(self, api_client):
        resp = api_client.courier_login(login_existing, '')
        assert resp.status_code == 400 
        assert resp.json()['message'] == 'Недостаточно данных для входа'