# run.py
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        # 1. Запускаем браузер (на Windows можно channel="msedge" для Edge)
        browser = p.chromium.launch(headless=False)  # или channel="msedge"
        context = browser.new_context()              # изолированный профиль
        page = context.new_page()                    # вкладка

        # 2. Навигация
        page.goto("https://example.com", wait_until="domcontentloaded")
        print("Title:", page.title())

        # 3. Поиск и действия
        link = page.get_by_role("link", name="More information...")
        link.click()

        # 4. Ожидание навигации/состояний
        page.wait_for_url("**/iana.org/**")          # маска

        # 5. Скриншот
        page.screenshot(path="page.png")

        # 6. Закрытие
        context.close()
        browser.close()

if __name__ == "__main__":
    main()
