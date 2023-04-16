import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # browser.driver.set_window_size(1400, 960)
    browser.config.base_url = 'https://demoqa.com'
