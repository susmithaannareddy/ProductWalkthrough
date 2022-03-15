from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class Candidate(BasePage):
    """Home Page Locators fetch to test_Candidate_page"""
    full_name = (By.XPATH, "//div[text()='GirishKumar']")
    email = (By.XPATH, "//div[text()='girish@gmail.com']")
    phone = (By.XPATH, "//div[text()='(239) 816-9029']")
    mobile = (By.XPATH, "//div[text()='(320) 380-4539']")
    adress = (By.XPATH, "//div[text()='Bay Area, San Francisco, CA']")
    interview_name = (By.XPATH, "//p[text()='testtest']")
    interview_email = (By.XPATH, "//p[text()='Test12@gmail.com']")
    job_role = (By.XPATH, "//p[text()='QA 3']")
    meeting_id = (By.XPATH, "//p[text()='72965670754']")
    meeting_pass = (By.XPATH, "//p[text()='pT5RiG']")
    Zoomlink = (By.XPATH, "//a[@class='button-join-now']")
    image = (By.XPATH, "//img[@class='rounded-circle']")
    skills = (By.XPATH, "//span[text()='Django']")
    JoinFromHereLink = (By.XPATH, "//span[text()='Join from here']")

    """I am Using Boolean Value When it's Pass True else False"""

    def __init__(self, driver):  # Super class
        super().__init__(driver)

    # Home Page title
    def home_page_title(self, title):
        return self.get_title(title)

    # Checking Full_name
    def is_display_full_name(self):
        return self.is_visible(self.full_name)

    # Home page email
    def is_display_email(self):
        return self.is_visible(self.email)

    # home phone number(tax)
    def is_display_phone(self):
        return self.is_visible(self.phone)

    # home mobile number
    def is_display_mobile(self):
        return self.is_visible(self.mobile)

    # home address
    def is_display_adress(self):
        return self.is_visible(self.adress)

    # Interviewer Name
    def is_display_interview_home(self):
        return self.is_visible(self.interview_name)

    # interview email
    def is_display_interview_email_home(self):
        return self.is_visible(self.interview_email)

    # Job-role
    def is_display_job_role_home(self):
        return self.is_visible(self.job_role)

    # Meeting id interview
    def is_display_metting_id_home(self):
        return self.is_visible(self.meeting_id)

    # meeting Password
    def is_display_metting_pass_home(self):
        return self.is_visible(self.meeting_pass)

    # Image will display
    def is_display_image(self):
        return self.is_visible(self.image)

    # Primary Skills
    def is_display_skill(self):
        return self.is_visible(self.skills)

    # checks element is clickable
    def check_is_clickable(self):
        try:
            self.clickable(self.JoinFromHereLink)
            return self.do_click(self.JoinFromHereLink)
        except:
            print("Click Failed")
