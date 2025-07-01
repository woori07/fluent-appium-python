from .core.fluent_element import FluentElement

__version__ = "0.1.0"

def page(locator, driver=None):
    """FluentElement 생성 함수"""
    if driver is None:
        driver = _get_global_driver()
    return FluentElement(locator, driver)

# 전역 드라이버 관리
_global_driver = None

def set_driver(driver):
    """전역 드라이버 설정"""
    global _global_driver
    _global_driver = driver

def _get_global_driver():
    """전역 드라이버 반환"""
    if _global_driver is None:
        raise RuntimeError("Driver not set. Call set_driver() or pass driver to page()")
    return _global_driver

# 제스처 액션 클래스들
class _SwipeActions:
    def __init__(self, driver):
        self.driver = driver
    
    def from_element(self, locator):
        from .chains.swipe_chain import SwipeChain
        return SwipeChain(locator, self.driver, 10)
    
    def up(self, start_x, start_y, distance=200, duration=1000):
        self.driver.swipe(start_x, start_y, start_x, start_y - distance, duration)
        return self

# 제스처 인스턴스
swipe = _SwipeActions

__all__ = ["page", "set_driver", "swipe"]