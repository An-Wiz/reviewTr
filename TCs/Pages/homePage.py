from TCs.Locators.locators import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.signin_link_classname = Locators.signin_link_classname

    def click_signin(self):
        self.driver.find_element_by_class_name(self.signin_link_classname).click()
