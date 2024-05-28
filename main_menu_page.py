from selenium.webdriver.common.by import By
from base_page import BasePage

class MainMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu_options = {
            'admin': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'),
            'pim': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'),
            'leave': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a'),
            'time': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a'),
            'recruitment': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span'),
            'myinfo': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a'),
            'performance': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a'),
            'dashboard': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a'),
            'directory': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a'),
            'maintenance': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a'),
            'claim': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a'),
            'buzz': (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a'),
        }

    def verify_menu_options(self):
        for option_name, locator in self.menu_options.items():
            element = self.find_element(*locator)
            assert element.is_displayed(), f"{option_name} menu option is not displayed"
        print("All the Main Menu Options have been Tested Successfully!")
