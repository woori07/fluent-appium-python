class SwipeChain:
    def __init__(self, locator, driver, timeout):
        self.locator = locator
        self.driver = driver
        self.timeout = timeout
    
    def up(self, duration=1000):
        """위로 스와이프"""
        element = self.driver.find_element(*self.locator)
        start_x = element.location['x'] + element.size['width'] // 2
        start_y = element.location['y'] + element.size['height'] // 2
        end_y = start_y - 200
        
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        return self
    
    def down(self, duration=1000):
        """아래로 스와이프"""
        element = self.driver.find_element(*self.locator)
        start_x = element.location['x'] + element.size['width'] // 2
        start_y = element.location['y'] + element.size['height'] // 2
        end_y = start_y + 200
        
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        return self
    
    def left(self, duration=1000):
        """왼쪽으로 스와이프"""
        element = self.driver.find_element(*self.locator)
        start_x = element.location['x'] + element.size['width'] // 2
        start_y = element.location['y'] + element.size['height'] // 2
        end_x = start_x - 200
        
        self.driver.swipe(start_x, start_y, end_x, start_y, duration)
        return self
    
    def right(self, duration=1000):
        """오른쪽으로 스와이프"""
        element = self.driver.find_element(*self.locator)
        start_x = element.location['x'] + element.size['width'] // 2
        start_y = element.location['y'] + element.size['height'] // 2
        end_x = start_x + 200
        
        self.driver.swipe(start_x, start_y, end_x, start_y, duration)
        return self