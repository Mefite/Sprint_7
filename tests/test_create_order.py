import allure
import pytest
from data import CreateOrderData


class TestListOrders:

    @allure.title("Создание заказа самоката")
    @allure.description("Проверка возможности заказа самоката разных цветов")
    @pytest.mark.parametrize("color", CreateOrderData.COLORS)
    def test_create_order_with_color(self, order_api, color):
        with allure.step("Отправка запроса на заказ самоката"):
            order_data = {**CreateOrderData.BASE_ORDER, "color": color}

            with allure.step("Отправка запроса на создание заказа"):
                response = order_api.create_order(order_data)

            with allure.step("Десериализация ответа"):
                data = response.json()

            with allure.step("Проверка, что тело ответа содержит track"):
                assert "track" in data
                assert isinstance(data["track"], int)

            with allure.step("Проверка выбранного цвета самоката"):
                for c in color:
                    assert c in {"BLACK", "GREY"}
