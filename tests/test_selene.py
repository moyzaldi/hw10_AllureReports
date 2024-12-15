from git_search.issue_search import IssueSearch


def test_issue_search_in_github():
    issue_search = IssueSearch()
    issue_search.input_search("eroshenkoam/allure-example")
    issue_search.assert_issue("eroshenkoam/allure-example", "#95")
