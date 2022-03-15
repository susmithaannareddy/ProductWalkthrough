from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    Emailadress = (By.XPATH, "//input[@id='email']")
    Password = (By.XPATH, "//input[@id='password']")
    SignIn = (By.XPATH, "//span[text()='Sign In']")

    # Constructor of the Page class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_Url)

    # Method to get page of the title
    def get_login_page_title(self, title):
        return self.get_title(title)

    # Method to check the Signin Button
    def is_signin_button_exist(self):
        return self.is_visible(self.SignIn)

    def do_login(self, usrname, pswd):
        self.waiting()
        self.do_send_keys(self.Emailadress, usrname)
        self.do_send_keys(self.Password, pswd)
        self.do_click(self.SignIn)


