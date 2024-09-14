from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class StartLendingPage():

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по элементу')
    def click_button(self, locators):
        self.driver.find_element(*locators).click()

    @allure.step('Скроллим страницу вниз')
    def scroll_down(self, locators):
        element = self.driver.find_element(*locators)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текст с элемента')
    def get_button_text(self, locators):
        button_text = self.driver.find_element(*locators).text
        return button_text

    @allure.step('Задаем ожидание')
    def wait_time(self, locators):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locators))







