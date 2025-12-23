
class link_1:
    def __init__(self, driver):
        self.driver = driver
        self.iFrame1 = "iframeResult"

    def switchToiFrame(self):
        return self.driver.switch_to.frame(self.iFrame1)