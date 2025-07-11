from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InputChain:
    def __init__(self, locator, driver: webdriver.Remote, timeout, text):
        self._locator = locator
        self._driver = driver
        self._timeout = timeout
        self._text = text
        
        # 즉시 텍스트 입력 실행
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)
    
    @property
    def enter(self):
        """엔터 키 입력"""
        element = self._driver.find_element(*self._locator)
        element.send_keys(Keys.RETURN)
        return self
    
    @property
    def tab(self):
        """탭 키 입력"""
        element = self._driver.find_element(*self._locator)
        element.send_keys(Keys.TAB)
        return self
    
    def wait(self, timeout):
        """추가 대기"""
        from ..core.fluent_element import FluentElement
        return FluentElement(self._locator, self._driver, timeout)