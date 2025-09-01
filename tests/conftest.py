# conftest.py
import pytest
import time
from pathlib import Path

"""  Кусок кода на случай если захочу не параметром, а в коде задавать настройки """
# from playwright.sync_api import sync_playwright
# @pytest.fixture(scope="session")
# def playwright():
#     with sync_playwright() as p:
#         yield p
#
# @pytest.fixture(scope="session")
# def browser(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     yield browser
#     browser.close()
#
# @pytest.fixture(scope="function")
# def page(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук: сохраняет результат выполнения теста (setup/call/teardown)."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture(autouse=True)
def screenshot_after_each_test(request, page):
    """После каждого теста делает скриншот.
       Если тест упал → имя файла оканчивается на _failed.
    """
    yield

    # Базовая папка для скринов
    screenshots_dir = Path("tests/screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    # """Вариант когда нам важно видеть что структура сломана"""
    # if not screenshots_dir.exists():
    #     raise RuntimeError("❌ Папка tests/screenshots не найдена!")

    # Имя теста и таймштамп
    test_name = request.node.name
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    # Проверяем все стадии (setup/call/teardown)
    failed = (
        getattr(request.node, "rep_call", None)
        or getattr(request.node, "rep_setup", None)
        or getattr(request.node, "rep_teardown", None)
    )

    # Проверяем результат
    # failed = getattr(request.node, "rep_call", None)
    suffix = "_failed" if failed and failed.failed else ""

    # Итоговый путь
    screen_path = screenshots_dir / f"{test_name}_{timestamp}{suffix}.png"

    # Сохраняем скрин
    page.screenshot(path=screen_path)
    print(f"\n📸 Скриншот сохранён: {screen_path}")
