"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selenium import webdriver
from selene import browser, have

@pytest.fixture(params=[
    (2280, 720),
    (320, 180)
])
def browser_type(request):
    browser.config.driver_options = webdriver.ChromeOptions()

    browser.config.window_height = request.param[1]
    browser.config.window_width = request.param[0]

    browser.config.base_url = 'https://github.com'

    yield browser
    browser.quit()

desktop = pytest.mark.parametrize('browser_type', [(2280, 720)], indirect=True)
mobile = pytest.mark.parametrize('browser_type', [(320, 180)], indirect=True)

@desktop
def test_github_desktop(browser_type):
    browser.open('')
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


@mobile
def test_github_mobile(browser_type):
    browser.open('')
    browser.element('[class="Button-content"]').click()
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
