import allure
from selene.support import by
from allure_commons.types import Severity
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'tema1255')
@allure.feature('Проверка наличия Issue на github')
@allure.story('Чистый Selene (без шагов)')
@allure.link('https://github.com', name='Testing')
def test_github():
    browser.open('https://github.com')



    s('.header-search-input').click()
    s('.header-search-input').send_keys('tema1255/qa_guru_hw_4_9')
    s('.header-search-input').submit()

    s(by.link_text('tema1255/qa_guru_hw_4_9')).click()

    s('#issues-tab').click()

    s(by.partial_text('#1')).should(be.visible)

