import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'tema1255')
@allure.feature('Проверка наличия Issue на github')
@allure.story('Лямбда шаги через with allure.step')
@allure.link('https://github.com', name='Testing')
def test_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('tema1255/qa_guru_hw_4_9')
        s('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('tema1255/qa_guru_hw_4_9')).click()

    with allure.step('Ищем таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue на странице'):
        s(by.partial_text('#1')).should(be.visible)
