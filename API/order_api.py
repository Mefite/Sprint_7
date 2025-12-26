from urls import Urls

class OrderApi:
    def __init__(self, client):
        self.client = client

    def create_order(self, data):
        return self.client.post(Urls.CREATE_ORDER, json=data)

    def get_order_list(self, params=None):
        return self.client.get(Urls.LIST_ORDERS,  params=params)
