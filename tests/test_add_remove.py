from pages.add_remove_page import AddRemovePage


def test_add_and_remove_elements(driver):
    page = AddRemovePage(driver)
    page.open_add_remove()
    assert page.get_delete_button_count() == 0

    page.add_element()
    page.add_element()
    assert page.get_delete_button_count() == 2

    page.delete_first_element()
    assert page.get_delete_button_count() == 1