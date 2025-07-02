from .fluent_element import FluentElement

class PageObject:
    """page 객체 - 요소 기반과 액션 기반 모두 지원"""
    
    def __init__(self, get_driver_func):
        self._swipe = None
        self._get_driver = get_driver_func
    
    def __call__(self, locator, driver=None):
        """page(locator) 방식으로 사용"""
        if driver is None:
            driver = self._get_driver()
        return FluentElement(locator, driver)
    
    @property
    def swipe(self):
        """page.swipe.up() 방식으로 사용"""
        if self._swipe is None:
            from .swipe_actions import SwipeActions
            self._swipe = SwipeActions(self._get_driver())
        return self._swipe