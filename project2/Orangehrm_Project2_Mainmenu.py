import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestOrangeHRMLAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def login(self):
        user_name_input = self.driver.find_element(By.NAME, "username")
        user_password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.TAG_NAME, "button")
        user_name_input.send_keys("Admin")
        user_password_input.send_keys("admin123")

        login_button.click()

    def test_main_menu_navigation(self):
        self.login()

        admin_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Admin")))
        admin_menu.click()

        pim_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "PIM")))
        pim_menu.click()

        leave_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Leave")))
        leave_menu.click()

        time_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Time")))
        time_menu.click()

        recruitment_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Recruitment")))
        recruitment_menu.click()

        my_info_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "My Info")))
        my_info_menu.click()

        Performance_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Performance")))
        Performance_menu.click()

        dashboard_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Dashboard")))
        dashboard_menu.click()

        directory_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Directory")))
        directory_menu.click()

        buzz_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Buzz")))
        buzz_menu.click()



if __name__ == '__main__':
    unittest.main()
