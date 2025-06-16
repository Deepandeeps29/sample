import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def driver_init(request):
    options = Options()
    # options - disabling popups
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--password-store=basic")
    options.add_argument("--suppress-message-center-popups")

    driver = webdriver.Chrome(options=options)     # setup Run before
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()                        #teardown

