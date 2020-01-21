class AmazonHelp:
    YourOrders = "//div[@class='a-column a-span9 a-span-last'][1]"
    HelpSearchTextBox = "//form[@id='search-help']//input[@class='a-input-text a-span12']"
    GoButton = "//form[@id='search-help']//input[@class='a-button-input']"
    CancelItemsOrOrdersLink = "//body[@class='a-meter-animate']//div[@class='cs-help-v4']//a[@class='a-link-normal'][1]"

    def __init__(self, driver):
        self.driver = driver

    def your_orders_click(self):
        self.driver.find_element_by_xpath(self.YourOrders).click()

    def help_search_text_box_search(self, text):
        x = self.driver.find_element_by_xpath(self.HelpSearchTextBox)
        self.driver.find_element_by_xpath(self.HelpSearchTextBox).send_keys(text)

    def go_button_click(self):
        self.driver.find_element_by_xpath(self.GoButton).click()
