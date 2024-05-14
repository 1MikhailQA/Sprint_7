import allure
import pytest
from helper import CourierRandom
from scooter_api import CourierMethods


@allure.title("Логин курьера")
class TestLoginCourier:
    @allure.description("Проверка успешного логина курьера.")
    def test_login_courier_success(self, create_account_courier):
        login_courier = CourierMethods.create_and_login_courier(create_account_courier)
        assert login_courier.status_code == 200 and login_courier.json()['id'] != 0

    @allure.title('Проверка,на наличие полей логина или пароля, если отсутсвуют запрос возвращает ошибку 400')
    @pytest.mark.parametrize('field_key, field_value', [('login', ''), ('password', '')])
    def test_login_courier_empty_field_error(self, field_key, field_value):
        user_data = CourierRandom.generate_random_courier_data()
        payload = user_data.copy()
        payload[field_key] = field_value
        response = CourierMethods.create_and_login_courier(payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    @allure.description('Проверка невозможности залогиниться с несуществующим аккаунтом.')
    def test_no_such_login(self):
        user_data = CourierRandom.generate_random_courier_data()
        response = CourierMethods.login_courier(user_data)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'