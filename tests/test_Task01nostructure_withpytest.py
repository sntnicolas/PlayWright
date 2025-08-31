def test_open_example_com(page):
    # 1. Открыть сайт
    page.goto("https://example.com")

    # 2. Проверить заголовок <h1>
    h = page.get_by_role("heading", name="Example Domain")
    assert h.text_content() == "Example Domain"

    # 3. Скриншот
    page.screenshot(path="../screenshot.png")

    # 4. Вывод заголовка страницы
    print("title is \"" + page.title() + "\"")
