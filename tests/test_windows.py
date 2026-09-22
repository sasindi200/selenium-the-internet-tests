from pages.windows_page import WindowsPage


def test_new_window_opens_with_correct_title(driver):
    page = WindowsPage(driver)
    page.open_windows()
    page.click_new_window()
    page.switch_to_new_window()
    assert page.get_new_window_title() == "New Window"