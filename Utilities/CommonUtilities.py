import logging
import os
import inspect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseDriverCode:
    def verifyElementPresence(self, search_criteria):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, search_criteria)))
        return element

    def getLogger(self, test_name=None):
        """
        Create a per-test logger. If test_name is not passed,
        derive it from the calling function.
        """
        if not test_name:
            test_name = inspect.stack()[1][3]

        safe_name = test_name.replace("/", "_").replace("::", "_")
        log_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, f"{safe_name}.log")
        logger = logging.getLogger(safe_name)
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:  # prevent duplicate handlers
            fileHandler = logging.FileHandler(log_file, encoding="utf-8")
            formatter = logging.Formatter(
                "%(asctime)s :%(levelname)s :%(name)s :%(message)s"
            )
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)

        return logger, log_file

    """    
    def getLogger(self):
            loggerName = inspect.stack()[1][3] #code to get the name of the test file thats calling the getLogger method
            logger = logging.getLogger(loggerName) #creating a logger object with passing the calling test file as argument
            if not logger.handlers:  # prevent duplicate handlers
                fileHandler = logging.FileHandler('logfile.log', encoding='utf-8') #created a file handler object
                formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s") #Setting logging format
                fileHandler.setFormatter(formatter) #passing the formatter to the file handler object
                logger.addHandler(fileHandler) #FileHandler object
                logger.setLevel(logging.DEBUG)
            return logger
    """