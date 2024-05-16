import allure
import pytest
from helper import DataGenerationOrder
from scooter_api import OrderMethods


@allure.feature("Создание заказа и выбор любого цвета")
class TestOrders:
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    @allure.title('Проверка, что можно создать заказ с указанием любого цвета')
    def test_create_order_with_color(self, color):
        order_data = DataGenerationOrder.generate_order_data(color)
        response = OrderMethods.create_order(order_data)
        assert response.status_code == 201 and response.json()['track'] != 0