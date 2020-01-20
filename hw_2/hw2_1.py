from hw_2.AmazonMainPage import Amazon
from hw_2.AmazonSignInPage import SignIn
from time import sleep


def find_amazon_logo():
    amazon = Amazon()
    amazon.open_browser_and_navigate_to_amazon_sign_in_url()
    amazon_sign_in = SignIn(amazon.driver)
    amazon_sign_in.click_on_amazon_logo()
    assert amazon.get_current_url() == "https://www.amazon.com/ref=ap_frn_logo"
    amazon.close_browser()


def find_email_field_and_click_continue_button():
    amazon = Amazon()
    amazon.open_browser_and_navigate_to_amazon_sign_in_url()
    amazon_sign_in = SignIn(amazon.driver)
    amazon_sign_in.enter_email_address("fakeemail")
    amazon_sign_in.click_continue_button()
    assert amazon_sign_in.get_error_message() == "We cannot find an account with that email address"
    amazon.close_browser()


def validate_need_help_forgot_password_and_other_issues():
    amazon = Amazon()
    amazon.open_browser_and_navigate_to_amazon_sign_in_url()
    amazon_sign_in = SignIn(amazon.driver)
    amazon_sign_in.click_need_help_link()
    assert amazon_sign_in.driver.find_element_by_xpath(amazon_sign_in.ForgotPassword).text == "Forgot your password?"
    assert amazon_sign_in.driver.find_element_by_xpath(amazon_sign_in.OtherIssues).text == "Other issues with Sign-In"
    amazon.close_browser()


def validate_create_your_amazon_account():
    amazon = Amazon()
    amazon.open_browser_and_navigate_to_amazon_sign_in_url()
    amazon_sign_in = SignIn(amazon.driver)
    amazon_sign_in.click_create_your_amazon_account_button()
    assert "register" in amazon.get_current_url()


validate_create_your_amazon_account()
sleep(2)
# validate_need_help_forgot_password_and_other_issues()
# sleep(2)
# find_email_field_and_click_continue_button()
# sleep(2)
# find_amazon_logo()
