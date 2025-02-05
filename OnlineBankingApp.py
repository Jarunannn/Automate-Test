# framework write test case
import unittest
# browser
from selenium import webdriver
# element on web (id, name)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BankingAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  
        self.driver.get("https://your-banking-app-url.com")  # Replace with your URL

    def test_user_registration(self):
        try:
            register_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Register"))
            )
            register_link.click()

            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.send_keys("test12")

            password_field = self.driver.find_element(By.ID, "password")  
            password_field.send_keys("P@ssw0rd")

            confirm_password_field = self.driver.find_element(By.ID, "confirmPassword") 
            confirm_password_field.send_keys("P@ssw0rd")

            register_button = self.driver.find_element(By.ID, "registerButton")  
            register_button.click()

            welcome_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Welcome')]")) 
            )
            self.assertIn("Youu have successfully registered.", welcome_message.text)

        except Exception as e:
            print(f"Registration test failed: {e}")
            self.fail("Registration test failed")

    def test_user_registration_password_mismatch(self):
        try:
            register_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Register"))
            )
            register_link.click()

            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username")) 
            )
            username_field.send_keys("test12")

            password_field = self.driver.find_element(By.ID, "password") 
            password_field.send_keys("P@ssw0rd")

            confirm_password_field = self.driver.find_element(By.ID, "confirmPassword") 
            confirm_password_field.send_keys("wrongpassword")  

            register_button = self.driver.find_element(By.ID, "registerButton") 
            register_button.click()

            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "passwordMismatchError"))  
            )

            self.assertTrue(error_message.is_displayed())
            self.assertIn("Passwords do not match", error_message.text)  

        except Exception as e:
            print(f"Password mismatch test failed: {e}")
            self.fail("Password mismatch test failed")


    def test_check_balance(self):
        try:
            self.login("test12", "P@ssw0rd") 

            balance_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Check Balance")) 
            )
            balance_link.click()

            balance_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "balance"))  
            )
            balance = balance_element.text
            self.assertRegex(balance, r"^\$\d+(\.\d+)?$") 

        except Exception as e:
            print(f"Check balance test failed: {e}")
            self.fail("Check balance test failed")

    def test_transfer_money(self):
        try:
            self.login("test12", "P@ssw0rd")  

            transfer_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Transfer Money"))  
            )
            transfer_link.click()

            recipient_field = self.driver.find_element(By.ID, "recipient")  
            recipient_field.send_keys("anotheruser")

            amount_field = self.driver.find_element(By.ID, "amount")  
            amount_field.send_keys("50")

            transfer_button = self.driver.find_element(By.ID, "transferButton") 
            transfer_button.click()

            confirmation_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Transfer successful')]")) 
            )
            self.assertIn("Transfer successful", confirmation_message.text)

        except Exception as e:
            print(f"Transfer money test failed: {e}")
            self.fail("Transfer money test failed")


    def login(self, username, password):  # Helper login function
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "loginUsername")) 
            )
            username_field.send_keys(username)
            password_field = self.driver.find_element(By.ID, "loginPassword")  
            password_field.send_keys(password)
            login_button = self.driver.find_element(By.ID, "loginButton")  
            login_button.click()
        except Exception as e:
            print(f"Login failed: {e}")
            self.fail("Login failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
