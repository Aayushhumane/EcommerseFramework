import pytest

from PageObject.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen


class Test_001_Login:

    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.Sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info('************* Test_001_Login ***************')
        self.logger.info('************* Verifing Home Page Title ***************')
        self.driver= setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.logger.info('************* Test is Passed ***************')
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\screenShots\\'+'test_homePageTitle.png')
            self.logger.error('************* Test is Failed ***************')
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info('************* Verifing Login ***************')
        self.driver= setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassWord(self.password)
        self.lp.ClickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info('************* Test Passed ***************')
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenShots\\"+"test_login.png")
            self.logger.error('************* Test Failed ***************')
            self.driver.close()
            assert False