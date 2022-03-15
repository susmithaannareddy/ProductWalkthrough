from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def find_ele(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return ele

    def find_all_elements(self, by_locators):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locators))
        return elements

    def waiting(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def scrolling(self, slider, width):
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(width / 2, 0).release().perform()

    def clickable(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
