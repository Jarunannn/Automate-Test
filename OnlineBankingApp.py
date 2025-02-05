import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BankingAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  
        self.driver.get("https://your-banking-app-url.com") # แทนที่ด้วย URL

    def test_user_registration(self):
        # element การลงทะเบียน
        register_link = self.driver.find_element(By.LINK_TEXT, "Register") 
        register_link.click()

        username_field = self.driver.find_element(By.ID, "username") 
        username_field.send_keys("testuser123")

        password_field = self.driver.find_element(By.ID, "password") 
        password_field.send_keys("password123")

        # ลงทะเบียน

        register_button = self.driver.find_element(By.ID, "registerButton") 
        register_button.click()

        # ตรวจสอบการลงทะเบียนสำเร็จ
        welcome_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Welcome')]")) 
        )
        self.assertIn("Welcome", welcome_message.text)


    def test_check_balance(self):
        self.login("testuser123", "password123")  # ใส่ username และ password

        balance_link = self.driver.find_element(By.LINK_TEXT, "Check Balance")
        balance_link.click()

        # ตรวจสอบยอดเงินคงเหลือ
        balance_element = self.driver.find_element(By.ID, "balance") 
        balance = balance_element.text
        self.assertRegex(balance, r"^\$\d+(\.\d+)?$") # regex

    def test_transfer_money(self):
        self.login("testuser123", "password123")

        transfer_link = self.driver.find_element(By.LINK_TEXT, "Transfer Money")
        transfer_link.click()

        recipient_field = self.driver.find_element(By.ID, "recipient") 
        recipient_field.send_keys("anotheruser")

        amount_field = self.driver.find_element(By.ID, "amount") 
        amount_field.send_keys("50")

        transfer_button = self.driver.find_element(By.ID, "transferButton") 
        transfer_button.click()

        # ตรวจสอบการโอนเงินสำเร็จ
        confirmation_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Transfer successful')]"))
        )
        self.assertIn("Transfer successful", confirmation_message.text)


    def login(self, username, password):  # ฟังก์ชัน helper สำหรับการเข้าสู่ระบบ
        # ใส่ username และ password
        username_field = self.driver.find_element(By.ID, "loginUsername") 
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.ID, "loginPassword") 
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.ID, "loginButton") 
        login_button.click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
