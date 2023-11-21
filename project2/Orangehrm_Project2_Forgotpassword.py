import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestOrangeHRMForgotpassword(unittest.TestCase):
    """
    Test case for the forgot password functionality on the OrangeHRM login page.
    """
    def setUp(self):
        """
        Set up the test environment by initializing the WebDriver, maximizing the window,
        and navigating to the OrangeHRM login page.
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def test_forgot_password(self):

        """
        Test the forgot password functionality by clicking on the forgot password link,
        navigating to the reset password page, entering a username, and initiating the password reset.
        """
        # Click on the forgot password link
        forgot_password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header")))
        forgot_password.click()

        # Navigate to the password reset page
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
        self.driver.implicitly_wait(20)
         # Enter a username for password reset
        user_name_input = self.driver.find_element(By.NAME, "username")
        user_name_input.send_keys("Madhu")
        # Click on the reset password button
        reset_password_selector = ".oxd-button.oxd-button--large.oxd-button--secondary.orangehrm-forgot-password-button.orangehrm-forgot-password-button--reset"
        reset_password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, reset_password_selector)))
        reset_password.click()


    def tearDown(self):
        """
        Clean up the test environment by quitting the WebDriver.
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

