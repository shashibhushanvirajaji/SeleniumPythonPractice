from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import pytest


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    chDriver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = chDriver
    yield
    chDriver.quit()

@pytest.fixture(scope='class')
def init_firefox_driver(request):
    ffDriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ffDriver
    yield
    ffDriver.quit()

@pytest.mark.usefixtures('init_firefox_driver')
class BaseClassFireFox:
    pass

@pytest.mark.usefixtures('init_chrome_driver')
class BaseClassChrome:
    pass

class TestGoogleChrome(BaseClassChrome):
    def test_google_title(self):
        self.driver.get('https://www.google.com/')
        assert self.driver.title == 'Google'


class TestGoogleFireFox(BaseClassFireFox):
    def test_google_title_firefox(self):
        self.driver.get('https://www.google.com/')
        assert self.driver.title == 'Google'
