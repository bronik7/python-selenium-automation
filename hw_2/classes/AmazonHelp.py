class AmazonHelp:
    YourOrders = "//div[@class='a-column a-span9 a-span-last'][1]"

    def __init__(self, driver):
        self.driver = driver

    def your_orders_click(self):
        self.driver.find_element_by_xpath(self.YourOrders).click()