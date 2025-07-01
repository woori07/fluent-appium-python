from ..chains.input_chain import InputChain
from ..chains.get_chain import GetChain
from ..chains.swipe_chain import SwipeChain

class Actions:
    def __init__(self, locator, driver, timeout=10):
        self.locator = locator
        self.driver = driver
        self.timeout = timeout
    
    @property
    def click(self):
        """클릭 실행"""
        element = self.driver.find_element(*self.locator)
        element.click()
        return self
    
    @property
    def get(self):
        """속성 및 텍스트 가져오기"""
        return GetChain(self.locator, self.driver, self.timeout)
    
    def input_text(self, text):
        """텍스트 입력"""
        return InputChain(self.locator, self.driver, self.timeout, text)
    
    @property
    def swipe(self):
        """스와이프 시작"""
        return SwipeChain(self.locator, self.driver, self.timeout)
    
    def wait(self, timeout):
        """추가 대기"""
        from .fluent_element import FluentElement
        return FluentElement(self.locator, self.driver, timeout)