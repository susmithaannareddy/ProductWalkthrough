import time

from Pages.Canditate_page import Candidate
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Config.config import TestData


class Test_Home(BaseTest):
    """"Validating Home Page"""

    def test_user_details(self):
        """take Login Page"""
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.CandidateUsername, TestData.Password)
        CandidatePage = Candidate(self.driver)
        CandidatePage.home_page_title(TestData.LoginPageTitle)

        """I am Using Boolean Value When it's Pass True else False"""
        # Verify Full-name"""
        fullname = CandidatePage.is_display_full_name()
        assert fullname == TestData.ExpectedValue
        print(fullname)

        # Verify email"""
        email = CandidatePage.is_display_email()
        assert email == TestData.ExpectedValue
        print(email)

        # Verify Phone"""
        phone = CandidatePage.is_display_phone()
        assert phone == TestData.ExpectedValue
        print(phone)

        # Verify Mobile"""
        mobile = CandidatePage.is_display_mobile()
        assert mobile == TestData.ExpectedValue
        print(mobile)

        # Verify adress"""
        address = CandidatePage.is_display_adress()
        assert address == TestData.ExpectedValue
        print(address)

        # Verify Interview name"""
        interview = CandidatePage.is_display_interview_home()
        assert interview == TestData.ExpectedValue
        print(interview)

        # Verify Interview-email"""
        interview_email = CandidatePage.is_display_interview_email_home()
        assert interview_email == TestData.ExpectedValue
        print(interview_email)

        # Verify Job-role"""
        job_role = CandidatePage.is_display_job_role_home()
        assert job_role == TestData.ExpectedValue
        print(job_role)

        # Verify Metting-ID"""
        meeting_id = CandidatePage.is_display_metting_id_home()
        assert meeting_id == TestData.ExpectedValue
        print(meeting_id)

        # Verify-Meeting-password"""
        meeting_password = CandidatePage.is_display_metting_pass_home()
        assert meeting_password == TestData.ExpectedValue
        print(meeting_password)

        # Verify-Image
        img = CandidatePage.is_display_image()
        assert img == TestData.ExpectedValue
        print(img)

        # verify-skills
        skill = CandidatePage.is_display_skill()
        assert skill == TestData.ExpectedValue
        print(skill)

        # Check Join From Here link is clickable
        CandidatePage.check_is_clickable()


