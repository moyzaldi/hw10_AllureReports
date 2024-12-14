from selene import browser, by, have



def test_github():

    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()
    browser.element("[data-testid='results-list']").element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()
    browser.element("[class='js-navigation-container js-active-navigation-container']").should(have.text("#95"))

