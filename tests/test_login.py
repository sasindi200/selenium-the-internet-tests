import pytest

from pages.login_page import LoginPage


def test_valid_login(driver):
    page = LoginPage(driver)
    page.open_login()
    page.login("tomsmith", "SuperSecretPassword!")
    page.wait_for_secure_url()
    assert "secure" in page.driver.current_url


def test_invalid_login_shows_error(driver):
    page = LoginPage(driver)
    page.open_login()
    page.login("wronguser", "wrongpass")
    error_text = page.get_flash_text()
    assert "invalid" in error_text.lower()


@pytest.mark.parametrize("username,password", [
    ("tomsmith", "wrongpass"),
    ("wronguser", "SuperSecretPassword!"),
    ("", ""),
])
def test_login_invalid_combinations(driver, username, password):
    page = LoginPage(driver)
    page.open_login()
    page.login(username, password)
    error_text = page.get_flash_text()
    assert "invalid" in error_text.lower() or "your username is invalid" in error_text.lower()