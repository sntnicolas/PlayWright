# Загрузка файла (input[type=file])
page.set_input_files('input[type="file"]', "C:/path/to/photo.png")

# Скачивание
with page.expect_download() as dl:
    page.click("text=Download")
download = dl.value
download.save_as("C:/Temp/file.zip")

# Диалоги (alert/confirm/prompt)
page.on("dialog", lambda d: d.accept())  # или d.dismiss()

# iFrame: сначала находим фрейм, потом работаем как со страницей
frame = page.frame_locator("iframe#iframeId")
frame.get_by_text("Click me").click()

# Мок/перехват сети
def fake_products(route):
    route.fulfill(
        status=200,
        content_type="application/json",
        body='[{"id":1,"name":"Mocked"}]'
    )
context.route("**/api/products", fake_products)

# сделать скриншот страницы:
page.screenshot(path="screenshot.png")
