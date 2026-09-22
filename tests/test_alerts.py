from pages.alerts_page import AlertsPage


def test_accept_js_alert(driver):
    page = AlertsPage(driver)
    page.open_alerts()
    page.trigger_alert()
    page.accept_alert()
    assert "successfully clicked an alert" in page.get_result_text()


def test_dismiss_js_confirm(driver):
    page = AlertsPage(driver)
    page.open_alerts()
    page.trigger_confirm()
    page.dismiss_alert()
    assert "cancel" in page.get_result_text().lower()