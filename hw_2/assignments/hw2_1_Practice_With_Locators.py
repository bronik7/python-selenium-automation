from hw_2.classes.AmazonMainPage import Amazon
from hw_2.classes.AmazonSignInPage import SignIn
from time import sleep


def validate_amazon_logo():
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
    amazon.close_browser()


def validate_condition_of_use_link():
    amazon = Amazon()
    amazon.open_browser_and_navigate_to_amazon_sign_in_url()
    amazon_sign_in = SignIn(amazon.driver)
    amazon_sign_in.click_get_condition_of_use_link()
    current_page = amazon.driver.current_window_handle
    new_window = None
    for handle in amazon.driver.window_handles:
        if handle != current_page:
            new_window = handle
            break
    amazon_sign_in.driver.switch_to.window(new_window)
    assert "508088" in amazon.get_current_url()  # same url as condition of privacy different reference id
    amazon.close_browser()


def validate_condition_of_privacy_link():
    amazon = Amazon()
    amazon.open_browser_and_navigate_to_amazon_sign_in_url()
    amazon_sign_in = SignIn(amazon.driver)
    amazon_sign_in.click_privacy_notice_link()
    current_page = amazon.driver.current_window_handle
    new_window = None
    for handle in amazon.driver.window_handles:
        if handle != current_page:
            new_window = handle
            break
    amazon_sign_in.driver.switch_to.window(new_window)
    assert "468496" in amazon.get_current_url()  # same url as condition of use different reference id
    amazon.close_browser()


validate_condition_of_privacy_link()
sleep(2)
validate_condition_of_use_link()
sleep(2)
validate_create_your_amazon_account()
sleep(2)
validate_need_help_forgot_password_and_other_issues()
sleep(2)
find_email_field_and_click_continue_button()
sleep(2)
validate_amazon_logo()
