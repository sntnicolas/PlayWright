# Новый контекст с шириной/высотой и юзер-агентом
context = browser.new_context(
    viewport={"width": 1280, "height": 800},
    user_agent="MyBot/1.0"
)

# Эмуляция устройства (пример)
from playwright.sync_api import devices
iphone_13 = devices["iPhone 13"]
mobile = browser.new_context(**iphone_13)

# Авторизация один раз → сохраняем стейт
context = browser.new_context()
page = context.new_page()
# ... логин ...
context.storage_state(path="state.json")

# Повторное использование с готовыми куки/локалсторадж
reused = browser.new_context(storage_state="state.json")
