import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class TestLogin(BaseTest):

    def test_signin_button_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signin_button_exist()
        print(flag)
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LoginPageTitle)
        assert title == TestData.LoginPageTitle

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.UserName, TestData.Password)





