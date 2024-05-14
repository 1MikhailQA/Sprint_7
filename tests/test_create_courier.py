import allure
import pytest
from helper import CourierRandom
from scooter_api import CourierMethods

@allure.title("Создание и проверка данных курьера")
class TestCreateCourier:
    @allure.description("Создание курьера с корректными данными. Получаем код 201 и сообщение 'ок':true")
    def test_create_courier_success(self, courier_data):
        create_courier = CourierMethods.create_courier(courier_data)
        assert create_courier.status_code == 201
        assert create_courier.json() == {"ok": True}

    @allure.description("Проверка невозможности создания курьера с существующим логином. Получаем ошибку 409")
    def test_cant_create_double_courier(self, create_account_courier):
        duplicate_response = CourierMethods.create_courier(create_account_courier)
        assert duplicate_response.status_code == 409
        assert duplicate_response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.description("Проверка невозможности создания курьера, когда одно из полей незаполнено. Получаем ошибку 400")
    @pytest.mark.parametrize('field', ['login', 'password' ])
    def test_create_courier_empty_field_error(self, field):

        user_data = CourierRandom.generate_random_courier_data()

        payload = user_data.copy()
        payload[field] = ""

        response = CourierMethods.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"