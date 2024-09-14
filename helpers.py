from selenium.webdriver.common.by import By


class MetroLocators():
    metro_place = (By.XPATH, "//input[@class='select-search__input']")

    @staticmethod
    def get_station_locator(metro):
        return By.XPATH, f"//*[@class='select-search__select']//*[text()='{metro}']"

