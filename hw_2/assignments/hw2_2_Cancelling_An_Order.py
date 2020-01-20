from hw_2.classes.AmazonMainPage import Amazon
from hw_2.classes.AmazonHelp import AmazonHelp


def logged_out_user_sees_sign_in_page_when_clicking_orders():
    amazon = Amazon()
    amazon.open_browser_and_naviate_to_amazon()
    amazon.help_from_left_menu_click()
    amazon_help = AmazonHelp(amazon.driver)
    amazon_help.your_orders_click()
    assert "signin" in amazon.driver.current_url
    amazon.close_browser()


logged_out_user_sees_sign_in_page_when_clicking_orders()