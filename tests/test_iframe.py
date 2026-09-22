from pages.iframe_page import IframePage


def test_type_in_iframe_editor(driver):
    page = IframePage(driver)
    page.open_iframe()
    page.clear_and_type("Hello from Selenium")
    assert page.get_editor_text() == "Hello from Selenium"