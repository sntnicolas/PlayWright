def test_open_wikipedia_and_click_russian (page):
    page.goto("https://wikipedia.org", timeout=5000)

    """Находим элемент по роли"""
    heading = page.get_by_role("heading", name= "Wikipedia")
    assert heading.is_visible()

    """Раскрываем список и переходим"""
    page.get_by_role("button", name="Read Wikipedia in your").click()
    page.get_by_role("link", name="Nederlands").click()

    """Проверяем что перешли в нидерландскую страницу"""
    assert "Hoofdpagina" in page.url

    searchbox = page.get_by_role("searchbox", name="Doorzoek Wikipedia")
    assert searchbox.is_visible()

    print("title is \"" + page.title() + "\"")