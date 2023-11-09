import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestOrangeHRMLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def test_successful_login(self):
        user_name_input = self.driver.find_element(By.NAME, "username")
        user_password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.TAG_NAME, "button")
        user_name_input.send_keys("Admin")
        user_password_input.send_keys("Madhu")

        login_button.click()


        error_message_locator = (By.CSS_SELECTOR, ".oxd-alert-content-text")
        wait = WebDriverWait(self.driver, 10)
        error_message = wait.until(EC.presence_of_element_located(error_message_locator))

        self.assertTrue("Invalid credentials" in error_message.text)
        print("Invalid credentials")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()





