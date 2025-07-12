from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from ..chains.input_chain import InputChain
from ..chains.get_chain import GetChain
from .condition_actions import ConditionActions
from ..utils.debug_helper import strip_stacktrace

class FluentElement:
    def __init__(self, locator, driver: webdriver.Remote, timeout=10):
        self._locator = locator
        self._driver = driver
        self._timeout = timeout
        self._wait = WebDriverWait(driver, timeout)
        
    def wait(self, timeout):
        """새로운 타임아웃으로 체이닝 계속"""
        return FluentElement(self._locator, self._driver, timeout)
    
    @property
    def is_visible(self):
        """요소가 보일 때까지 대기"""
        try:
            self._wait.until(EC.visibility_of_element_located(self._locator))
            return ConditionActions(self._locator, self._driver, self._timeout)
        except TimeoutException as exc:
            raise TimeoutException(strip_stacktrace(f"Element {self._locator} not visible within {self._timeout}s: {exc}"))
    
    @property
    def is_invisible(self):
        """요소가 사라질 때까지 대기"""
        try:
            self._wait.until(EC.invisibility_of_element_located(self._locator))
            return ConditionActions(self._locator, self._driver, self._timeout)
        except TimeoutException as exc:
            raise TimeoutException(strip_stacktrace(f"Element {self._locator} still visible after {self._timeout}s: {exc}"))
    
    @property
    def is_all_visible(self):
        """모든 요소가 보일 때까지 대기 (복수 요소)"""
        try:
            self._wait.until(EC.visibility_of_all_elements_located(self._locator))
            return ConditionActions(self._locator, self._driver, self._timeout)
        except TimeoutException as exc:
            raise TimeoutException(strip_stacktrace(f"Not all elements {self._locator} visible within {self._timeout}s: {exc}"))
    
    @property
    def is_any_visible(self):
        """요소 중 하나라도 보일 때까지 대기"""
        try:
            self._wait.until(EC.visibility_of_any_elements_located(self._locator))
            return ConditionActions(self._locator, self._driver, self._timeout)
        except TimeoutException as exc:
            raise TimeoutException(strip_stacktrace(f"No elements {self._locator} visible within {self._timeout}s: {exc}"))
    
    @property
    def is_clickable(self):
        """클릭 가능할 때까지 대기"""
        try:
            self._wait.until(EC.element_to_be_clickable(self._locator))
            return ConditionActions(self._locator, self._driver, self._timeout)
        except TimeoutException as exc:
            raise TimeoutException(strip_stacktrace(f"Element {self._locator} not clickable within {self._timeout}s: {exc}"))
    
    @property
    def click(self):
        """즉시 클릭 - 종료"""
        element = self._driver.find_element(*self._locator)
        element.click()
        return None  # 체이닝 종료
    
    @property
    def get(self):
        """속성 및 텍스트 가져오기 - 종료"""
        return GetChain(self._locator, self._driver, self._timeout)
    
    def input_text(self, text):
        """텍스트 입력 - 종료"""
        return InputChain(self._locator, self._driver, self._timeout, text)
