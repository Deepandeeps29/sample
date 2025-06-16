from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from data.db import fetch_contacts
from report.custom_logger import CustomLogger
from Library.library import Library_Locator

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

logger = CustomLogger()

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        logger.log("Initialize Signup Page", "PASS", "Driver initialized for Signup")

    def load(self):
        try:
            self.driver.get(Library_Locator.Login_Url)
            logger.log("Open Signup URL", "PASS", "Navigated to Login page")
            time.sleep(2)


        except Exception as e:
            logger.log("Open Signup URL", "FAIL", f"Exception: {str(e)}")

    def Signup_Page(self):
        try:
            data = fetch_contacts()
            if data:
                name, email, password = data[0]

                try:
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Library_Locator.Login_Page_Text)))
                    logger.log("Verify Login Page", "PASS", "Login heading is visible")
                except Exception as e:
                    logger.log("Verify Login Page", "FAIL", f"Login heading not visible: {e}")

                try:
                    self.driver.find_element(By.XPATH, Library_Locator.Login_Email).send_keys(email)
                    logger.log("Enter Email", "PASS", f"Entered email: {email}")
                except Exception as e:
                    logger.log("Enter Email", "FAIL", f"Could not enter email: {e}")
                    # raise
                time.sleep(1)  # Can be replaced with a wait if needed

                try:
                    self.driver.find_element(By.XPATH, Library_Locator.Login_Password).send_keys(password)
                    logger.log("Enter Password", "PASS", "Entered password")
                except Exception as e:
                    logger.log("Enter Password", "FAIL", f"Could not enter password: {e}")
                time.sleep(1)

                try:
                    self.driver.find_element(By.XPATH, Library_Locator.Login_Submit_Button).click()
                    logger.log("Click Submit", "PASS", "Clicked Submit button")
                except Exception as e:
                    logger.log("Click Submit", "FAIL", f"Submit button click failed: {e}")
                time.sleep(2)
            else:
                logger.log("Fetch Contacts", "FAIL", "No contact data returned from DB")
        except Exception as e:
            logger.log("Signup Page", "FAIL", f"Exception: {str(e)}")
