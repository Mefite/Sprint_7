import random
import string

class CreateCourierData:
    VALID_COURIER = {
        "login": "user_1",
        "password": "password1",
        "firstName": "Test"
    }

    LOGIN_COURIER = {
        "login": "user_2",
        "password": "password2",
        "firstName": "Test"
    }

    SECOND_COURIER = {
        "login": "second_user2",
        "password": "123",
        "firstName": "Test"
    }

    WITHOUT_LOGIN = {
        "login": "",
        "password": "password3",
        "firstName": "NoLogin"
    }

    WITHOUT_PASSWORD = {
        "login": "NoPasswordUser",
        "password": "",
        "firstName": "NoPassword"
    }

    WITHOUT_FIRST_NAME = {
        "login": "NonameUser",
        "password": "password4",
        "firstName": ""
    }

    NO_EXIST_USER = {
        "login": "Notexist",
        "password": "password5"
    }

    INVALID_COURIER = {
        "login": "wrong_login",
        "password": "wrong_pass"
    }

class CreateOrderData:
    BASE_ORDER = {
        "firstName": "Test",
        "lastName": "Testov",
        "address": "Moscow, st. Pushkina 11",
        "metroStation": "4",
        "phone": "8 800 555 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-12-30",
        "comment": "Welcome to 7th sprint"
    }

    COLORS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        [] 
    ]

class RandomCourier:
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    

    def generate_new_courier(self):
        courier =  RandomCourier
        login = courier.generate_random_string(10)
        password = courier.generate_random_string(10)
        first_name = courier.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload
    
class ResponseText:
    NOT_FOUND = "Учетная запись не найдена"
    NO_DATA_LOGIN = "Недостаточно данных для входа"
    NO_DATA_CREATE = "Недостаточно данных для создания учетной записи"
        