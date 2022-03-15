import time

import pytest
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.RecruiterPage import RecruiterPage


class Test_RecruiterPage(BaseTest):

    def test_login(self):
        self.loginpage = RecruiterPage(self.driver)
        self.loginpage.Login(TestData.RecruiterUsername, TestData.Password)

    def test_create_new_job(self):
        self.createnewjob = RecruiterPage(self.driver)
        self.createnewjob.CreateNewJob()

    def test_assign_job(self):
        self.assignjob = RecruiterPage(self.driver)
        self.assignjob.AssignJob()

    def test_schedule_interview(self):
        self.scheduleinterview = RecruiterPage(self.driver)
        self.scheduleinterview.ScheduleInterview()

    def test_dashboard(self):
        self.dashboard = RecruiterPage(self.driver)
        self.dashboard.Dashboard()

    def test_Jobopenings(self):
        self.jobopenings = RecruiterPage(self.driver)
        self.jobopenings.Job_openings()
        