def test_search_in_wikipedia(page):
    page.goto("https://en.wikipedia.org/", timeout=5000)
    search = page.get_by_role("searchbox", name="Search Wikipedia")
    search.click()
    # В этот момент почему-то серчбокс становится комбобоксом
    search.fill("Playwright")
    page.get_by_role("button", name="Search").click()
    assert "Playwright" in page.url
    print("title is \"" + page.title() + "\"")