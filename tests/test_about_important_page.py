import pytest
<<<<<<< HEAD
from pages.about_important_page import AboutImportantPage
from src.data import Answers
from src.locators import StartPageLocators
=======
from pages.about_important_page import StartLendingPage
from src.data import Answers
from src.locators import StartPageLocators
from conftest import driver
>>>>>>> 1b9ee898ee275ba8504827e2f3c51379949d1305
import allure
@allure.suite('Тестируем раздел "Вопросы о важном"')
class TestQuestionsAboutImportant():

    @allure.title('Проверяем ответы в разделе "Вопросы о важном"')
    @pytest.mark.parametrize(
        'locator, question, answer',
        [
            (StartPageLocators.how_much_cost, StartPageLocators.how_much_cost_text, Answers.how_much_cost_answer),
            (StartPageLocators.want_several_scooters, StartPageLocators.want_several_scooters_text, Answers.want_several_scooters_answer),
            (StartPageLocators.how_calculate_rent_time, StartPageLocators.how_calculate_rent_time_text, Answers.how_calculate_rent_time_answer),
            (StartPageLocators.order_scooter_today, StartPageLocators.order_scooter_today_text, Answers.order_scooter_today_answer),
            (StartPageLocators.extend_the_order, StartPageLocators.extend_the_order_text, Answers.extend_the_order_answer),
            (StartPageLocators.charging_scooter, StartPageLocators.charging_scooter_text, Answers.charging_scooter_answer),
            (StartPageLocators.cancel_order, StartPageLocators.cancel_order_text, Answers.cancel_order_answer),
            (StartPageLocators.moscow_ring_road, StartPageLocators.moscow_ring_road_text, Answers.moscow_ring_road_answer),
        ]
    )
    def test_question_answer(self, driver, locator, question, answer):
<<<<<<< HEAD
        self.about_important_page = AboutImportantPage(driver)
        self.about_important_page.scroll_down(StartPageLocators.moscow_ring_road)
        self.about_important_page.click_button(locator)
        self.answer = answer
        self.about_important_page.wait_time(question)
        assert self.about_important_page.get_button_text(question) == self.answer
=======
        self.button = StartLendingPage(driver)
        self.button.scroll_down(StartPageLocators.moscow_ring_road)
        self.button.click_button(locator)
        self.answer = answer
        self.button.wait_time(question)
        assert self.button.get_button_text(question) == self.answer
>>>>>>> 1b9ee898ee275ba8504827e2f3c51379949d1305

