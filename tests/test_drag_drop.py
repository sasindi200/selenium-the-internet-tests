from pages.drag_drop_page import DragDropPage


def test_drag_and_drop_swaps_columns(driver):
    page = DragDropPage(driver)
    page.open_drag_drop()
    initial_a = page.get_column_a_text()
    page.drag_a_to_b()
    assert page.get_column_b_text() == initial_a