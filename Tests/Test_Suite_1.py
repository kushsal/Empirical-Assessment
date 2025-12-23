import pytest
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException, \
    ElementNotInteractableException
from Utilities.CommonUtilities import BaseDriverCode
from POM.Link1 import link_1

@pytest.mark.usefixtures("setupBrowser")
class TestCase1(BaseDriverCode):
    def test_case1(self, test_url):
        try:
            self.driver.get(test_url)
            self.verifyElementPresence("//button[text()='Click me']").click()
            #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Click me']"))).click()
            handles = self.driver.window_handles
            assert len(handles) > 1
            self.driver.switch_to.window(handles[-1])
            signup_btn = self.verifyElementPresence('//div[@class="ml-auto flex gap-2 items-center"]//button[2]')
            #signup_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="ml-auto flex gap-2 items-center"]//button[2]')))
            assert signup_btn.is_displayed()
            assert signup_btn.is_enabled()
        except (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException,
                    ElementNotInteractableException) as e:
            pytest.fail(f"There was some error in locating the element: {e}")

    def test_case2(self, test_url):
        try:
            self.driver.get(test_url)
            testlink = link_1(self.driver)
            testlink.switchToiFrame()
            #self.driver.switch_to.frame("iframeResult")
            self.verifyElementPresence('//a[contains(text(), "W3School")]').click()
            #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "W3School")]'))).click()
            handles = self.driver.window_handles
            assert len(handles) > 1
            self.driver.switch_to.window(handles[-1])
            search_area = self.verifyElementPresence('//input[@id = "search2"]')
            #search_area = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id = "search2"]')))
            assert search_area.is_displayed()
            assert search_area.is_enabled()
        except (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException, ElementNotInteractableException) as e:
            pytest.fail(f"There was some error in locating the element: {e}")