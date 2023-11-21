import unittest

import self
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestOrangeHRMLAdmin(unittest.TestCase):
     """
    Test case for the admin navigation functionality on the OrangeHRM application.
    """
    def setUp(self):

        """
        Set up the test environment by initializing the WebDriver,
        maximizing the window, and navigating to the OrangeHRM login page.
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def login(self):
        """
        Helper method to perform login by entering credentials and clicking the login button.
        """
        user_name_input = self.driver.find_element(By.NAME, "username")
        user_password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.TAG_NAME, "button")
        user_name_input.send_keys("Admin")
        user_password_input.send_keys("admin123")

        login_button.click()

    def test_admin_navigation(self):

          """
        Test the navigation through various admin options in the OrangeHRM application.
        """
         # Perform login

        self.login()
         # Click on the Admin menu
        admin_menu = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Admin")))
        admin_menu.click()
         # Wait for the User Management tab to be present
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'User Management')]")))
          # Navigate to User Management
        user_management_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'User Management')]")))
        user_management_option.click()
            # Navigate to Job
        job_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Job')]")))
        job_option.click()
            # Navigate to Organization
        organization_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Organization')]")))
        organization_option.click()
               # Navigate to Qualifications
        qualifications_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Qualifications')]")))
        qualifications_option.click()
               # Navigate to Nationalities
        nationalities_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and text()='Nationalities']")))
        nationalities_option.click()

               # Navigate to Corporate Branding
        corporate_banking_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and text()='Corporate Branding']")))
        corporate_banking_option.click()
             # Navigate to Configuration
        configuration_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Configuration')]/i[@class='oxd-icon bi-chevron-down' and @with-container='false' and @data-v-bddebfba]")))
        configuration_option.click()







    def tearDown(self):

        """
        Clean up the test environment by quitting the WebDriver.
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()









