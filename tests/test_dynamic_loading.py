from pages.dynamic_loading_page import DynamicLoadingPage


def test_dynamic_loading_example_1(driver):
    page = DynamicLoadingPage(driver)
    page.open_example(1)
    page.start()
    assert page.get_finish_text() == "Hello World!"


def test_dynamic_loading_example_2(driver):
    page = DynamicLoadingPage(driver)
    page.open_example(2)
    page.start()
    assert page.get_finish_text() == "Hello World!"