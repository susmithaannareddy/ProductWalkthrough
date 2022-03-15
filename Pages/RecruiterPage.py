import time

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Config.config import TestData
from Pages.BasePage import BasePage


class RecruiterPage(BasePage):
    email = (By.ID, 'email')
    password = (By.ID, 'password')
    login = (By.XPATH, '//span[@class="MuiButton-label"]')
    MenuBar = By.XPATH, '//*[@id="root"]/div/div/div[1]/header/div/button[1]/span[1]'
    Create_NewJob = (By.LINK_TEXT, 'Create new Job')
    Role = (By.ID, 'job-title-input')
    Band_sel = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/form/div/div[3]/div/div')
    Band = (By.XPATH, "//li[contains(text(),'B8')]")
    Designation_sel = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/form/div/div[5]/div/div')
    Designation = (By.XPATH, "//li[contains(text(),'Senior Software Developer')]")
    Skill_Data = (By.XPATH, '//input[@class="e-dropdownbase"]')
    Location_sel = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/form/div/div[7]/div/div')
    Location = (By.XPATH, "//li[contains(text(),'Banglore')]")
    Min_Exp = (By.ID, 'minimum-exp-input')
    Max_Exp = (By.ID, 'maximum-exp-input')
    Response = (By.ID, 'responsibilities-input')
    # Upload = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/form/div/div[11]/label/span[1]/input')
    Upload = (By.XPATH, '//input[@type="file"]')
    Submit_btn = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/form/div/div[12]/button')
    Alert_path = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/form/div/div[14]')
    Assign_job = (By.LINK_TEXT, 'Assign Job')
    job_sel = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div')
    Job = By.XPATH, "//li[contains(text(),'SDET')]"
    Width = (By.CSS_SELECTOR,
             '#root > div > div > div:nth-child(2) > div > div > div:nth-child(5) > div > div > div.MuiDataGrid-main > div:nth-child(2) > div > div')
    slider = (By.CSS_SELECTOR,
              '#root > div > div > div:nth-child(2) > div > div > div:nth-child(5) > div > div > div.MuiDataGrid-main > div:nth-child(2) > div > div')
    panelist = (By.CSS_SELECTOR, '#panelist')
    panelist_sel = (By.XPATH, "//li[contains(text(),'susmitha')]")
    schedule = (By.LINK_TEXT, 'Schedule interview')
    More = (By.CSS_SELECTOR,
            '#container > div > div > div:nth-child(3) > div > div.MuiTablePagination-root.css-rtrcn9-MuiTablePagination-root > div > div.MuiTablePagination-actions > button:nth-child(2)')
    width2 = (By.CSS_SELECTOR,
              '#container > div > div > div.MuiDataGrid-main.css-204u17-MuiDataGrid-main > div:nth-child(2) > div')
    slider2 = (By.CSS_SELECTOR,
               '#container > div > div > div.MuiDataGrid-main.css-204u17-MuiDataGrid-main > div:nth-child(2) > div')
    time_date = (By.CLASS_NAME,
                 'MuiInput-input MuiInputBase-input MuiInputBase-inputAdornedEnd css-1x51dt5-MuiInputBase-input-MuiInput-input')
    date = (By.LINK_TEXT, '23')
    save_invite = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[3]/button')
    dash_board = (By.LINK_TEXT, 'Dashboard')
    # feedback_data = (By.CLASS_NAME, 'MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft MuiTableCell-sizeMedium css-1ex1afd-MuiTableCell-root')
    feedback_data = (By.XPATH, '//td')
    # feedback_data = (By.CLASS_NAME, 'MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButtonBase-root  css-1rwt2y5-MuiButtonBase-root-MuiButton-root')
    fed_sel = (By.CSS_SELECTOR, '#customized-dialog-title > button')
    next = (By.CSS_SELECTOR,
            '#root > div > div > div:nth-child(2) > div > div > div > div > div.MuiTablePagination-root.css-jtlhu6-MuiTablePagination-root > div > div.MuiTablePagination-actions > button:nth-child(2)')

    JobOpenings = (By.XPATH, "//span[text()='Job Openings']")
    SearchText = (By.XPATH, "//input[@type='text']")
    JobDescription = (By.XPATH, "//span[text()='View Job Description’]")
    searchtext = (By.XPATH, "//input[@type='text']")
    SearchButton = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/h5/div/div/div/div/div/button/span[1]')
    ViewDescription = (By.XPATH, "//span[text()='View Job Description']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_Url)

    def Login(self, username, password):
        self.waiting()
        self.do_send_keys(self.email, username)
        self.do_send_keys(self.password, password)
        self.do_click(self.login)

    def CreateNewJob(self):
        self.waiting()
        self.Login(TestData.RecruiterUsername, TestData.Password)
        time.sleep(3)
        self.do_click(self.MenuBar)
        time.sleep(3)
        self.do_click(self.Create_NewJob)
        time.sleep(3)

        # Entering Data
        # Selecting the Band - based on requirement
        self.do_send_keys(self.Role, TestData.Role_In)
        self.do_click(self.Band_sel)
        self.do_click(self.Band)

        # Selecting Designation
        self.do_click(self.Designation_sel)
        self.do_click(self.Designation)

        # Selecting Skills
        self.do_send_keys(self.Skill_Data, TestData.Skill1)
        self.do_send_keys(self.Skill_Data, Keys.ENTER)
        time.sleep(3)
        self.do_send_keys(self.Skill_Data, TestData.Skill2)
        self.do_send_keys(self.Skill_Data, Keys.ENTER)
        time.sleep(3)
        self.do_send_keys(self.Skill_Data, TestData.Skill3)
        self.do_send_keys(self.Skill_Data, Keys.ENTER)

        # Selecting Location
        self.do_click(self.Location_sel)
        self.do_click(self.Location)

        # Entering Experience
        self.do_send_keys(self.Min_Exp, TestData.Min_data)
        time.sleep(2)
        self.do_send_keys(self.Max_Exp, TestData.Max_data)

        # Entering Responsibilities
        time.sleep(2)
        self.do_send_keys(self.Response, TestData.Res_Data)

        # Upload file
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/div/div/div[2]/div/div/form/div/div[11]/label/span[1]/input').send_keys(
            'C:/Users/visrilakshmi/Downloads/API Track Main Assignment Day 2.docx')

        # Submitting the data
        time.sleep(2)
        self.do_click(self.Submit_btn)
        try:
            alert_msg = self.find_ele(self.Alert_path)
            alert_msg = alert_msg.text
            print(alert_msg)
            assert alert_msg == TestData.Alert_msg
        except NoAlertPresentException:
            print(TestData.created_job)

    def AssignJob(self):
        self.waiting()
        self.Login(TestData.RecruiterUsername, TestData.Password)
        time.sleep(3)
        self.do_click(self.MenuBar)
        self.do_click(self.Assign_job)

        # Selecting the job
        self.do_click(self.job_sel)
        time.sleep(3)
        self.do_click(self.Job)
        time.sleep(2)
        try:
            # a = 'MuiDataGrid-overlay css-163y13e-MuiDataGrid-overlay'
            width = self.find_ele(self.width2).rect['width']
            self.do_click(self.More)
            # Entering interviewer and date driver.find_element(By.CSS_SELECTOR, '#container > div > div >
            slider = self.find_ele(self.slider2)
            self.scrolling(slider, width)
            self.do_click(self.panelist)
            time.sleep(2)
            self.do_click(self.panelist_sel)
            time.sleep(2)
            self.do_send_keys(self.time_date, '03/16/2022 06:24 am')
        except:
            print(TestData.Error_msg2)

    def ScheduleInterview(self):
        self.waiting()
        self.Login(TestData.RecruiterUsername, TestData.Password)
        time.sleep(3)
        self.do_click(self.MenuBar)
        self.do_click(self.schedule)
        time.sleep(5)
        # Checking if candidates available or not
        try:
            # a = 'MuiDataGrid-overlay css-163y13e-MuiDataGrid-overlay'
            width = self.find_ele(self.width2).rect['width']
            self.do_click(self.More)
            # Entering interviewer and date driver.find_element(By.CSS_SELECTOR, '#container > div > div >
            slider = self.find_ele(self.slider2)
            self.scrolling(slider, width)
            self.do_click(self.panelist)
            time.sleep(2)
            self.do_click(self.panelist_sel)
            time.sleep(2)
            self.do_send_keys(self.time_date, '03/16/2022 06:24 am')
        except:
            print(TestData.Error_msg2)

    def Dashboard(self):
        self.waiting()
        self.Login(TestData.RecruiterUsername, TestData.Password)
        time.sleep(3)

        # Verifying the feedback button
        time.sleep(5)
        a = self.driver.find_elements(*RecruiterPage.feedback_data)
        for i in a:
            try:
                print(i.text)
                if i.text == 'VIEW FEEDBACK':
                    if self.clickable(i):
                        self.do_click(i)
                        print(TestData.int_comp)
                        break
            except:
                self.do_click(self.next)
                continue

    def Job_openings(self):
        self.waiting()
        self.Login(TestData.RecruiterUsername, TestData.Password)
        time.sleep(3)
        self.do_click(self.MenuBar)
        self.do_click(self.JobOpenings)
        self.do_send_keys(self.searchtext, TestData.search_job)
        self.do_click(self.SearchButton)
        self.is_enabled(self.ViewDescription)
