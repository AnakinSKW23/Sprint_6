from pages.transition_page import TransitionPage
from src.data import UrlElements
from conftest import driver
from src.locators import TransitionPageLocators
import allure

@allure.suite('Тестируем переход на страницы по клику на логотип')
class TestTransition():

    @allure.title('Тестируем переход на страницу "Дзен" при клике на логотип "Яндекс"')
    def test_yandex_logo(self, driver):
        self.button = TransitionPage(driver)
        self.button.click_logo(TransitionPageLocators.yandex_logo)
        new_window = self.button.driver.window_handles[1]
        self.button.driver.switch_to.window(new_window)
        self.button.wait_time(TransitionPageLocators.button_find_in_dzen)
        assert self.button.get_text_from_element(TransitionPageLocators.button_find_in_dzen) == UrlElements.dzen_page_text

    @allure.title('Тестируем переход на страницу "Дзен" при клике на логотип "Самокат"')
    def test_scooter_logo(self, driver):
        self.button = TransitionPage(driver)
        self.button.click_button(TransitionPageLocators.upper_order_button)
        self.button.click_logo(TransitionPageLocators.scooter_logo)
        assert self.button.get_text_from_element(TransitionPageLocators.text_on_start_page) == UrlElements.yandex_page_text

