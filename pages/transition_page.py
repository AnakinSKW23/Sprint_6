from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class TransitionPage():

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по элементу')
    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Кликаем по логотипу')
    def click_logo(self, locator):
        self.click_button(locator)

    @allure.step('Получаем текст с элемента')
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Задаем ожидание')
    def wait_time(self, locators):
        return WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locators))
