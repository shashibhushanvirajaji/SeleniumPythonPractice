from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.mark.usefixtures('initialize_driver')
class Baseclass:
    pass


class TestGoogle(Baseclass):
    def test_google_title(self):
        self.driver.get('https://www.google.com/')
        assert self.driver.title == 'Google'
