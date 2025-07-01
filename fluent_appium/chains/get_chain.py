from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GetChain:
    def __init__(self, locator, driver, timeout):
        self.locator = locator
        self.driver = driver
        self.timeout = timeout
    
    @property
    def text(self):
        """요소의 텍스트 반환"""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.locator)
        )
        return element.text
    
    def attribute(self, attr_name):
        """특정 속성값 반환"""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.locator)
        )
        return element.get_attribute(attr_name)
    
    @property
    def size(self):
        """요소 크기 반환"""
        element = self.driver.find_element(*self.locator)
        return element.size
    
    @property
    def location(self):
        """요소 위치 반환"""
        element = self.driver.find_element(*self.locator)
        return element.location