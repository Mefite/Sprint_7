import allure
import pytest
from data import CreateCourierData, ResponseText, RandomCourier


class TestCreateCourier:

    @allure.title("Cоздание курьера")
    @allure.description("Проверка создания курьера с валидными данными и код ответа 201, а в "
                        "ответе 'ok' равно True")
    def test_create_courier_success(self, courier_api, cleanup_courier):
        with allure.step("Данные курьера"):
            courier_data = RandomCourier.generate_new_courier(self)

        with allure.step("Создать курьера через API"):
            response = courier_api.create_courier(courier_data)

        with allure.step("Проверить, что в ответе у ключа 'ok' значение 'True'"):
            assert response.json().get("ok") is True

        with allure.step("Удалить данные курьера"):
            cleanup_courier.append(courier_data)


    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("При попытке создать курьера с дублирующимся логином  код ответа 409"
                        " и сообщение об ошибке")
    def test_create_duplicate_courier(self, courier_api, cleanup_courier):
        courier_data = CreateCourierData.SECOND_COURIER

        with allure.step("Создать первого курьера"):
            response1 = courier_api.create_courier(courier_data)
            cleanup_courier.append(courier_data)

        with allure.step("Создание второго курьера с тем же логином"):
            response2 = courier_api.create_courier(courier_data)

        with allure.step("Проверка код ответа 409"):
             assert response2.status_code == 409

        with allure.step("Проверка сообщения об ошибке"):
            assert "Этот логин уже используется" in response2.text


    @allure.title("Обязательные поля должны быть в теле запроса")
    @allure.description("Проверить, что если не передать одно из обязательных полей, сервис возвращает 400 и сообщение"
                        " 'Недостаточно данных'")
    @pytest.mark.parametrize("invalid_data, expected_message", [
        (CreateCourierData.WITHOUT_LOGIN, ResponseText.NO_DATA_CREATE),
        (CreateCourierData.WITHOUT_PASSWORD, ResponseText.NO_DATA_CREATE)])
    def test_create_courier_missing_required_fields(self, courier_api, invalid_data, expected_message):
        with allure.step(f"Создать курьера с неполными данными: {invalid_data}"):
            response = courier_api.create_courier(invalid_data)
        with allure.step("Проверить, что код ответа 400"):
            assert response.status_code == 400
        with allure.step(f"Проверить, что сообщение содержит '{expected_message}'"):
            assert expected_message in response.text