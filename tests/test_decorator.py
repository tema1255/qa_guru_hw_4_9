import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'tema1255')
@allure.feature('Проверка наличия Issue на github')
@allure.story('Шаги с декоратором @allure.step')
@allure.link('https://github.com', name='Testing')
def test_dekorator_steps():
    open_main_page()
    search_for_repository('tema1255/qa_guru_hw_4_9')
    go_to_repository('tema1255/qa_guru_hw_4_9')
    open_issue_tab()
    should_see_issue('#1')

@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')

@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()

@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step('Ищем таб Issues')
def open_issue_tab():
    s('#issues-tab').click()

@allure.step('Проверяем наличие Issue на странице')
def should_see_issue(issue):
    s(by.partial_text(issue)).click()
