# Ввод, клики, ховеры, чекбоксы
page.fill("#username", "alice")
page.fill("#password", "secret")
page.click("text=Log in")
page.hover(".menu")
page.check("#agree")          # или uncheck()

# Выпадающие списки
page.select_option("#country", value="LV")

# Клавиатура и мышь
page.keyboard.type("Hello")
page.keyboard.press("Control+A")
page.mouse.wheel(0, 1000)

# Работа с несколькими вкладками/попапами
with page.expect_popup() as popup_info:
    page.click("a[target=_blank]")
new_page = popup_info.value
