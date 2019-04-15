from TCs.Locators.locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_id = Locators.email_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.signin_button_xpath = Locators.signin_button_xpath
        self.error_message_xpath = Locators.error_message_xpath

    #Enter email address in to the email field method
    def fillout_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    #Enter password in to the password field method
    def fillout_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    #Click 'Sign In' button method
    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()

    #Method returns True when the error message 'Invalid Login Or Password' is present
    def error_message_is_present(self):
        error_message_is_present = self.driver.find_element_by_xpath(self.error_message_xpath).is_displayed()
        return error_message_is_present



