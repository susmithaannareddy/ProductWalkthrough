import pytest
from selenium import webdriver

from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.Chrome_Executable_Path)
        request.cls.driver = web_driver
    # yield
    # web_driver.close()
