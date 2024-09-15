from selenium.webdriver.common.by import By

class MetroLocators():
    @staticmethod
    def get_station_locator(metro):
        return By.XPATH, f"//*[@class='select-search__select']//*[text()='{metro}']"