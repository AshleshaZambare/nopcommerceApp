import pytest

from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_home_page_title(self, setup):
        self.logger.info("******************** Test_001_Login ********************")
        self.logger.info("*************** Verifying Home Page Title ********************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.driver.get(self.baseURL)
        act_title = "Your store. Login"
        self.exp_title = self.driver.title
        if act_title == self.exp_title:
            self.logger.info("**************** Home Page Title Test Passed **************************")
            assert True
        else:
            self.logger.error("**************** Home Page Title Test Failed **************************")
            self.driver.save_screenshot(".\\Screenshots\\"+"Test_Home_Page_title.png")
            assert False


    def test_Login(self, setup):
        self.logger.info("*********************** Verifying Login Test ****************************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.driver.get(self.baseURL)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.clickLogin()
        self.exp_title = self.driver.title
        act_title = "Dashboard / nopCommerce administration"
        if act_title == self.exp_title:
            self.logger.info("**************** Login Test Passed **************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_Login.png")
            self.driver.close()
            assert True
        else:
            self.logger.error("**************** Login Test failed **************************")
            self.driver.save_screenshot(".\\Screenshots\\"+"Test_Login.png")
            self.driver.close()
            assert False


