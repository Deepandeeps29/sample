from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from report.custom_logger import CustomLogger
from Library.library import Library_Locator

logger = CustomLogger()

class Button_Page:
    def __init__(self, driver):
        try:
            self.driver = driver
            logger.log("Initialize Button Page", "PASS", "Driver initialized for Button Page")
        except Exception as e:
            logger.log("Initialize Button Page", "FAIL", f"Exception: {str(e)}")

    def load(self):
        try:
            self.driver.get(Library_Locator.Login_Url)
            logger.log("Open Qspider Webpage", "PASS", "Navigated to Qspiders successfully")
        except Exception as e:
            logger.log("Open Qspider Webpage", "FAIL", f"Exception: {str(e)}")

    def click_buttons(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Library_Locator.Button_Page))).click()
            logger.log("Click 'Button Section'", "PASS", "Clicked Button section successfully")
        except Exception as e:
            logger.log("Click 'Button Section'", "FAIL", f"Exception: {str(e)}")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Library_Locator.Button_Page_Text))
            )
            logger.log("Wait for Feedback Title", "PASS", "Feedback section is visible")
        except Exception as e:
            logger.log("Wait for Feedback Title", "FAIL", f"Exception: {str(e)}")

        try:
            self.driver.find_element(By.XPATH, Library_Locator.Button_Page_Yes_Button).click()
            logger.log("Click 'Yes' Button", "PASS", "Clicked Yes")
        except Exception as e:
            logger.log("Click 'Yes' Button", "FAIL", f"Exception: {str(e)}")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Library_Locator.Button_Page_Yes_Button_Text))
            )
            logger.log("Verify Response After 'Yes'", "PASS", "Response visible after clicking Yes")
        except Exception as e:
            logger.log("Verify Response After 'Yes'", "FAIL", f"Exception: {str(e)}")

        try:
            self.driver.find_element(By.XPATH, Library_Locator.Button_Page_No_Button).click()
            logger.log("Click 'No' Button", "PASS", "Clicked No")
        except Exception as e:
            logger.log("Click 'No' Button", "FAIL", f"Exception: {str(e)}")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Library_Locator.Button_Page_No_Button_Text))
            )
            logger.log("Verify Response After 'No'", "PASS", "Response visible after clicking No")
        except Exception as e:
            logger.log("Verify Response After 'No'", "FAIL", f"Exception: {str(e)}")

# if __name__ == "__main__":
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     driver.maximize_window()

#     page = Button_Page(driver)
#     page.load()
#     page.click_buttons()

#     time.sleep(2)
#     driver.quit()
#     logger.finalize()
