from selene import browser, by, have

class IssueSearch:

    def input_search(self, repo):
        browser.element("[data-target='qbsearch-input.inputButtonText']").click()
        browser.element("#query-builder-test").send_keys(repo).press_enter()

    def assert_issue(self, repo,issue):
        browser.element("[data-testid='results-list']").element(by.link_text(repo)).click()
        browser.element("#issues-tab").click()
        browser.element("[class='js-navigation-container js-active-navigation-container']").should(have.text(issue))





