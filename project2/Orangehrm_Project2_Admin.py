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

    def test_admin_navigation(self):
        self.login()

        admin_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Admin")))
        admin_menu.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'User Management')]")))

        user_management_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'User Management')]")))
        user_management_option.click()

        job_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Job')]")))
        job_option.click()

        organization_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Organization')]")))
        organization_option.click()

        qualifications_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Qualifications')]")))
        qualifications_option.click()

        nationalities_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and text()='Nationalities']")))
        nationalities_option.click()


        corporate_banking_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and text()='Corporate Branding']")))
        corporate_banking_option.click()

        configuration_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Configuration')]/i[@class='oxd-icon bi-chevron-down' and @with-container='false' and @data-v-bddebfba]")))
        configuration_option.click()







    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()









