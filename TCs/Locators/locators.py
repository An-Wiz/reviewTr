class Locators():

    #Home page objects
    signin_link_classname = "header__account-nav-link--account"

    #Login page objects
    email_textbox_id = "CustomerEmail"
    password_textbox_id = "CustomerPassword"
    signin_button_xpath = "//*[@id='customer_login']/ul/li[3]/button"
    error_message_xpath = "//*[@id='customer_login']/div/ul/li/text()"

    #Account page objects
    signout_link_xpath = "//li[contains(@class,'signout')]/a"
    account_header_xpath = "//h1"
