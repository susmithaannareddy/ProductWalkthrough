from Config.config import TestData
from Pages.InterviewerPage import InterviewerPage
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class TestInterviewer(BaseTest):

    # Login to Application and validate Interviewer Page Multi icon Button

    def test_interviewer_home_page(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.InterviewerUserName, TestData.Password)
            interviewerpage = InterviewerPage(self.driver)
            flag1 = interviewerpage.is_multitouch_button_visible()
            assert flag1 == TestData.ExpectedValue
            interviewerpage.click_multi_icon_button()
            JobOpeningsButton = interviewerpage.is_job_openings_button()
            assert JobOpeningsButton == TestData.ExpectedValue

        except:
            print(TestData.InterviewerErrorMessage)

    # Clicks on Job Openings button and validate the search button based on the specified text

    def test_job_openings_page(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.InterviewerUserName, TestData.Password)
            interviewerpage = InterviewerPage(self.driver)
            interviewerpage.click_multi_icon_button()
            JobOpeningsButton = interviewerpage.is_job_openings_button()
            assert JobOpeningsButton == TestData.ExpectedValue
            interviewerpage.click_job_openings_button()
            interviewerpage.send_keys_search_box()
            DescriptionButton = interviewerpage.click_view_description()
            assert DescriptionButton == TestData.ExpectedValue
        except:
            print(TestData.JobopeningsErrorMessage)

    # Clicks on Profile page and validates the Profile page buttons

    def test_profile_page_validation(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.InterviewerUserName, TestData.Password)
            interviewerpage = InterviewerPage(self.driver)
            interviewerpage.click_multi_icon_button()
            interviewerpage.click_profile_button()
            fullname = interviewerpage.is_profile_fullname()
            assert fullname == TestData.ExpectedValue
            email = interviewerpage.is_profile_email()
            assert email == TestData.ExpectedValue
            mobile = interviewerpage.is_profile_mobile()
            assert mobile == TestData.ExpectedValue
            availability = interviewerpage.is_profile_availability()
            assert availability == TestData.ExpectedValue
        except:
            print(TestData.ProfilePageErrorMessage)

    # Clicks on Dashboard and verifies data in the Dashboard table

    def test_dashboard_data(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.InterviewerUserName, TestData.Password)
            interviewerpage = InterviewerPage(self.driver)
            interviewerpage.click_multi_icon_button()
            interviewerpage.check_dashboard_data()
            interviewerpage.click_dashboard_link()

        except:
            print(TestData.DashboardErrorMessage)

    # Checks Interview meeting requests and validates accept, reschedule and reject buttons

    def test_interview_requests(self):
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.InterviewerUserName, TestData.Password)
            interviewerpage = InterviewerPage(self.driver)
            InterviewMeeting = interviewerpage.check_interview_meeting_requests()
            assert InterviewMeeting == TestData.ExpectedValue
            AcceptBtn = interviewerpage.is_accept_button_visible()
            assert AcceptBtn == TestData.ExpectedValue
            RejectBtn = interviewerpage.is_reject_button_visible()
            assert RejectBtn == TestData.ExpectedValue
            RescheduleBtn = interviewerpage.is_reschedule_button_visible()
            assert RescheduleBtn == TestData.ExpectedValue
        except:
            print(TestData.InterviewerErrorMessage)
