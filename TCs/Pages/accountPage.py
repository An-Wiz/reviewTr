from TCs.Locators.locators import Locators


class AccountPage():

    def __init__(self, driver):
        self.driver = driver
        self.signout_link_xpath = Locators.signout_link_xpath
        self.account_header_xpath = Locators.account_header_xpath

    #Click 'Sign Out' link method
    def click_signout(self):
        self.driver.find_element_by_xpath(self.signout_link_xpath).click()

    #Method returns the text of the header on the Account page
    def account_header_text(self):
        header = self.driver.find_element_by_xpath(self.account_header_xpath).text
        return header

