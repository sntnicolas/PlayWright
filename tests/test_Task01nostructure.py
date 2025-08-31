from playwright.sync_api import sync_playwright

def test_open_example_com():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://example.com")
        h = page.get_by_role("heading", name="Example Domain")
        assert h.text_content() != "Example Domain"

        page.screenshot(path="../screenshot.png")

        print(page.title())

if __name__ == "__main__":
    test_open_example_com()