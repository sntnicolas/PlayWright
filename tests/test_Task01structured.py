def test_open_example_com(page):
    page.goto("https://example.com")
    h = page.get_by_role("heading", name="Example Domain")
    assert h.text_content() == "Example Domain"
    page.screenshot(path="tests/screenshots/test_open_example_com.png")
    print("title is \"" + page.title() + "\"")
