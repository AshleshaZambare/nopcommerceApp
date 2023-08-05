from selenium.webdriver.common.by import By


class SearchCustomerPage:
    textbox_Email_id = "SearchEmail"
    textbox_FirstName_id = "SearchFirstName"
    textbox_Lastname_id = "SearchLastName"
    btn_search_id = "search-customers"
    table_xpath = "//*[@class='dataTables_scrollBody']"
    table_row_xpath = "//*[@class='dataTables_scrollBody']//tbody/tr"
    table_column_xpath = "//*[@class='dataTables_scrollBody']//tbody/tr/td"

    def __init__(self, setup):
        self.driver = setup

    def set_Email(self, email):
        self.driver.find_element(By.ID, self.textbox_Email_id).send_keys(email)

    def set_Firstname(self, firstname):
        self.driver.find_element(By.ID, self.textbox_FirstName_id).send_keys(firstname)

    def set_Lastname(self, lastname):
        self.driver.find_element(By.ID, self.textbox_Lastname_id).send_keys(lastname)

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for rows in range(1, self.getNoOfRows()+1):
            emailid = self.driver.find_element(By.XPATH, "//*[@class='dataTables_scrollBody']//tbody/tr["+ str(rows)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag


    def searchCustomerByName(self, firstname):
        flag = False
        for rows in range(1, self.getNoOfRows()+1):
            name = self.driver.find_element(By.XPATH, "//*[@class='dataTables_scrollBody']//tbody/tr["+ str(rows)+"]/td[3]").text
            if firstname in name:
                flag = True
                break
        return flag

    def ClickOnSearchBtn(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()