import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestOrangeHRMForgotpassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def test_forgot_password(self):
        forgot_password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header")))
        forgot_password.click()


        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
        self.driver.implicitly_wait(20)

        user_name_input = self.driver.find_element(By.NAME, "username")
        user_name_input.send_keys("Madhu")

        reset_password_selector = ".oxd-button.oxd-button--large.oxd-button--secondary.orangehrm-forgot-password-button.orangehrm-forgot-password-button--reset"
        reset_password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, reset_password_selector)))
        reset_password.click()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

