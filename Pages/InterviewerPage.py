from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class InterviewerPage(BasePage):
    MultitouchButton = (By.XPATH, "/html/body/div/div/div/div[1]/header/div/button[1]/span[1]")
    JobOpenings = (By.XPATH, "//span[text()='Job Openings']")
    SearchText = (By.XPATH, "//input[@type='text']")
    JobDescription = (By.XPATH, "//span[text()='View Job Description’]")
    searchtext = (By.XPATH, "//input[@type='text']")
    SearchButton = (By.XPATH, "//div[@class='MuiInputAdornment-root MuiInputAdornment-positionStart']//button["
                              "@type='button']")
    ViewDescription = (By.XPATH, "//span[text()='View Job Description']")
    DashboardButton = (By.XPATH, "// span[text() = 'Dashboard']")
    DashboardZoomLink = (By.XPATH, "//a[text()='https://us04web.zoom.us/j/71130964632?pwd=79tqnZkszAl0x70pX5hgjkK3SPHJ45.1']")
    ProfileButton = (By.XPATH, "//span[text()='Profile']")
    ProfileFullName = (By.XPATH, "//h6[text()='Full Name']")
    ProfileEmail = (By.XPATH, "//h6[text()='Email']")
    ProfileMobile = (By.XPATH, "//h6[text()='Mobile']")
    ProfileAvailability = (By.XPATH, "//h6[text()='Availability']")
    ProfileEverydayButton = (By.XPATH, "//input[@value='everyday']")
    ProfileMonWedFri = (By.XPATH, "//span[text()='Mon-Wed-Fri']")
    ProfileTueThurSat = (By.XPATH, "//span[text()='Tue-Thu-Sat']")
    DashboardTableData = (By.XPATH, "//tbody[@class='MuiTableBody-root']")
    InterviewMeetingRequests = (By.XPATH, "//h4[text()='Interview Meeting Requests']")
    AcceptButton = (By.XPATH, "//span[text()='Accept']")
    RescheduleButton = (By.XPATH, "//span[text()='Reschedule']")
    RejectButton = (By.XPATH, "//span[text()='Reject']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_multitouch_button_visible(self):
        return self.is_visible(self.MultitouchButton)

    def click_multi_icon_button(self):
        return self.do_click(self.MultitouchButton)

    def is_job_openings_button(self):
        return self.is_visible(self.JobOpenings)

    def click_job_openings_button(self):
        return self.do_click(self.JobOpenings)

    def click_dashboard_link(self):
        return self.do_click(self.DashboardZoomLink)

    def send_keys_search_box(self):
        self.do_send_keys(self.searchtext, "SDET2")
        self.do_click(self.SearchButton)

    def click_view_description(self):
        return self.is_visible(self.ViewDescription)

    def click_profile_button(self):
        return self.do_click(self.ProfileButton)

    def is_profile_fullname(self):
        return self.is_visible(self.ProfileFullName)

    def is_profile_email(self):
        return self.is_visible(self.ProfileEmail)

    def is_profile_mobile(self):
        return self.is_visible(self.ProfileMobile)

    def is_profile_availability(self):
        return self.is_visible(self.ProfileAvailability)

    def check_dashboard_data(self):
        return self.find_all_elements(self.DashboardTableData)

    def check_interview_meeting_requests(self):
        return self.is_visible(self.InterviewMeetingRequests)

    def is_accept_button_visible(self):
        return self.is_visible(self.AcceptButton)

    def is_reject_button_visible(self):
        return self.is_visible(self.RejectButton)

    def is_reschedule_button_visible(self):
        return self.is_visible(self.RescheduleButton)


