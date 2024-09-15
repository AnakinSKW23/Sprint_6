from src.locators import OrderPageLocators
from src.data import UserInfo_1, UserInfo_2
from helpers import MetroLocators
import allure

class OrderPage():

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по элементу')
    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Принимаем куки')
    def accept_cookie(self, locator):
        self.click_button(locator)

    @allure.step('Вводим текст')
    def set_text_to_element(self, locators, text):
        self.driver.find_element(*locators).send_keys(text)

    @allure.step('Вводим текст в поле "Имя"')
    def set_name_field(self, locator, name):
        self.driver.find_element(*locator).send_keys(name)

    @allure.step('Вводим текст в поле "Фамилия"')
    def set_surname_field(self, locator, surname):
        self.driver.find_element(*locator).send_keys(surname)

    @allure.step('Вводим текст в поле "Адрес"')
    def set_address_field(self, locator, address):
        self.driver.find_element(*locator).send_keys(address)

    @allure.step('Выбираем станцию метро')
    def set_metro(self, locator, metro_place):
        self.set_text_to_element(locator, metro_place)
        self.driver.find_element(*MetroLocators.get_station_locator(metro_place)).click()

    @allure.step('Вводим номер телефона')
    def set_phone(self, locator, phone):
        self.driver.find_element(*locator).send_keys(phone)

    @allure.step('Выбираем дату когда привезти самокат')
    def set_when_to_bring_date(self, locator, locator_date):
        self.click_button(locator)
        self.click_button(locator_date)

    @allure.step('Нажимаем на кнопку "Да" в форме подтверждения заказа')
    def accept_order(self, locator):
        self.click_button(locator)

    @allure.step('Выбираем срок аренды')
    def set_rent_time(self, locator, locator_day):
        self.click_button(locator)
        self.click_button(locator_day)

    @allure.step('Выбираем цвет самоката')
    def set_color_scooter(self, locator):
        self.click_button(locator)

    @allure.step('Выбираем текст в поле "Комментарий для курьера')
    def add_comment_to_courier(self, locator, text):
        self.set_text_to_element(locator, text)

    @allure.step('Нажимаем кнопку "Заказ" на странице "Про аренду"')
    def set_confirm_order(self, locator):
        self.click_button(locator)

    @allure.step('Получем текст с элемента')
    def get_text_from_status_button(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Заполняем все данные пользователя №1')
    def add_user_info_1(self):
        self.set_name_field(OrderPageLocators.name_field, UserInfo_1.name)
        self.set_surname_field(OrderPageLocators.surname_field, UserInfo_1.surname)
        self.set_address_field(OrderPageLocators.address_field, UserInfo_1.address)
        self.set_metro(OrderPageLocators.metro, UserInfo_1.metro)
        self.set_phone(OrderPageLocators.phone, UserInfo_1.phone)
        self.click_button(OrderPageLocators.next_button)

    @allure.step('Заполняем информацию об аренде пользователя №1')
    def about_rent_user_1(self):
        self.set_when_to_bring_date(OrderPageLocators.when_to_bring, OrderPageLocators.rent_date)
        self.set_rent_time(OrderPageLocators.rent_time, OrderPageLocators.four_days_rent)
        self.set_color_scooter(OrderPageLocators.black_scooter)
        self.add_comment_to_courier(OrderPageLocators.comment_to_courier, UserInfo_1.comment)

    @allure.step('Создаем заказ с данными и информацией об аренде пользователя №1')
    def confirm_order_user_1(self, locator_1, locator_2):
        self.add_user_info_1()
        self.about_rent_user_1()
        self.set_confirm_order(locator_1)
        self.accept_order(locator_2)

    @allure.step('Заполняем все данные пользователя №2')
    def add_user_info_2(self):
        self.set_name_field(OrderPageLocators.name_field, UserInfo_2.name)
        self.set_surname_field(OrderPageLocators.surname_field, UserInfo_2.surname)
        self.set_address_field(OrderPageLocators.address_field, UserInfo_2.address)
        self.set_metro(OrderPageLocators.metro, UserInfo_2.metro)
        self.set_phone(OrderPageLocators.phone, UserInfo_2.phone)
        self.click_button(OrderPageLocators.next_button)

    @allure.step('Заполняем информацию об аренде пользователя №2')
    def about_rent_user_2(self):
        self.set_when_to_bring_date(OrderPageLocators.when_to_bring, OrderPageLocators.rent_date_next)
        self.set_rent_time(OrderPageLocators.rent_time, OrderPageLocators.three_days_rent)
        self.set_color_scooter(OrderPageLocators.grey_scooter)
        self.add_comment_to_courier(OrderPageLocators.comment_to_courier, UserInfo_2.comment)

    @allure.step('Создаем заказ с данными и информацией об аренде пользователя №2')
    def confirm_order_user_2(self, locator_confirm, locator_accept):
        self.add_user_info_2()
        self.about_rent_user_2()
        self.set_confirm_order(locator_confirm)
        self.accept_order(locator_accept)
