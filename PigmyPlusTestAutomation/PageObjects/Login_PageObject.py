from selenium.webdriver.common.by import By


class Login:
    txt_username = (By.TAG_NAME, "input[name='txtUserName']")
    txt_pwd = (By.TAG_NAME, "input[name='txtPassword']")
    btn_login = (By.ID, "btnLogin")
    validation_summary = (By.TAG_NAME, "div[id='ValidationSummary1'] ul li")

    def __init__(self, drv):
        self.driver = drv
        self.wb_txtusername = None
        self.wb_txtpassword = None
        self.wb_btnlogin = None

    def get_txt_username(self):
        if self.wb_txtusername is None:
            self.wb_txtusername = self.driver.find_element(*Login.txt_username)
        return self.wb_txtusername

    def get_txt_password(self):
        if self.wb_txtpassword is None:
            self.wb_txtpassword = self.driver.find_element(*Login.txt_pwd)
        return self.wb_txtpassword

    def get_btn_login(self):
        if self.wb_btnlogin is None:
            self.wb_btnlogin = self.driver.find_element(*Login.btn_login)
        return self.wb_btnlogin

    def get_validation_summary(self):
        return self.driver.find_elements(*Login.validation_summary)
