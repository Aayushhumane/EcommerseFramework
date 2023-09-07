import pytest

from Utilities.customlogger import LogGen
from Utilities.readProperties import ReadConfig
from PageObject.LoginPage import LoginPage
from PageObject.AddCustomerPage import AddCustomer
from PageObject.SerchCoustomer import SerchCustomerTest
import time

class Test_005_SerchCustomer:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_serchCustomerByName(self,setup):

        self.logger.info('****** Test_005_SerchCustomer ****** ')
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info('***** login statted *****')

        self.lp = LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassWord(self.password)
        self.lp.ClickLogin()
        self.logger.info('***** Login Successful *****')

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOn_customerModule()
        self.addcust.clickon_customerModuleItem()
        self.logger.info('****** opean search window ******')
        try:
            self.serchcust = SerchCustomerTest(self.driver)
            self.serchcust.SetFirstName('Virat Kohli')
            self.serchcust.clickSerch()
            time.sleep(5)
        except 'NoSuchElement ':
            status = self.serchcust.serchCustomerByName('Virat Kohli')
            assert True == status
            self.logger.info('***** TC.Test_005_SerchCustomer by Name is finished')
