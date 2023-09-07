import pytest
import time

from selenium.webdriver.common.by import By

from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
from PageObject.LoginPage import LoginPage
from PageObject.AddCustomerPage import AddCustomer
import string
import random

class Test_003_AddNewcustomer:
    baseure = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_AddCustomer(self,setup):
        self.logger.info('*******Test_003_Addcustomer*****')
        self.driver=setup
        self.driver.get(self.baseure)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassWord(self.password)
        self.lp.ClickLogin()
        self.logger.info('******Login successful******')

        self.logger.info('******** starting Add customer******')

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOn_customerModule()
        self.addcust.clickon_customerModuleItem()
        self.addcust.clickon_Addnew()

        self.logger.info('****** Adding customer info ******')

        self.email=random_generator()+"@gmail.com"
        self.addcust.Add_email(self.email)
        self.addcust.Add_password('123@aa')
        self.addcust.Add_firstName('Aayush')
        self.addcust.Add_lastName('Humane')
        self.addcust.setGender('Male')
        self.addcust.AdminComment('aaayusssshhhhhhh')
        self.addcust.cumpanyName('aayuifotec')
        self.addcust.dob('5/30/1994')
        self.addcust.SetmanagerVendor('Vendor 2')
        time.sleep(3)
        self.addcust.CustomerRole('Guests')
        self.addcust.SaveButton()

        self.logger.info('****** saving customer info *******')

        self.logger.info('***** validating test case ****** ')
        self.msg = self.driver.find_element(By.TAG_NAME,'body').text
        print(self.msg)
        if "The new customer has been added successfully."in self.msg:
            assert True == True
            self.logger.info('***** Add customer Test is Passed *****')
        else:
            self.driver.save_screenshot(".\\screenShots\\"+"test_addCustomer.png")
            self.logger.error('***** Add customer Test Failed ******')
            assert  True == False
            self.driver.close()
            self.logger.info('****** Ending of Adding new customer ******')

def random_generator(size=20,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars)for x in range(size))
