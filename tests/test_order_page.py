from pages.order_page import OrderPage
from src.data import ButtonStatus
from src.locators import OrderPageLocators
import allure
@allure.suite('Тестируем заказ самоката')
class TestOrderPage():

    @allure.title('Создаем заказ через верхнюю кнопку "Заказать" с данными пользователя №1')
    def test_perform_order_user_1(self, driver):
        self.order_page = OrderPage(driver)
        self.order_page.accept_cookie(OrderPageLocators.accept_cookie)
        self.order_page.click_button(OrderPageLocators.upper_order_button)
        self.order_page.confirm_order_user_1(OrderPageLocators.confirm_order, OrderPageLocators.accept_order)
        assert self.order_page.get_text_from_status_button(OrderPageLocators.status_button_text) == ButtonStatus.look_at_status

    @allure.title('Создаем заказ через нижнюю кнопку "Заказать" с данными пользователя №2')
    def test_perform_order_user_2(self, driver):
        self.order_page = OrderPage(driver)
        self.order_page.accept_cookie(OrderPageLocators.accept_cookie)
        self.order_page.click_button(OrderPageLocators.down_order_button)
        self.order_page.confirm_order_user_2(OrderPageLocators.confirm_order, OrderPageLocators.accept_order)
        assert self.order_page.get_text_from_status_button(OrderPageLocators.status_button_text) == ButtonStatus.look_at_status

