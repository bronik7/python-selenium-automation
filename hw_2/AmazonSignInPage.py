from selenium import webdriver
from selenium.webdriver.common.by import By
from hw_2.AmazonMainPage import Amazon


class SignIn:
    AmazonLogo = "//a[@class='a-link-nav-icon']"
    EmailTextField = "//input[@class='a-input-text a-span12 auth-autofocus auth-required-field']"
    ContinueButton = "//input[@class='a-button-input']"
    ErrorMessage = "//span[@class='a-list-item']"
    NeedHelpLink = "//span[@class='a-expander-prompt']"
    ForgotPassword = "//div[@class='a-expander-content a-expander-inline-content a-expander-inner a-expander-content-expanded']//a[@class='a-link-normal']"
    OtherIssues = "//div[@class='a-row a-expander-container a-expander-inline-container']//a[@id='ap-other-signin-issues-link']"
    CreateYourAmazonAccount ="//span['@class=a-button a-button-span12 a-button-base']//span['@class=a-button-inner']//a['@id=createAccountSubmit']"
    ConditionOfUseLink =  "//div[@class='a-section a-spacing-small a-text-center a-size-mini']//a[@class='a-link-normal']"
    PrivateNoticeLink = "//div[@class='a-section a-spacing-small a-text-center a-size-mini']/a[@class='a-link-normal'][2]"

    def __init__(self, driver):
        self.driver = driver

    def click_on_amazon_logo(self):
        self.driver.find_element_by_xpath(self.AmazonLogo).click()

    def enter_email_address(self, email):
        self.driver.find_element_by_xpath(self.EmailTextField).send_keys(email)

    def click_continue_button(self):
        self.driver.find_element_by_xpath(self.ContinueButton).click()

    def get_error_message(self):
        return self.driver.find_element_by_xpath(self.ErrorMessage).text

    def click_need_help_link(self):
        self.driver.find_element_by_xpath(self.NeedHelpLink).click()

    def click_create_your_amazon_account_button(self):
        self.driver.find_element_by_xpath(self.CreateYourAmazonAccount).click()

    def click_get_condition_of_use_link(self):
        self.driver.find_element_by_xpath(self.ConditionOfUseLink).click()

    def click_privacy_notice_link(self):
        self.driver.find_element_by_xpath(self.PrivateNoticeLink).click()