from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from report.custom_logger import CustomLogger
from Library.library import Library_Locator

logger = CustomLogger()

class RadioButton:
    def __init__(self, driver):
        try:
            self.driver = driver
            logger.log("Initialize RadioButton Page", "PASS", "Driver initialized for Radio Button page")
        except Exception as e:
            logger.log("Initialize RadioButton Page", "FAIL", f"Exception: {str(e)}")

    def load(self):
        try:
            self.driver.get(Library_Locator.Login_Url)
            logger.log("Open Qspider Webpage", "PASS", "Navigated to Qspiders")
        except Exception as e:
            logger.log("Open Qspider Webpage", "FAIL", f"Exception: {str(e)}")

    def Radio_Button(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Library_Locator.Radio_Button))).click()
            logger.log("Click 'Radio Button' Section", "PASS", "Radio Button section clicked")
        except Exception as e:
            logger.log("Click 'Radio Button' Section", "FAIL", f"Exception: {str(e)}")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Library_Locator.Radio_Button_Title))
            )
            logger.log("Wait for 'Checkout Page' Title", "PASS", "Checkout page title visible")
        except Exception as e:
            logger.log("Wait for 'Checkout Page' Title", "FAIL", f"Exception: {str(e)}")

        # Select UPI Option
        try:
            self.driver.find_element(By.XPATH, Library_Locator.Radio_Button_Payment_1).click()
            logger.log("Select UPI Option", "PASS", "UPI selected")
            time.sleep(1)
        except Exception as e:
            logger.log("Select UPI Option", "FAIL", f"Exception: {str(e)}")

        # Select COD Option
        try:
            self.driver.find_element(By.XPATH, Library_Locator.Radio_Button_Payment_2).click()
            logger.log("Select COD Option", "PASS", "Cash on Delivery selected")
            time.sleep(1)
        except Exception as e:
            logger.log("Select COD Option", "FAIL", f"Exception: {str(e)}")

        # Select Delivery Location
        try:
            self.driver.find_element(By.XPATH, Library_Locator.Radio_Button_Delivery).click()
            logger.log("Select Delivery Location", "PASS", "Home delivery selected")
            time.sleep(1)
        except Exception as e:
            logger.log("Select Delivery Location", "FAIL", f"Exception: {str(e)}")

        # Click Continue Button
        try:
            self.driver.find_element(By.XPATH, Library_Locator.Radio_Button_Continue).click()
            logger.log("Click 'Continue' Button", "PASS", "Continue clicked")
        except Exception as e:
            logger.log("Click 'Continue' Button", "FAIL", f"Exception: {str(e)}")

# if __name__ == "__main__":
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     page = RadioButton(driver)
#     page.load()
#     page.Radio_Button()
#     driver.quit()
#     logger.finalize()
