import pytest

from Utilities.customlogger import LogGen
from Utilities.readProperties import ReadConfig
from PageObject.LoginPage import LoginPage
from PageObject.AddCustomerPage import AddCustomer
from PageObject.SerchCoustomer import SerchCustomerTest

import time

class Test_004_serchCustomer:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_serchCustomer(self,setup):
        self.logger.info('******* Test_004_ serch customer ******')
        self.driver= setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassWord(self.password)
        self.lp.ClickLogin()
        self.logger.info('******** login successful *******')

        self.logger.info('***** start serching customer email ******')
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOn_customerModule()
        self.addcust.clickon_customerModuleItem()

        self.logger.info('****** Adding customer email *******')
        self.sechcust = SerchCustomerTest(self.driver)
        self.sechcust.SetEmail('kiyjcycyhjc676008@gmail.com')
        self.sechcust.clickSerch()
        time.sleep(5)
        status = self.sechcust.SerchCustomerByEmail('kiyjcycyhjc676008@gmail.com')
        assert True == status
        self.logger.info('****** Test_004_serchCustomer is finished *******')