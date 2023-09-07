import time

import pytest

from PageObject.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import xlutility

class Test_002_DDT_Login:

    baseurl = ReadConfig.getApplicationUrl()
    path=".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("************* Test_002_DDT_login ************")
        self.logger.info('************* Verifing Login DDT test ***************')
        self.driver= setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.rows=xlutility.getRow_count(self.path,'Sheet1')
        print("Number of rows in the excel:",self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
            self.user=xlutility.ReadData(self.path,'Sheet1',r,1)
            self.password=xlutility.ReadData(self.path,'Sheet1',r,2)
            self.exp=xlutility.ReadData(self.path,'Sheet1',r,3)

            self.lp.SetUserName(self.user)
            self.lp.SetPassWord(self.password)
            self.lp.ClickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title='Dashboard / nopCommerce administration'

            if act_title == exp_title:

                if self.exp=="pass":
                    self.logger.info("*****passed*****")
                    self.lp.ClickLogout()
                    lst_status.append("pass")
                elif self.exp=="fail":
                    self.logger.info("**** fail ****")
                    self.lp.ClickLogout()

            elif act_title != exp_title:
                if self.exp =='pass':
                    self.logger.info("**** fail ****")
                    lst_status.append('fail')
                elif self.exp == 'fail':
                    self.logger.info("**** pass ****")
                    lst_status.append("pass")

        if 'fail'not in lst_status:
            self.logger.info('***** login DDT test is passed *****')
            self.driver.close()
            assert True

        else:
            self.logger.info("***** login DDT test is fail *****")
            self.driver.close()
            assert False

        self.logger.info('************** End of login DDT Test **************')
        self.logger.info('************* complete Tc_login_DDT_002 **************')
