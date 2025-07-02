from appium import webdriver

class SwipeChain:
    def __init__(self, locator, driver: webdriver.Remote, timeout):
        self.locator = locator
        self.driver = driver
        self.timeout = timeout
    
    def up(self, distance=200, duration=1000):
        """요소 중심에서 위로 스와이프"""
        element = self.driver.find_element(*self.locator)
        center_x = element.location['x'] + element.size['width'] // 2
        center_y = element.location['y'] + element.size['height'] // 2
        end_y = center_y - distance
        
        self.driver.swipe(center_x, center_y, center_x, end_y, duration)
        return self
    
    def down(self, distance=200, duration=1000):
        """요소 중심에서 아래로 스와이프"""
        element = self.driver.find_element(*self.locator)
        center_x = element.location['x'] + element.size['width'] // 2
        center_y = element.location['y'] + element.size['height'] // 2
        end_y = center_y + distance
        
        self.driver.swipe(center_x, center_y, center_x, end_y, duration)
        return self
    
    def left(self, distance=200, duration=1000):
        """요소 중심에서 왼쪽으로 스와이프"""
        element = self.driver.find_element(*self.locator)
        center_x = element.location['x'] + element.size['width'] // 2
        center_y = element.location['y'] + element.size['height'] // 2
        end_x = center_x - distance
        
        self.driver.swipe(center_x, center_y, end_x, center_y, duration)
        return self
    
    def right(self, distance=200, duration=1000):
        """요소 중심에서 오른쪽으로 스와이프"""
        element = self.driver.find_element(*self.locator)
        center_x = element.location['x'] + element.size['width'] // 2
        center_y = element.location['y'] + element.size['height'] // 2
        end_x = center_x + distance
        
        self.driver.swipe(center_x, center_y, end_x, center_y, duration)
        return self