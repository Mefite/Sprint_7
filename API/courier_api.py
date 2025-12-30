from urls import Urls

class CourierApi:
    def __init__(self, client):
        self.client = client

    def create_courier(self, courier_data):
        return self.client.post(Urls.CREATE_COURIER, json=courier_data)

    def login_courier(self, creds):
        return self.client.post(Urls.LOGIN_COURIER, json=creds)

    def delete_courier(self, courier_id):
        return self.client.delete(f"{Urls.DELETE_COURIER}/{courier_id}")