"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest
from selenium import webdriver
from selene import browser, have

@pytest.fixture(params=[
    (2280, 720),
    (320, 180)],
    ids=[
    'desktop',
    'mobile'
])
def browser_type(request):
    browser.config.driver_options = webdriver.ChromeOptions()
    id = request.node.callspec.id
    browser.config.window_height = request.param[1]
    browser.config.window_width = request.param[0]

    browser.config.base_url = 'https://github.com'

    yield browser, id

    browser.quit()

desktop = pytest.mark.parametrize('browser_type', [(2280, 720)], indirect=True)
mobile = pytest.mark.parametrize('browser_type', [(320, 180)], indirect=True)

@desktop
def test_github_desktop(browser_type):
    browser, id = browser_type
    if 'mobile' in id:
        pytest.skip('Mobile type browser is not suitable for the browser')
    browser.open('')
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


@mobile
def test_github_mobile(browser_type):
    browser, id = browser_type
    if 'desktop' in id:
        pytest.skip('Desktop type browser is not suitable for the browser')
    browser.open('')
    browser.element('[class="Button-content"]').click()
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
