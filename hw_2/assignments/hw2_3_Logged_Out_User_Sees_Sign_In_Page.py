from hw_2.classes.AmazonMainPage import Amazon
from hw_2.classes.AmazonHelp import AmazonHelp


def canceling_an_order():
    amazon = Amazon()
    amazon.open_browser_and_naviate_to_amazon()
    amazon.help_from_left_menu_click()
    amazon_help = AmazonHelp(amazon.driver)
    assert "Edit or cancel orders" in amazon_help.driver.find_element_by_xpath(amazon_help.YourOrders).text
    amazon.close_browser()

canceling_an_order()