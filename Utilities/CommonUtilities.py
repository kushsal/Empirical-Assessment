import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setupBrowser")
class BaseDriverCode:
    def verifyElementPresence(self, search_criteria):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, search_criteria)))
        return element


