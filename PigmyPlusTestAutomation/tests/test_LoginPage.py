from PigmyPlusTestAutomation.PageObjects.Login_PageObject import Login
from utilities.Base import Base


class Test_LoginPage(Base):

    def clear_textboxes_on_loginPage(self, login):
        self.clear_textbox(login.get_txt_username())
        self.clear_textbox(login.get_txt_password())

    def test_blank_username_password(self):
        login = Login(self.driver)
        flag = 0

        self.clear_textboxes_on_loginPage(login)

        login.get_btn_login().click()

        for validation in login.get_validation_summary():
            if validation.text == "Enter Your Username":
                self.log.info("Password validation found....")
                flag += 1
            elif validation.text == "Enter Password":
                self.log.info("Password validation found....")
                flag += 1
        assert flag == 2

    def test_blank_username(self):
        login = Login(self.driver)
        flag = False

        self.clear_textboxes_on_loginPage(login)

        login.get_txt_password().send_keys("sagar")

        login.get_btn_login().click()

        for validation in login.get_validation_summary():
            if validation.text == "Enter Your Username":
                self.log.info("Username validation found....")
                flag = True
        assert flag

    def test_blank_password(self):
        login = Login(self.driver)
        flag = False

        self.clear_textboxes_on_loginPage(login)

        login.get_txt_username().send_keys("system")

        login.get_btn_login().click()

        for validation in login.get_validation_summary():
            if validation.text == "Enter Password":
                self.log.info("Password validation found....")
                flag = True
        assert flag

    def test_login_success(self):
        if "Login" in self.driver.current_url:
            login = Login(self.driver)

            self.clear_textboxes_on_loginPage(login)

            login.get_txt_username().send_keys("system")
            login.get_txt_password().send_keys("sagar")

            login.get_btn_login().click()

            assert self.driver.current_url == "http://localhost/PigmyPlus/Welcome.aspx"
        else:
            assert self.driver.find_element_by_tag_name("a[href='Welcome.aspx']")
