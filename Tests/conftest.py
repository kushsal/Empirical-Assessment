from selenium import webdriver
from TestData.URLData import get_url_for_testcase
import pytest
import os
from Utilities.CommonUtilities import BaseDriverCode
from pytest_html import extras

#Intiate Selenium driver object for Chrome browser
driver = None
@pytest.fixture(scope="function")
def setupBrowser(request):
    #service_obj = Service(r"C:\Users\Kusha\PycharmProjects\Driver\chromedriver.exe")
    chrome_options =webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

#Fixture to do logging of all events in log file
""" 
@pytest.fixture(scope="class", autouse=True)
def logger(request):
    log_obj = BaseDriverCode()
    request.cls.log = log_obj.getLogger()
    request.cls.log = logger
    return logger
"""

#Fixture to add per test logger that will create individual log files per test case
@pytest.fixture(scope="function", autouse=True)
def per_test_logger(request):
    base = BaseDriverCode()
    logger, log_path = base.getLogger(request.node.nodeid)

    # Attach logger to test class
    if hasattr(request, "cls"):
        request.cls.log = logger

    # Store log path for embedding into pytest-html
    request.node._log_path = log_path
    return logger


# Fixture to define report path
@pytest.fixture(scope="session", autouse=True)
def configure_reports(request):
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    report_file = os.path.join(reports_dir, "report.html")

    # Add custom pytest-html report path
    request.config.option.htmlpath = report_file
    request.config.option.self_contained_html = True
    print(f"\nReports will be generated at: {report_file}")

#This is a hook that - Runs after each test, Reads the per‑test log file and embeds its contents into the HTML report under “Execution Log”.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Attach logs
        log_path = getattr(item, "_log_path", None)
        if log_path and os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                content = f.read()
            extra = getattr(report, "extra", [])
            extra.append(extras.text(content, name="Execution Log"))
            report.extra = extra

        # Attach screenshot if test failed
        if report.failed:
            driver = getattr(item.cls, "driver", None)
            if driver:
                screenshot_path = os.path.join(os.getcwd(), "reports", f"{item.nodeid.replace('::','_')}.png")
                driver.save_screenshot(screenshot_path)

                extra = getattr(report, "extra", [])
                extra.append(extras.image(screenshot_path, name="Failure Screenshot"))
                report.extra = extra

#Fixture to pick URLs for executing both Test cases from an excel sheet (DDT approach)
@pytest.fixture(scope="function")
def test_url(request, per_test_logger):
    file_path = os.path.join(os.getcwd(), "TestData", "List_of_URLs.xlsx")
    testcase_name = request.node.name.split("::")[-1]
    print(f"Excel path: {file_path}")
    per_test_logger.info(f"Excel path: {file_path}")
    print(f"Test Case name: {testcase_name}")
    per_test_logger.info(f"Test Case name: {testcase_name}")
    url = get_url_for_testcase(file_path, testcase_name)
    if not url:
        pytest.skip("No URLs present in Excel..")
        per_test_logger.debug(f"No URLs present in Excel..")
    return url
