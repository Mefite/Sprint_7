import pytest
from API.client_api import ClientApi

from API.courier_api import CourierApi
from API.order_api import OrderApi
from helpers import register_new_courier_and_return_login_password


@pytest.fixture
def order_api():
    client = ClientApi()
    return OrderApi(client)

@pytest.fixture
def courier_api():
    client = ClientApi()
    return CourierApi(client)

@pytest.fixture
def cleanup_courier(courier_api):
    """Фикстура для удаления курьера после тестов"""
    couriers = []
    yield couriers
    for creds in couriers:
        login_response = courier_api.login_courier({
            "login": creds["login"],
            "password": creds["password"]
        })
        courier_id = login_response.json().get("id")
        if courier_id:
            courier_api.delete_courier(courier_id)

@pytest.fixture
def random_courier():
    """Создание курьера и возврат его логина, пароля и имени"""
    login, password, first_name = register_new_courier_and_return_login_password()
    return {"login": login, "password": password, "firstName": first_name}