import allure
from selene import browser, by, have
from git_search.issue_search import IssueSearch
from allure_commons.types import Severity

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_dynamic_steps_issue_search_in_github():
    issue_search = IssueSearch()

    with allure.step("Ищем репозиторий"):
        issue_search.input_search("eroshenkoam/allure-example")

    with allure.step("Проверяем наличие Issue с номером 95"):
        issue_search.assert_issue("eroshenkoam/allure-example", "#95")



@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps_issue_search_in_github():
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#95")

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys(repo).press_enter()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element("[data-testid='results-list']").element(by.link_text(repo)).click()

@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()

@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element("[class='js-navigation-container js-active-navigation-container']").should(have.text(number))


