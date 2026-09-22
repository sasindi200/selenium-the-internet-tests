import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver_path():
    return ChromeDriverManager().install()


@pytest.fixture
def driver(driver_path):
    service = Service(driver_path)
    drv = webdriver.Chrome(service=service)
    drv.implicitly_wait(0)
    drv.maximize_window()
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(f"screenshots/{item.name}.png")