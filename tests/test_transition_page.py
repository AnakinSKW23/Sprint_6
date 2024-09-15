from pages.transition_page import TransitionPage
from src.data import UrlElements
<<<<<<< HEAD
=======
from conftest import driver
>>>>>>> 1b9ee898ee275ba8504827e2f3c51379949d1305
from src.locators import TransitionPageLocators
import allure

@allure.suite('Тестируем переход на страницы по клику на логотип')
class TestTransition():

    @allure.title('Тестируем переход на страницу "Дзен" при клике на логотип "Яндекс"')
    def test_yandex_logo(self, driver):
<<<<<<< HEAD
        self.transition_page = TransitionPage(driver)
        self.transition_page.click_logo(TransitionPageLocators.yandex_logo)
        new_window = self.transition_page.driver.window_handles[1]
        self.transition_page.driver.switch_to.window(new_window)
        self.transition_page.wait_time(TransitionPageLocators.button_find_in_dzen)
        assert self.transition_page.get_text_from_element(TransitionPageLocators.button_find_in_dzen) == UrlElements.dzen_page_text

    @allure.title('Тестируем переход на страницу "Яндекс Самокат" при клике на логотип "Самокат"')
    def test_scooter_logo(self, driver):
        self.transition_page = TransitionPage(driver)
        self.transition_page.click_button(TransitionPageLocators.upper_order_button)
        self.transition_page.click_logo(TransitionPageLocators.scooter_logo)
        assert self.transition_page.get_text_from_element(TransitionPageLocators.text_on_start_page) == UrlElements.yandex_page_text
=======
        self.button = TransitionPage(driver)
        self.button.click_logo(TransitionPageLocators.yandex_logo)
        new_window = self.button.driver.window_handles[1]
        self.button.driver.switch_to.window(new_window)
        self.button.wait_time(TransitionPageLocators.button_find_in_dzen)
        assert self.button.get_text_from_element(TransitionPageLocators.button_find_in_dzen) == UrlElements.dzen_page_text

    @allure.title('Тестируем переход на страницу "Яндекс Самокат" при клике на логотип "Самокат"')
    def test_scooter_logo(self, driver):
        self.button = TransitionPage(driver)
        self.button.click_button(TransitionPageLocators.upper_order_button)
        self.button.click_logo(TransitionPageLocators.scooter_logo)
        assert self.button.get_text_from_element(TransitionPageLocators.text_on_start_page) == UrlElements.yandex_page_text
>>>>>>> 1b9ee898ee275ba8504827e2f3c51379949d1305

