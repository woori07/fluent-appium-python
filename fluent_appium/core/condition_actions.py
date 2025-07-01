from appium import webdriver
from ..chains.input_chain import InputChain
from ..chains.get_chain import GetChain

class ConditionActions:
    """조건부 대기 후 액션 가능 + 자체적으로도 종료 가능한 클래스"""
    def __init__(self, locator, driver: webdriver.Remote, timeout=10):
        self.locator = locator
        self.driver = driver
        self.timeout = timeout
    
    @property
    def click(self):
        """클릭 실행 - 종료"""
        element = self.driver.find_element(*self.locator)
        element.click()
        return None  # 체이닝 종료
    
    @property
    def get(self):
        """속성 및 텍스트 가져오기 - 종료"""
        return GetChain(self.locator, self.driver, self.timeout)
    
    def input_text(self, text):
        """텍스트 입력 - 종료"""
        return InputChain(self.locator, self.driver, self.timeout, text)
    
    def __bool__(self):
        """조건 확인 결과 반환 (항상 True, 이미 조건을 만족했으므로)"""
        return True