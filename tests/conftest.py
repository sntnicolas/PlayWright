import pytest
from pathlib import Path

@pytest.fixture(autouse=True)
def screenshot_dir(page,request):
    """Автоматически делает скриншот если тест упал"""
    yield
    if request.node.rep_call.failed: # если тест упал
        path = Path(__file__).parent / "screenshots" / f"{request.node.name}.png"


import pytest
from pathlib import Path

# Хук, который цепляет результат выполнения теста
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def screenshot_on_fail(page, request):
    """Делает скриншот, если тест упал"""
    yield  # здесь запускается сам тест

    # Проверка: тест упал именно в фазе выполнения (call)
    if request.node.rep_call.failed:
        screenshots_dir = Path(__file__).parent / "screenshots"
        screenshots_dir.mkdir(exist_ok=True)

        file_path = screenshots_dir / f"{request.node.name}.png"
        page.screenshot(path=file_path)

        print(f"\n📸 Скриншот сохранён: {file_path}")
