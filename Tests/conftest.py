from selenium import webdriver
from TestData.URLData import get_url_for_testcase
import pytest
import os

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
    yield
    driver.quit()

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

#Fixture to pick URLs for executing both Test cases from an excel sheet (DDT approach)
@pytest.fixture(scope="function")
def test_url(request):
    file_path = os.path.join(os.getcwd(), "TestData", "List_of_URLs.xlsx")
    testcase_name = request.node.name.split("::")[-1]
    print(f"Excel path: {file_path}")
    print(f"Test Case name: {testcase_name}")
    url = get_url_for_testcase(file_path, testcase_name)
    if not url:
        pytest.skip("No URLs present in Excel..")
    return url