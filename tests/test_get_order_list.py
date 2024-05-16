import allure
from scooter_api import OrderMethods


@allure.feature("Списки заказов")
class TestGetListOfOrder:

    @allure.title('Проверка получения списка заказов. Получаем код 200 и список (не пустой)')
    def test_get_list_of_order(self):
        orders = OrderMethods.get_list_order()
        assert orders.status_code == 200 and orders.json()["orders"] != []