from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(params=['chrome', 'firefox'], scope='class', i)
def initialize_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.implicitly_wait(10)
        web_driver.maximize_window()
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        web_driver.implicitly_wait(10)
        web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.quit()


@pytest.mark.usefixtures('initialize_driver')
class Baseclass:
    pass


class TestGoogle(Baseclass):
    def test_google_title(self):
        self.driver.get('https://www.google.com/')
        assert self.driver.title == 'Google'
