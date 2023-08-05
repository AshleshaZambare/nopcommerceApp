import logging
import time

from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from PageObjects.LoginPage import LoginPage
from utilities import XLUtils

class Test_Login_DDT_002:
    URL = ReadConfig.getApplicationURL()
    xl_path = ReadConfig.get_file_path()
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("*********************** Test_Login_DDT_002 started ***************************")
        self.driver = setup
        self.driver.get(self.URL)
        self.lp = LoginPage(self.driver)

        lst_status = []
        self.row = XLUtils.getRowCount(self.xl_path, "Sheet1")

        for r in range(2, self.row+1):
            self.username = XLUtils.readData(self.xl_path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.xl_path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.xl_path, "Sheet1", r, 3)
            act_title = "Dashboard / nopCommerce administration"

            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            self.act_title = self.driver.title
            self.exp_title = "Dashboard / nopCommerce administration"
            if self.act_title == self.exp_title:
                if self.exp == "Pass":
                    lst_status.append("Pass")
                    logging.info("******* Passed *******")
                    self.lp.click_logout()

                elif self.exp == "Fail":
                    logging.info("******** Failed *********")
                    lst_status.append("Fail")

            else:
                if self.exp == "Pass":
                    lst_status.append("Fail")
                    logging.info("******** Failed *********")

                elif self.exp == "Fail":
                    lst_status.append("Pass")
                    logging.info("******* Passed *******")

        self.driver.close()
        if "Fail" not in lst_status:
            self.logger.info("**************** TestCase is Passed ************************")
            assert True
        else:
            self.logger.info("***************** TestCase is Failed ***********************")
            assert False

        logging.info("******************* End of Login DDT Test ************************")
        logging.info("*************************** Completed LoginDDTTest002 *********************************")