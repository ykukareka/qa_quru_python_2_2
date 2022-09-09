from selene.support.shared import browser
from selene import have
import pytest


@pytest.fixture()
def browser_size():
    browser.config.browser_name = 'chrome'
    browser.config.window_width, browser.config.window_height = 1280, 720
    browser.open('https://google.com/ncr')
    yield
    browser.close()


def test_successful(browser_size):
    browser.element('[name=q]').type('selene').press_enter()
    browser.element('[aria-label="Page 2"]').click()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_unsuccessful(browser_size):
    browser.element('[name=q]').type('444r33efgh6667jjnbvff!@@@').press_enter()
    browser.element('[id=search]').should(have.no.text('444r33efgh6667jjnbvff!@@@'))
