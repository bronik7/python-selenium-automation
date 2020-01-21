from hw_2.classes.AmazonMainPage import Amazon
from hw_2.classes.AmazonHelp import AmazonHelp


def logged_out_user_sees_sign_in_page_when_clicking_orders():
    amazon = Amazon()
    amazon.open_browser_and_naviate_to_amazon()
    amazon.help_from_left_menu_click()
    amazon_help = AmazonHelp(amazon.driver)
    amazon_help.help_search_text_box_search("Cancel order")
    amazon_help.go_button_click()
    assert "Cancel Items or Orders" in amazon_help.driver.find_element_by_xpath(amazon_help.CancelItemsOrOrdersLink).text
    amazon.close_browser()


logged_out_user_sees_sign_in_page_when_clicking_orders()