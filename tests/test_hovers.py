from pages.hovers_page import HoversPage


def test_hover_reveals_caption(driver):
    page = HoversPage(driver)
    page.open_hovers()
    figure = page.hover_over(0)
    assert "name: user1" in page.get_caption_text(figure)
    assert "View profile" in page.get_profile_link_text(figure)