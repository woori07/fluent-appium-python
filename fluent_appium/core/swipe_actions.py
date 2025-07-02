from appium import webdriver

class SwipeActions:
    """좌표 기반 스와이프 액션"""
    def __init__(self, driver:webdriver.Remote):
        self._driver = driver
    
    def up(self, start_x, start_y, distance=200, duration=1000):
        """위로 스와이프"""
        self._driver.swipe(start_x, start_y, start_x, start_y - distance, duration)
        return self
    
    def down(self, start_x, start_y, distance=200, duration=1000):
        """아래로 스와이프"""
        self._driver.swipe(start_x, start_y, start_x, start_y + distance, duration)
        return self
    
    def screen_up(self, distance=300, duration=1000):
        """화면 전체 위로 스와이프"""
        size = self._driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 2 // 3
        self._driver.swipe(start_x, start_y, start_x, start_y - distance, duration)
        return self