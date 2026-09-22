from pages.checkboxes_page import CheckboxesPage


def test_checkbox_default_states(driver):
    page = CheckboxesPage(driver)
    page.open_checkboxes()
    assert page.is_checked(0) is False
    assert page.is_checked(1) is True


def test_toggle_checkbox(driver):
    page = CheckboxesPage(driver)
    page.open_checkboxes()
    initial_state = page.is_checked(0)
    page.toggle_checkbox(0)
    assert page.is_checked(0) != initial_state