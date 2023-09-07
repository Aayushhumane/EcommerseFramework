from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class SerchCustomerTest:
    customerModule = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    CustomerObject = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    txt_email_id = "SearchEmail"
    txt_firstname_id = "SearchFirstName"
    txt_lastname_id = "SearchLastName"
    btn_serch_id = "search-customers"
    table_xpath= "//div[@id='customers-grid_wrapper']"
    table_column_xpath = "//div[@id='customers-grid_wrapper']//tbody/tr/td"
    table_row_xpath = "//div[@id='customers-grid_wrapper']//tbody/tr"

    def __init__(self,driver):
        self.driver=driver

    def SetEmail(self,email):
        self.driver.find_element(By.ID,self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def SetFirstName(self,fname):
        self.driver.find_element(By.ID,self.txt_firstname_id).clear()
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(fname)

    def SetLastName(self,lname):
        self.driver.find_element(By.ID,self.txt_lastname_id).clear()
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lname)

    def clickSerch(self):
        self.driver.find_element(By.ID,self.btn_serch_id).click()

    def getRowCount(self):
        return len (self.driver.find_elements(By.XPATH,self.table_row_xpath))

    def getColumn(self):
        return len(self.driver.find_elements(By.XPATH,self.table_column_xpath))

    def SerchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getRowCount()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//div[@id='customers-grid_wrapper']//tbody/tr["+ str(r) +"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def serchCustomerByName(self,Name):
        flag= False
        for r in range(1,self.getRowCount()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            name=table.find_element(By.XPATH,"//div[@class='row']//div[@class='col-md-12']//tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag =True
                break
        return flag