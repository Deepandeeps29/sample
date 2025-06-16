import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from report.custom_logger import CustomLogger
from Library.library import Library_Locator

logger = CustomLogger()

class RegisterPage:
    # "__init__() runs automatically when you create an object from the class."
    def __init__(self, driver):
        try:
            self.driver = driver
            logger.log("Launching Chrome", "PASS", "ChromeDriver launched successfully")
        except Exception as e:
            logger.log("Launching Chrome", "FAIL", f"Exception: {str(e)}")

    def load(self):
        try:
            self.driver.get(Library_Locator.Url)
            logger.log("Opening Qspider Webpage", "PASS", "Navigated successfully")
        except Exception as e:
            logger.log("Opening Qspider Webpage", "FAIL", f"Exception: {str(e)}")

    def UI(self):
        try:
            self.driver.find_element(By.XPATH, Library_Locator.UI_Test).click()
            logger.log("Click 'UI Testing Concepts'", "PASS", "Clicked successfully")
        except Exception as e:
            logger.log("Click 'UI Testing Concepts'", "FAIL", f"Exception: {str(e)}")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Library_Locator.Practice_Session_Text))
            )
            logger.log("Verify 'Practice Session Title'", "PASS", "Button is visible")
        except Exception as e:
            logger.log("Verify 'Practice Session Title'", "FAIL", f"Exception: {str(e)}")

    def Register_Page(self):
        from data.db import fetch_contacts

        try:
            self.driver.find_element(By.XPATH, Library_Locator.Text_Field_Button).click()
            logger.log("Click 'Text Field'", "PASS", "Clicked the Text Field section")
        except Exception as e:
            logger.log("Click 'Text Field'", "FAIL", f"Exception: {str(e)}")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Library_Locator.Register_Text))
            )
            logger.log("Verify 'Register Title'", "PASS", "Register title is visible")
        except Exception as e:
            logger.log("Verify 'Register Title'", "FAIL", f"Exception: {str(e)}")

        try:
            contacts = fetch_contacts()
            if contacts:
                name, email, password = contacts[0]

                try:
                    self.driver.find_element(By.XPATH, Library_Locator.Signup_Name).send_keys(name)
                    logger.log("Enter 'Name'", "PASS", f"Entered: {name}")
                except Exception as e:
                    logger.log("Enter 'Name'", "FAIL", f"Could not enter name: {e}")
                time.sleep(1)

                # Step 2: Enter Email
                try:
                    self.driver.find_element(By.XPATH, Library_Locator.Signup_Email).send_keys(email)
                    logger.log("Enter 'Email'", "PASS", f"Entered: {email}")
                except Exception as e:
                    logger.log("Enter 'Email'", "FAIL", f"Could not enter email: {e}")
                time.sleep(1)

                # Step 3: Enter Password
                try:
                    self.driver.find_element(By.XPATH, Library_Locator.Signup_Password).send_keys(password)
                    logger.log("Enter 'Password'", "PASS", "Entered password")
                except Exception as e:
                    logger.log("Enter 'Password'", "FAIL", f"Could not enter password: {e}")
                time.sleep(1)

                # Step 4: Click Submit
                try:
                    self.driver.find_element(By.XPATH, Library_Locator.Signup_Submit_Button).click()
                    logger.log("Click 'Submit Button'", "PASS", "Clicked Submit")
                except Exception as e:
                    logger.log("Click 'Submit Button'", "FAIL", f"Click failed: {e}")
                time.sleep(2)
        except Exception as e:
            logger.log("Register Page Flow", "FAIL", f"Exception: {str(e)}")


@pytest.mark.usefixtures("driver_init")
class TestDemo:
    def test_register_page(self):
        page = RegisterPage(self.driver)
        page.load()
        page.UI()
        page.Register_Page()
        time.sleep(2)