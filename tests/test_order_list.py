import allure

class TestOrderList():

    @allure.feature('Список заказов')
    @allure.story('Проверка списка заказов')
    def test_get_order_list(self, api_client):
        resp = api_client.get_orders()
        assert resp.status_code == 200, 'некорректный статус-код'
        assert len(resp.json()['orders']) > 0, 'кол-во заказов равно 0'
