from pages.dropdown_page import DropdownPage


def test_select_option_1(driver):
    page = DropdownPage(driver)
    page.open_dropdown()
    page.select_option_by_text("Option 1")
    assert page.get_selected_option_text() == "Option 1"


def test_select_option_2(driver):
    page = DropdownPage(driver)
    page.open_dropdown()
    page.select_option_by_text("Option 2")
    assert page.get_selected_option_text() == "Option 2"