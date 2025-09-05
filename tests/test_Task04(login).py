def test_login_parabank(page):
    page.goto("https://automationexercise.com/", timeout=5000)
    page.get_by_role("link", name=" Signup / Login").click()

    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("sntnicolas@gmail.com")
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_role("button", name="Log In").click()

    # Проверяем, что на странице есть подтверждение входа
    logged = page.get_by_text("Logged in as nicolas")
    assert logged.is_visible()

    print("✅ Логин успешный, юзер в системе")
