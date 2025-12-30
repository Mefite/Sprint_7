import allure

class TestListOrders:

    @allure.title("Получение списка заказов")
    @allure.description("Проверка возвращения списка заказов и кода ответа 200")
    def test_get_order_list(self, order_api):
        with allure.step("Отправка запроса на получение списка"):
            response = order_api.get_order_list()
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Десереализация ответа"):
            data = response.json()
        with allure.step("Проверка содержания ответа по параметру 'orders'"):
            assert "orders" in data
        with allure.step("Проверка типа ответа на 'list'"):
            assert isinstance(data["orders"], list)