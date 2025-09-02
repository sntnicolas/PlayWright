
print("TEST START")

def test_open_example_com(page):
    page.goto("https://example.com", timeout=5000)
    h = page.get_by_role("heading", name="Example Domain")
    assert h.text_content() == "Example Domain"
    print("title is \"" + page.title() + "\"")