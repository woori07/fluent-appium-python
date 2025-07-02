# Fluent Appium

A fluent wrapper around Appium that transforms complex mobile automation into simple, readable test code.

## 🚀 Features

- **Fluent API**: Chain methods for natural, readable test code
- **Smart Waiting**: Built-in intelligent waiting for elements
- **Element Interactions**: Click, input, swipe, and more
- **Condition Checking**: Visibility, clickability, and other states
- **Swipe Actions**: Both element-based and coordinate-based swiping
- **Cross-Platform**: Works with iOS and Android apps

## 📦 Installation

```bash
pip install fluent-appium
```

## 🎯 Quick Start

```python
from fluent_appium import page, set_driver
from appium import webdriver

# Set up your Appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
set_driver(driver)

# Use fluent API
page(("id", "username")).wait(10).input_text("user@example.com")
page(("id", "password")).input_text("password123")
page(("id", "login-btn")).wait(5).is_clickable.click
```

## 📚 API Reference

### Basic Element Interactions

```python
# Element selection and waiting
page(locator).wait(10)                    # Wait with timeout
page(locator).is_visible                  # Wait until visible
page(locator).is_clickable               # Wait until clickable
page(locator).is_invisible               # Wait until invisible

# Actions
page(locator).click                      # Click element
page(locator).input_text("hello")       # Input text
page(locator).get.text                  # Get element text
page(locator).get.attribute("value")    # Get attribute
```

### Chaining Examples

```python
# Wait and then perform action
page(locator).wait(10).is_visible.click

# Input text and press enter
page(locator).input_text("search term").enter

# Multiple conditions
page(locator).wait(5).is_visible.input_text("data")

# Conditional actions
if page(popup_locator).wait(3).is_visible:
    page(close_button).click
```


## 🔧 Locator Examples

```python
from appium.webdriver.common.appiumby import AppiumBy

# Appium locators
start_btn = (AppiumBy.ACCESSIBILITY_ID, "accessibility-id")
login_btn = (AppiumBy.ID, "login-button")
text_field = (AppiumBy.XPATH, "//input[@type='text']")

# Usage
page(start_btn).wait(10).click
page(login_btn).is_clickable.click
page(text_field).input_text("Hello World")
```

## ⚙️ Configuration

### Driver Setup

```python
from appium import webdriver
from fluent_appium import set_driver

# Android example
android_caps = {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.example.app',
    'appActivity': '.MainActivity'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', android_caps)
set_driver(driver)
```

### Timeout Management

```python
# Global timeout (applies to all subsequent operations)
page(locator).wait(20).is_visible.click

# Individual operation timeouts
page(locator).wait(5).input_text("fast input")
page(slow_locator).wait(30).is_visible.click
```

## 🧪 Testing Examples

### Page Object Pattern

```python
class LoginPage:
    def __init__(self):
        self.username_field = ("id", "username")
        self.password_field = ("id", "password") 
        self.login_button = ("id", "login-btn")
        self.error_message = ("id", "error-msg")
    
    def login(self, username, password):
        page(self.username_field).wait(10).input_text(username)
        page(self.password_field).input_text(password)
        page(self.login_button).click
        
    def get_error_message(self):
        return page(self.error_message).wait(5).get.text
```

### Pytest Integration

```python
import pytest
from fluent_appium import set_driver, page

@pytest.fixture
def driver():
    # Setup driver
    driver = create_appium_driver()
    set_driver(driver)
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage()
    login_page.login("user@test.com", "password")
    
    assert page(("id", "welcome")).wait(10).is_visible
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on top of [Appium](https://appium.io/)
- Inspired by fluent interface patterns in modern testing frameworks

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/woori07/fluent-appium/issues)
- **Documentation**: [GitHub README](https://github.com/woori07/fluent-appium#readme)
- **Source Code**: [GitHub Repository](https://github.com/woori07/fluent-appium)