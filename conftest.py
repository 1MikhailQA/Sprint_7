import pytest
import requests
from urls import Urls
from helper import CourierRandom


@pytest.fixture(scope='function')
def courier_data():
    return CourierRandom.generate_random_courier_data()


@pytest.fixture(scope='function')
def create_account_courier(courier_data):
    url = Urls.MAIN_PAGE_URL + Urls.CREATE_COURIER_ENDPOINT
    response = requests.post(url, json=courier_data)

    if response.status_code == 409:
        pytest.fail("Этот логин уже используется. Попробуйте другой.")

    assert response.status_code == 201

    login_url = Urls.MAIN_PAGE_URL + Urls.LOGIN_COURIER_ENDPOINT
    login_response = requests.post(login_url, json=courier_data)
    assert login_response.status_code == 200
    id_courier = login_response.json()['id']

    yield courier_data

    # Очистка
    delete_url = Urls.MAIN_PAGE_URL + Urls.CREATE_COURIER_ENDPOINT + f"/{id_courier}"
    requests.delete(delete_url)