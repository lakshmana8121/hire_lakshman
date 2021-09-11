import pytest
from selenium import webdriver
@pytest.fixture
def setup():
    driver=webdriver.Chrome('C:\\driver\\chromedriver.exe')
    driver.implicitly_wait(5)
    return driver