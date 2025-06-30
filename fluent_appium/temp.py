from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class FluentLocator:
    def __init__(self, locator_tuple, driver):
        self.locator = locator_tuple  # (By.CSS_SELECTOR, "selector")
        self.driver = driver
        
    def wait(self, timeout=10):
        """대기 후 체이닝 계속"""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.locator)
        )
        return self
        
    @property
    def click(self):
        """클릭 실행"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.click()
        return self
        
    def input(self, text):
        """텍스트 입력"""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator)
        )
        element.clear()
        element.send_keys(text)
        return InputChain(self.driver, self.locator)
        
    def swipe(self):
        """스와이프 체이닝 시작"""
        return SwipeChain(self.driver, self.locator)

class InputChain:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        
    @property
    def enter(self):
        """엔터 키 입력"""
        element = self.driver.find_element(*self.locator)
        element.send_keys(Keys.RETURN)
        return self

class SwipeChain:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        
    def up(self, duration=1000):
        """위로 스와이프"""
        element = self.driver.find_element(*self.locator)
        self.driver.swipe(
            element.location['x'], 
            element.location['y'],
            element.location['x'], 
            element.location['y'] - 200,
            duration
        )
        return self