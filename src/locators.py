from selenium.webdriver.common.by import By

class StartPageLocators():

    how_much_cost = (By.ID, 'accordion__heading-0')
    want_several_scooters = (By.ID, 'accordion__heading-1')
    how_calculate_rent_time = (By.ID, 'accordion__heading-2')
    order_scooter_today = (By.ID, 'accordion__heading-3')
    extend_the_order = (By.ID, 'accordion__heading-4')
    charging_scooter = (By.ID, 'accordion__heading-5')
    cancel_order = (By.ID, 'accordion__heading-6')
    moscow_ring_road = (By.ID, 'accordion__heading-7')
    how_much_cost_text = (By.XPATH, ".//div[@id='accordion__panel-0']")
    want_several_scooters_text = (By.XPATH, ".//div[@id='accordion__panel-1']")
    how_calculate_rent_time_text = (By.XPATH, ".//div[@id='accordion__panel-2']")
    order_scooter_today_text = (By.XPATH, ".//div[@id='accordion__panel-3']")
    extend_the_order_text = (By.XPATH, ".//div[@id='accordion__panel-4']")
    charging_scooter_text = (By.XPATH, ".//div[@id='accordion__panel-5']")
    cancel_order_text = (By.XPATH, ".//div[@id='accordion__panel-6']")
    moscow_ring_road_text = (By.XPATH, ".//div[@id='accordion__panel-7']")


class OrderPageLocators():
    upper_order_button = (By.XPATH, ".//div[2]/button[1]")
    down_order_button = (By.XPATH, ".//div[5]/button")
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, ".//button[text()='Далее']")
    when_to_bring = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    rent_date = (By.XPATH, ".//div[text()='20']")
    rent_date_next = (By.XPATH, ".//div[text()='27']")
    rent_time = (By.XPATH, ".//div[text()='* Срок аренды']")
    three_days_rent = (By.XPATH, ".//div[text()='трое суток']")
    four_days_rent = (By.XPATH, ".//div[text()='четверо суток']")
    black_scooter = (By.XPATH, ".//input[@id='black']")
    grey_scooter = (By.XPATH, ".//input[@id='grey']")
    comment_to_courier = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    confirm_order = (By.XPATH, ".//div[3]/button[2]")
    accept_order = (By.XPATH, ".//button[text()='Да']")
    status_button_text = (By.XPATH, ".//button[text()='Посмотреть статус']")
    accept_cookie = (By.XPATH, ".//button[text()='да все привыкли']")
    metro_place = (By.XPATH, "//input[@class='select-search__input']")

class TransitionPageLocators():
    button_find_in_dzen = (By.XPATH, ".//button[text()='Найти']")
    text_on_start_page = (By.XPATH, ".//div[text()='Заказываете самокат']")
    upper_order_button = (By.XPATH, ".//div[2]/button[1]")
    scooter_logo = (By.XPATH, ".//img[@alt='Scooter']")
    yandex_logo = (By.XPATH, ".//img[@alt='Yandex']")

