import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BankingAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # หรือ browser driver อื่นๆ
        self.driver.get("https://your-banking-app-url.com") # แทนที่ด้วย URL แอปของคุณ

    def test_user_registration(self):
        # ค้นหาและโต้ตอบกับ element การลงทะเบียน
        register_link = self.driver.find_element(By.LINK_TEXT, "Register") # ตัวอย่าง locator
        register_link.click()

        username_field = self.driver.find_element(By.ID, "username") # ตัวอย่าง locator
        username_field.send_keys("testuser123")

        password_field = self.driver.find_element(By.ID, "password") # ตัวอย่าง locator
        password_field.send_keys("password123")

        # ... กรอกข้อมูลการลงทะเบียนอื่นๆ ...

        register_button = self.driver.find_element(By.ID, "registerButton") # ตัวอย่าง locator
        register_button.click()

        # ตรวจสอบการลงทะเบียนสำเร็จ (เช่น ตรวจสอบข้อความต้อนรับ)
        welcome_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Welcome')]")) # ตัวอย่าง locator
        )
        self.assertIn("Welcome", welcome_message.text)  # ตรวจสอบส่วนหนึ่งของข้อความ


    def test_check_balance(self):
        # เข้าสู่ระบบ (สมมติว่ามีฟังก์ชันหรือขั้นตอนการเข้าสู่ระบบ)
        self.login("testuser123", "password123")  # แทนที่ด้วยการเข้าสู่ระบบจริงของคุณ

        balance_link = self.driver.find_element(By.LINK_TEXT, "Check Balance") # ตัวอย่าง locator
        balance_link.click()

        # ค้นหาและตรวจสอบการแสดงยอดคงเหลือ
        balance_element = self.driver.find_element(By.ID, "balance") # ตัวอย่าง locator
        balance = balance_element.text
        self.assertRegex(balance, r"^\$\d+(\.\d+)?$") # regex พื้นฐานสำหรับรูปแบบสกุลเงิน

    def test_transfer_money(self):
        self.login("testuser123", "password123")

        transfer_link = self.driver.find_element(By.LINK_TEXT, "Transfer Money") # ตัวอย่าง locator
        transfer_link.click()

        recipient_field = self.driver.find_element(By.ID, "recipient") # ตัวอย่าง locator
        recipient_field.send_keys("anotheruser")

        amount_field = self.driver.find_element(By.ID, "amount") # ตัวอย่าง locator
        amount_field.send_keys("50")

        transfer_button = self.driver.find_element(By.ID, "transferButton") # ตัวอย่าง locator
        transfer_button.click()

        # ตรวจสอบการโอนเงินสำเร็จ (เช่น ตรวจสอบข้อความยืนยัน)
        confirmation_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Transfer successful')]"))
        )
        self.assertIn("Transfer successful", confirmation_message.text)

        # (Optional) ตรวจสอบเพิ่มเติม: ตรวจสอบยอดคงเหลือของผู้ใช้ทั้งสอง

    def login(self, username, password):  # ฟังก์ชัน helper สำหรับการเข้าสู่ระบบ
        # แทนที่ด้วยขั้นตอนการเข้าสู่ระบบจริงของคุณ
        username_field = self.driver.find_element(By.ID, "loginUsername") # ตัวอย่าง locator
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.ID, "loginPassword") # ตัวอย่าง locator
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.ID, "loginButton") # ตัวอย่าง locator
        login_button.click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
