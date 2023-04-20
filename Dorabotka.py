import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def brow():
    browser.open('https://google.com')
    browser.driver.set_window_size(3200, 2000)
    yield
    browser.close()


def test_size_brow(brow):
    browser.element('[name="q"]').should(be.blank).set_value('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search(brow):
    browser.element('[name="q"]').should(be.blank).set_value('sfdahansdnsdfgnsr').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('По результату теста Search ничего не найдено')
