import random
import time
import string

from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from PageObjects.AddCustomerPage import AddCustomerPage
from PageObjects.LoginPage import LoginPage

class Test_AddCustomer_003:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger.info("************************ Test Add Customer 003 started ****************************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.clickLogin()
        self.add_cust = AddCustomerPage(self.driver)
        self.add_cust.ClickOnCustomerMenu()
        self.add_cust.ClickOnCustomerMenuItem()
        self.add_cust.ClickOnAddNew()
        time.sleep(5)

        self.Email = random_generator() + "@gmail.com"
        self.logger.info("Email:" + self.Email)
        self.add_cust.set_Email(self.Email)
        time.sleep(5)

        self.add_cust.set_Password("neha@7276")
        self.add_cust.set_FirstName("Neha")
        self.add_cust.set_LastName("Zambare")
        self.add_cust.set_Date_Of_Birth("12/06/1996")
        self.add_cust.set_Gender_Female()
        self.add_cust.set_CompanyName("Thundersoft India")
        self.add_cust.set_Tax_Exempt_Checkbox()
        self.add_cust.set_Customer_Roles("Guests")
        self.add_cust.set_ManagerOFVendor("Vendor 2")
        self.add_cust.set_AdminComment("I am comment")
        time.sleep(5)
        self.add_cust.ClickOnSave()
        time.sleep(5)

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        if 'customer has been added successfully.' in self.msg:
            self.logger.info("**************** Add Customer Test Passed ******************** ")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_customer.PNG")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_customer.PNG")
            self.logger.error("**************** Add Customer Test Failed ******************** ")
            assert False
        self.driver.close()

        self.logger.info("********************** Ending Home Page Title Test **************************")

def random_generator(size=8, chars= string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))





