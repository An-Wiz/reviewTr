from selenium import webdriver
import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from TCs.Pages.homePage import HomePage
from TCs.Pages.loginPage import LoginPage
from TCs.Pages.accountPage import AccountPage
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        #self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.gouletpens.com")

        home = HomePage(self.driver)
        home.click_signin()

    def test_login_valid(self):

        login = LoginPage(self.driver)
        login.fillout_email("t.tester@testmail.com")
        login.fillout_password("P@$$word")
        login.click_signin()

        account = AccountPage(self.driver)
        self.assertEqual(account.account_header_text(), 'My Account', "pass")
        account.click_signout()

    def test_validemail_invalidpassword(self):

        login = LoginPage(self.driver)
        login.fillout_email("t.tester@testmail.com")
        login.fillout_password("password")
        login.click_signin()
        self.assertTrue(login.error_message_is_present())

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()