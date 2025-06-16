from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from report.custom_logger import CustomLogger
from Library.library import Library_Locator

logger = CustomLogger()

class Check_Page:
    def __init__(self, driver):
        try:
            self.driver = driver
            logger.log("Initialize Check Page", "PASS", "Driver initialized for Check Page")
        except Exception as e:
            logger.log("Initialize Check Page", "FAIL", f"Exception: {str(e)}")

    def load(self):
        try:
            self.driver.get(Library_Locator.Login_Url)
            logger.log("Open Qspider Webpage", "PASS", "Navigated to Qspiders successfully")
            time.sleep(2)
        except Exception as e:
            logger.log("Open Qspider Webpage", "FAIL", f"Exception: {str(e)}")



    def Check_Box(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Library_Locator.CheckBox_Button))).click()
            logger.log("Click 'Check Box'", "PASS", "Clicked on Check Box section")
            time.sleep(2)
        except Exception as e:
            logger.log("Click 'Check Box'", "FAIL", f"Exception: {str(e)}")

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Library_Locator.CheckBox_Button_Text)))
            logger.log("Wait for 'Checkout Page'", "PASS", "Checkout Page is visible")
            time.sleep(2)
        except Exception as e:
            logger.log("Wait for 'Checkout Page'", "FAIL", f"Exception: {str(e)}")

        try:
            self.driver.find_element(By.XPATH, Library_Locator.CheckBox_Select_Domain).click()
            logger.log("Select Domain", "PASS", "Selected first domain option")
            time.sleep(2)
        except Exception as e:
            logger.log("Select Domain", "FAIL", f"Exception: {str(e)}")

        try:
            self.driver.find_element(By.XPATH, Library_Locator.CheckBox_Select_mode).click()
            logger.log("Select Product", "PASS", "Selected 'Sandals' option")
            time.sleep(2)
        except Exception as e:
            logger.log("Select Product", "FAIL", f"Exception: {str(e)}")

        # try:
        #     self.scroll_to_element(Library_Locator.CheckBox_Submit_Button)
        #     logger.log("Scroll to Submit Button", "PASS", "Scrolled to submit button")
        #     time.sleep(2)
        # except Exception as e:
        #     logger.log("Scroll to Submit Button", "FAIL", f"Exception: {str(e)}")

        try:
            self.driver.find_element(By.XPATH, Library_Locator.CheckBox_Select_mode_2).click()
            logger.log("Select Radio Option", "PASS", "Selected 'Regarding the same product'")
            time.sleep(2)
        except Exception as e:
            logger.log("Select Radio Option", "FAIL", f"Exception: {str(e)}")

        try:
            self.driver.find_element(By.XPATH, Library_Locator.CheckBox_Submit_Button).click()
            logger.log("Click Submit", "PASS", "Clicked Submit button")
            time.sleep(2)
        except Exception as e:
            logger.log("Click Submit", "FAIL", f"Exception: {str(e)}")

    # def scroll_to_element(self, xpath):
    #     try:
    #         element = self.driver.find_element(By.XPATH, xpath)
    #         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #         time.sleep(1)
    #     except Exception as e:
    #         logger.log("Scroll to Element", "FAIL", f"Exception: {str(e)}")
#
# if __name__ == "__main__":
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     page = Check_Page(driver)
#     page.load()
#     page.UI()
#     page.Check_Box()
#     driver.quit()
#     logger.finalize()
