import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestOrangeHRMAddEmployeeDetails(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def test_add_employee_details_sucess(self):
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
        add_employee_option = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Add Employee")
        add_employee_option.click()

        wait = WebDriverWait(self.driver, 10)
        first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
         
        first_name_input = self.driver.find_element(By.NAME, "firstName")
        middle_name_input = self.driver.find_element(By.NAME, "middleName")
        last_name_input = self.driver.find_element(By.NAME, "lastName")

        first_name_input.send_keys("YYY")
        middle_name_input.send_keys("YYYX")
        last_name_input.send_keys("ZZZXY")

        WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located((By.CLASS_NAME, "oxd-form-loader")))

        switch_button = self.driver.find_element(By.CLASS_NAME, "oxd-switch-input--active")
        switch_button.click()




        username_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-input.oxd-input--active")))
        password_input = self.driver.find_element(By.CSS_SELECTOR, ".oxd-input.oxd-input--active")
        confirm_password_input = self.driver.find_element(By.CSS_SELECTOR, ".oxd-input.oxd-input--active")


        username_input.send_keys("YYYYY")
        password_input.send_keys("Password123@")
        confirm_password_input.send_keys("Password123@")

        save_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")))



        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/272")
        self.driver.implicitly_wait(20)

        nick_name_input = self.driver.find_element(By.CLASS_NAME, "oxd-input--active")
        license_number_input = self.driver.find_element(By.CSS_SELECTOR, ".oxd-input.oxd-input--active")


        nick_name_input.send_keys("XYZ")
        license_number_input.send_keys("876987697")

        day_picker = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-date-wrapper")))
        WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located((By.CLASS_NAME, "oxd-form-loader")))
        day_picker.click()
        day_to_select = "30"
        day_element = self.driver.find_element(By.CLASS_NAME, "oxd-date-input")
        self.driver.execute_script("arguments[0].value = arguments[1];", day_element, day_to_select)

        selected_day = day_element.get_attribute("value")
        print(f"Selected day: {selected_day}")
        self.assertEqual(selected_day, day_to_select)


        SSN_number_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.oxd-input.oxd-input--active")))
        SIN_number_input = self.driver.find_element(By.CSS_SELECTOR, "input.oxd-input.oxd-input--active")

        SSN_number_input.send_keys("453475360")
        SIN_number_input.send_keys("8769876960")




        dropdown_div = self.driver.find_element(By.CLASS_NAME, "oxd-select-text-input")
        dropdown_div.click()
        married_option = self.driver.find_element(By.XPATH, '//div[@clear="false" and @class="oxd-select-text-input" and @tabindex="0" and @data-v-67d2aedf=""]')
        married_option.click()

        day_picker = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//i[@class="oxd-icon bi-calendar oxd-date-input-icon"]')))
        day_picker.click()
        day_to_select = "30"
        day_element = self.driver.find_element(By.CLASS_NAME, "oxd-date-input")
        self.driver.execute_script("arguments[0].value = arguments[1];", day_element, day_to_select)
        selected_day = day_element.get_attribute("value")

        print(f"Selected day: {selected_day}")
        self.assertEqual(selected_day, day_to_select)
        female_radio_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @value='2']/following-sibling::span[contains(@class, 'oxd-radio-input--active')]")))
        self.driver.execute_script("arguments[0].click();", female_radio_button)

        military_service_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-input--active")))
        military_service_input.send_keys("NO")


        save_button1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")))


        dropdown_div = self.driver.find_element(By.CLASS_NAME, "oxd-select-text-input")
        dropdown_div.click()
        A_plus_option = self.driver.find_element(By.XPATH, '//div[@clear="false" and @class="oxd-select-text-input" and @tabindex="0" and @data-v-67d2aedf=""]')
        A_plus_option.click()

        save_button2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")))



        add_pic_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--text")))
        add_pic_button.click()
        file_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-file-button")))
        picture_path = "/Users/madhu/Downloads/SDLC and STLC pic.docx"
        ActionChains(self.driver).move_to_element(file_input).click().send_keys(picture_path).perform()

        comment_box = self.driver.find_element(By.CSS_SELECTOR, ".oxd-textarea.oxd-textarea--active.oxd-textarea--resize-vertical")
        comment_text = "This is a test comment."
        comment_box.send_keys(comment_text)

        save_button3 = self.driver.find_element(By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
        wait = WebDriverWait(self.driver, 10)
        save_button3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")))
        action = ActionChains(self.driver)
        action.move_to_element(save_button3).click().perform()




    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
