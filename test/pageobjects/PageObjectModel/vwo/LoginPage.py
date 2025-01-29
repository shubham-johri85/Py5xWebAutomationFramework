import time

from selenium.webdriver.common.by import By





class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    #page locators
    username = (By.ID, "login-username")
    password = (By.NAME, "password" )
    submit_button = (By.ID, "js-login-btn")
    error_message = (By.CLASS_NAME, "notification-box-description" )
    free_trial = (By.LINK_TEXT, "Start a free trial")

    #page actions
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)
    def get_password(self):
        return self.driver.find_element(*LoginPage.password)
    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)
    def get_free_trial_button(self):
        return self.driver.find_element(*LoginPage.free_trail)
    def get_error_message(self):
        time.sleep(5)
        return self.driver.find_element(*LoginPage.error_message)

    def login_to_vwo(self, usr, pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_submit_button().click()
        except Exception as e:
            print(e)

    def free_trial_button_click(self):
        try:
            self.get_free_trial_button().click()
        except Exception as e:
            print(e)

    def get_error_message_text(self):
        return self.get_error_message().text
