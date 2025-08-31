# ЛОКАТОРЫ
#
# Приоритет (от самого устойчивого к более «ломкому»):
# 1) get_by_role / get_by_label / get_by_placeholder / get_by_text
# 2) locator("[data-testid=...]") (в бою часто добавляют data-testid)
# 3) CSS-селекторы
# 4) XPath (крайний вариант)

page.get_by_role("button", name="Log in").click()
page.get_by_label("Email").fill("user@example.com")
page.get_by_placeholder("Search").press("Enter")
page.locator("[data-testid=submit]").click()
