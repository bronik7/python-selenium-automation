from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Amazon:
    SignInPopUpButton = "//*[@id='nav-signin-tooltip']/a/span"
    URL = "http://www.amazon.com"
    NavigationMenuButton ="//a[@id='nav-hamburger-menu']"
    HelpFromNavigationMenu = "//div[@id='hmenu-canvas']//div[@id='hmenu-content']//ul[@class='hmenu  hmenu-visible']/li[45]"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_browser_and_naviate_to_amazon(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)

    def open_browser_and_navigate_to_amazon_sign_in_url(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)

        def click_on_sign_in_button():
            sign_in_button = self.driver.find_element_by_xpath(self.SignInPopUpButton)
            sign_in_button.click()

        click_on_sign_in_button()

    def get_current_url(self):
        return self.driver.current_url

    def help_from_left_menu_click(self):
        self.driver.find_element_by_xpath(self.NavigationMenuButton).click()
        v = self.driver.find_element_by_xpath(self.HelpFromNavigationMenu)
        self.driver.find_element_by_xpath(self.HelpFromNavigationMenu).click()

    def close_browser(self):
        self.driver.quit()