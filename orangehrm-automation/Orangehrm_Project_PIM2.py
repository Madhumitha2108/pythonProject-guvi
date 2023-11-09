import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestOrangeHRMDeleteEmployeeDetails(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def test_delete_employee_detail_success(self):
        user_name_input = self.driver.find_element(By.NAME, "username")
        user_password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.TAG_NAME, "button")
        user_name_input.send_keys("Admin")
        user_password_input.send_keys("admin123")

        login_button.click()


        pim_menu = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "PIM")))
        pim_menu.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"PIM")))
        employee_list_option = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Employee List")
        employee_list_option.click()
        page_2_option = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='button' and contains(@class, 'oxd-pagination-page-item') and contains(@class, 'oxd-pagination-page-item--page-selected') and @data-v-92137808]")))
        page_2_option.click()
        Madhu_Manojkumar_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'oxd-checkbox-input') and contains(@class, 'oxd-checkbox-input--active') and contains(@class, '--label-right') and contains(@class, 'oxd-checkbox-input')]")))
        ActionChains(self.driver).move_to_element(Madhu_Manojkumar_checkbox).click().perform()
        delete_button_option = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-icon-button")))
        delete_button_option.click()
        confirm_delete_option = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-button--medium")))
        confirm_delete_option.click()





    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


