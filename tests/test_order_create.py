import pytest
import allure

@allure.feature('Создание заказов')
@allure.story('Проверка создания заказов')
class TestOrderCreation:

    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    @allure.title('')
    def test_create_order(self, api_client, color):
        order_data = {
            'firstName': 'Diana',
            'lastName': 'Test',
            'address': 'St.Petersburg, Pushkin\'s st.',
            'metroStation': 2,
            'phone': '+7 800 100 10 10',
            'rentTime': 5,
            'deliveryDate': '2024-07-05',
            'comment': 'im gonna test it',
            'color': color
        }

        with allure.step(f'Создаем заказ с цветом(-ами): {color}'):
            response = api_client.create_order(order_data)
            assert 'track' in response.json()