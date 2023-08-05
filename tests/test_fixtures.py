"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene.support.shared import browser, config
from selene import browser, have


@pytest.fixture
def open_browser_desktop():
    config.timeout = 5
    config.window_width = 1280
    config.window_height = 720
    config.base_url = 'https://github.com'
    yield
    browser.quit()

@pytest.fixture
def open_browser_mobile():
    config.timeout = 5
    config.window_width = 320
    config.window_height = 720
    config.base_url = 'https://github.com'
    yield
    browser.quit()


def test_github_desktop(open_browser_desktop):
    browser.open('')
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(open_browser_mobile):
    browser.open('')
    browser.element('[class="Button-content"]').click()
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
