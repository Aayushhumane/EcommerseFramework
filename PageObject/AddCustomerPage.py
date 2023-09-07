from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class AddCustomer:
    customerModule = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    CustomerObject = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    AddNew_customer = "//a[normalize-space()='Add new']"
    txtEmail_id = 'Email'
    txtPassword_id = 'Password'
    txtFirstName_id = "FirstName"
    txtLastName_id = 'LastName'
    RadGender_male_Xpath = "//input[@id='Gender_Male']"
    RadGender_female_Xpath = "//input[@id='Gender_Female']"
    txt_DoB_xpath = "//input[@id='DateOfBirth']"
    txt_customerRole_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listitemAdministrator_xpath = "//span[normalize-space()='Administrators']"
    listitemForumModerator_xpath = "//span[normalize-space()='Forum Moderators']"
    listitemGuest_xpath = "//span[normalize-space()='Guests']"
    listitemRegister = "//span[normalize-space()='Registered']"
    listitemVendor = "//span[normalize-space()='Vendors']"
    drpmngOfVendor = "//select[@id='VendorId']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminComment_xpath="//textarea[@id='AdminComment']"
    bntSave_xpath = "//button[@name='save']"

    def __init__ (self,driver):
        self.driver=driver

    def clickOn_customerModule(self):
        self.driver.find_element(By.XPATH, self.customerModule).click()

    def clickon_customerModuleItem(self):
        self.driver.find_element(By.XPATH,self.CustomerObject).click()

    def clickon_Addnew(self):
        self.driver.find_element(By.XPATH,self.AddNew_customer).click()

    def Add_email(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def Add_password(self,password):
        self.driver.find_element(By.ID,self.txtPassword_id).send_keys(password)

    def Add_firstName(self,firstname):
        self.driver.find_element(By.ID,self.txtFirstName_id).send_keys(firstname)

    def Add_lastName(self,lastname):
        self.driver.find_element(By.ID,self.txtLastName_id).send_keys(lastname)

    def gender_male(self):
        self.driver.find_element(By.XPATH,self.RadGender_male_Xpath).click()

    def gender_female(self):
        self.driver.find_element(By.XPATH,self.RadGender_female_Xpath).click()

    def dob(self,dob):
        self.driver.find_element(By.XPATH,self.txt_DoB_xpath).send_keys(dob)

    def cumpanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def AdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.txtAdminComment_xpath).send_keys(comment)

    def SaveButton(self):
        self.driver.find_element(By.XPATH,self.bntSave_xpath).click()

    def CustomerRole(self,role):
        self.driver.find_element(By.XPATH,self.txt_customerRole_xpath).click()
        time.sleep(5)
        # if role=="Registered":
        #     self.listitem = self.driver.find_element(By.XPATH,self.listitemRegister)
        #
        # elif role == "Forum Moderators":
        #     self.listitem = self.driver.find_element(By.XPATH,self.listitemForumModerator_xpath)
        #
        # elif role == "Vendors":
        #     self.listitem = self.driver.find_element(By.XPATH,self.listitemVendor)
        #
        # elif role == "Administrators":
        #     self.listitem = self.driver.find_element(By.XPATH,self.listitemAdministrator_xpath)
        #
        # elif role == "Guests":
        #     time.sleep(5)
        #     self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
        #     self.listitem = self.driver.find_element(By.XPATH,self.listitemGuest_xpath)
        #
        # elif role == "Registered":
        #     self.listitem = self.driver.find_element(By.XPATH, self.listitemRegister)
        #
        # else:
        #     self.listitem = self.driver.find_element(By.XPATH,self.listitemGuest_xpath)
        # time.sleep(3)
        # self.driver.execute_script("arguments[0].click();",self.listitem)

    def SetmanagerVendor(self,vendor):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmngOfVendor))
        drp.select_by_visible_text(vendor)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH,self.RadGender_male_Xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH,self.RadGender_female_Xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.RadGender_male_Xpath).click()