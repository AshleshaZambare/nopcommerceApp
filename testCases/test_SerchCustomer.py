import time
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomerPage
from PageObjects.SearchCustomerPage import SearchCustomerPage

class Test_SearchCustomer_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    Email = "zambareneha@gmail.com"

    def test_searchByEmail(self, setup):
        self.logger.info("************************** Test Search Customer 004 started ***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("************************* Login to page success ************************")

        self.add_cust = AddCustomerPage(self.driver)
        self.add_cust.ClickOnCustomerMenu()
        self.add_cust.ClickOnCustomerMenuItem()
        time.sleep(5)

        self.search_cust = SearchCustomerPage(self.driver)
        self.search_cust.set_Email(self.Email)
        self.search_cust.ClickOnSearchBtn()
        time.sleep(5)

        status = self.search_cust.searchCustomerByEmail(self.Email)
        if status == True:
            self.logger.info("**************** Email ID found ********************")
            assert True
        else:
            self.logger.error("**************** Email ID does not found ********************")
            assert False
        self.driver.close()

    @pytest.mark.smoke
    def test_searchByName(self, setup):
        self.logger.info("************************** Test Search Customer 004 started ***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("************************* Login to page success ************************")

        self.add_cust = AddCustomerPage(self.driver)
        self.add_cust.ClickOnCustomerMenu()
        self.add_cust.ClickOnCustomerMenuItem()
        time.sleep(5)

        self.search_cust = SearchCustomerPage(self.driver)
        self.search_cust.set_Firstname("Neha")
        self.search_cust.set_Lastname("Zambare")
        self.search_cust.ClickOnSearchBtn()
        time.sleep(5)

        status = self.search_cust.searchCustomerByName("Neha Zambare")
        if status == True:
            self.logger.info("**************** Name found ********************")
            assert True
        else:
            self.logger.error("**************** Name does not found ********************")
            assert False
        self.driver.close()




