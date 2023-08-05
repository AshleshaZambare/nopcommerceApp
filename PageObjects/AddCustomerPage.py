import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerPage:

    link_Customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_Customers_menu_item_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btn_AddNew_linktext = "Add new"
    textbox_Email_id = "Email"
    textbox_Password_id = "Password"
    textbox_FirstName_id = "FirstName"
    textbox_LastName_id =  "LastName"
    rad_btn_Male_id = "Gender_Male"
    rad_btn_Female_btn_id = "Gender_Female"
    datepicker_DOB_id = "DateOfBirth"
    textbox_company_id = "Company"
    txtbox_customerRole_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitem_Administrator_xpath = "//li[normalize-space()='Administrators']"
    lstitem_ForumModerator_xpath = "//li[normalize-space()='Forum Moderators']"
    lstitem_Guests_xpath = "//li[normalize-space()='Guests']"
    lstitem_Registered_xpath = "//li[normalize-space()='Registered']"
    lstitem_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    dropdwn_ManagerOfVendor_xpath = "//*[@id='VendorId']"
    checkbox_isTextExempt_id = "IsTaxExempt"
    textbox_AdminComment_xpath = "//textarea[@id='AdminComment']"
    btn_Save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.link_Customers_menu_xpath).click()

    def ClickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.link_Customers_menu_item_xpath).click()

    def ClickOnAddNew(self):
        self.driver.find_element(By.LINK_TEXT, self.btn_AddNew_linktext).click()

    def set_Email(self, emailid):
        self.driver.find_element(By.ID, self.textbox_Email_id).send_keys(emailid)

    def set_Password(self, password):
        self.driver.find_element(By.ID, self.textbox_Password_id).send_keys(password)

    def set_FirstName(self, firstname):
        self.driver.find_element(By.ID,self.textbox_FirstName_id).send_keys(firstname)

    def set_LastName(self, lastname):
        self.driver.find_element(By.ID, self.textbox_LastName_id).send_keys(lastname)

    def set_Gender_Female(self):
        self.driver.find_element(By.ID, self.rad_btn_Female_btn_id).click()

    def set_Gender_Male(self):
        self.driver.find_element(By.ID, self.rad_btn_Male_id).click()

    def set_Date_Of_Birth(self, dob):
        self.driver.find_element(By.ID, self.datepicker_DOB_id).send_keys(dob)

    def set_CompanyName(self, companyname):
        self.driver.find_element(By.ID, self.textbox_company_id).send_keys(companyname)

    def set_Tax_Exempt_Checkbox(self):
        self.driver.find_element(By.ID, self.checkbox_isTextExempt_id ).click()

    def set_Customer_Roles(self, role):
        self.driver.find_element(By.XPATH, self.txtbox_customerRole_xpath ).click()
        time.sleep(6)
        #self.lstitem = []
        if role == "Administrators":
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitem_Administrator_xpath)

        elif role == "Forrum Moderator":
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitem_ForumModerator_xpath )

        #Here user can be resistered or Guests, Only one
        elif role == "Guests":
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitem_Guests_xpath)

        elif role == "Registered":
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitem_Registered_xpath )

        else:
            self.driver.find_element(By.XPATH, self.lstitem_Guests_xpath)

        #self.lstitem.click() sometimes click dont work on some elements so below is the alternative way
        self.driver.execute_script("arguments[0].click()", self.lstitem)
        time.sleep(3)

    def set_ManagerOFVendor(self, value):
        self.drpdwn = Select(self.driver.find_element(By.XPATH, self.dropdwn_ManagerOfVendor_xpath))
        self.drpdwn.select_by_visible_text(value)
        time.sleep(2)

    def set_AdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.textbox_AdminComment_xpath).send_keys(comment)
    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()

