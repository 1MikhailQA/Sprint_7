import requests
import allure
from urls import Urls


class CourierMethods:
    @staticmethod
    @allure.step("Создание нового курьера")
    def create_courier(payload):
        url = Urls.MAIN_PAGE_URL + Urls.CREATE_COURIER_ENDPOINT
        response = requests.post(url, json=payload)
        return response

    @staticmethod
    @allure.step("Создание курьера c одинаковыми данными")
    def duplicate_create_courier(payload):
        requests.post(Urls.MAIN_PAGE_URL + Urls.CREATE_COURIER_ENDPOINT, data=payload)
        response_two = requests.post(Urls.MAIN_PAGE_URL + Urls.CREATE_COURIER_ENDPOINT, data=payload)
        return response_two

    @staticmethod
    @allure.step("Создание и Логин курьера в системе")
    def create_and_login_courier(payload):
        requests.post(Urls.MAIN_PAGE_URL + Urls.CREATE_COURIER_ENDPOINT, data=payload)
        response = requests.post(Urls.MAIN_PAGE_URL + Urls.LOGIN_COURIER_ENDPOINT, data=payload)
        return response

    @staticmethod
    @allure.step("Логин курьера")
    def login_courier(payload):
        response = requests.post(Urls.MAIN_PAGE_URL + Urls.LOGIN_COURIER_ENDPOINT, data=payload)
        return response


class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        response = requests.post(Urls.MAIN_PAGE_URL + Urls.ORDER_ENDPOINT, data=payload)
        return response

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_list_order():
        response = requests.get(Urls.MAIN_PAGE_URL + Urls.ORDER_ENDPOINT)
        return response

