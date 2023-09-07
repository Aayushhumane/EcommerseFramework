from selenium.webdriver.common.by import By

class LoginPage:
    textbox_Username_id="Email"
    textbox_Password_id="Password"
    button_login_Xpath="//button[normalize-space()='Log in']"
    link_logout_LinkText="Logout"

    def __init__ (self,driver):
        self.driver=driver

    def SetUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_Username_id).clear()
        self.driver.find_element(By.ID,self.textbox_Username_id).send_keys(username)

    def SetPassWord(self,Password):
        self.driver.find_element(By.ID,self.textbox_Password_id).clear()
        self.driver.find_element(By.ID,self.textbox_Password_id).send_keys(Password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_Xpath).click()

    def ClickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_LinkText).click()

