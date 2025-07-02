"""
Fluent Appium - A fluent interface for Appium automation

Example:
    >>> from fluent_appium import page, set_driver
    >>> set_driver(driver)
    >>> page(locator).wait(10).is_visible.click
"""

from .core.page_object import PageObject

__version__ = "0.1.0"

# 전역 드라이버 관리
_global_driver = None

def set_driver(driver):
    """전역 드라이버 설정
    
    Args:
        driver: Appium WebDriver 인스턴스
    """
    global _global_driver
    _global_driver = driver

def _get_global_driver():
    """전역 드라이버 반환"""
    if _global_driver is None:
        raise RuntimeError("Driver not set. Call set_driver() or pass driver to page()")
    return _global_driver

# 전역 인스턴스
page = PageObject(_get_global_driver)

__all__ = ["page", "set_driver"]