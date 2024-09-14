from pages.order_page import OrderPage
from src.data import ButtonStatus
from src.locators import OrderPageLocators
from conftest import driver
import allure

@allure.suite('Тестируем заказ самоката')
class TestOrderPage():

    @allure.title('Создаем заказ через верхнюю кнопку "Заказать" с данными пользователя №1')
    def test_perform_order_user_1(self, driver):
        self.button = OrderPage(driver)
        self.button.accept_cookie(OrderPageLocators.accept_cookie)
        self.button.click_button(OrderPageLocators.upper_order_button)
        self.button.add_full_user_info_1()
        assert self.button.get_text_from_status_button(OrderPageLocators.status_button_text) == ButtonStatus.look_at_status

    @allure.title('Создаем заказ через нижнюю кнопку "Заказать" с данными пользователя №2')
    def test_perform_order_user_2(self, driver):
        self.button = OrderPage(driver)
        self.button.accept_cookie(OrderPageLocators.accept_cookie)
        self.button.click_button(OrderPageLocators.down_order_button)
        self.button.add_full_user_info_2()
        assert self.button.get_text_from_status_button(OrderPageLocators.status_button_text) == ButtonStatus.look_at_status
