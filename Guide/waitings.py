# 4) Ожидания: автождём правильно
# Playwright сам ждёт, чтобы элемент стал «кликабельным», но:
# навигацию/сетевые события — оборачиваем в контексты ожидания;
# появление/исчезновение — через locator.wait_for.

# Навигация после клика
with page.expect_navigation():
    page.get_by_role("link", name="Profile").click()

# Ожидание запроса/ответа
with page.expect_response(lambda r: r.url.endswith("/api/login") and r.ok):
    page.get_by_role("button", name="Sign in").click()

# Явное ожидание видимости
form = page.locator("#checkout-form")
form.wait_for(state="visible")

# Избегай time.sleep() — почти всегда есть автождание или wait_for_*.