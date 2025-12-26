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
        "password": "password3",
        "firstName": "NoLogin"
    }

    WITHOUT_PASSWORD = {
        "login": "NoPassUser",
        "firstName": "NoPassword"
    }

    WITHOUT_FIRST_NAME = {
        "login": "Noname",
        "password": "password4"
    }

    NO_EXIST_USER = {
        "login": "Nonexist",
        "password": "password5"
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