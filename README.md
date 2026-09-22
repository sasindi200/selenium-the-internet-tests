# Selenium WebDriver Test Suite — the-internet.herokuapp.com

An automated UI test suite built with **Selenium WebDriver + pytest**, targeting [the-internet](https://the-internet.herokuapp.com) — a demo application purpose-built for practicing browser automation against tricky, real-world UI patterns (dynamic content, iframes, native alerts, multi-window handling, and more).

Rather than testing a single simple flow, this suite covers a range of distinct WebDriver capabilities — explicit waits, frame switching, native alert handling, multi-window management, and more — to demonstrate practical, hands-on Selenium experience beyond basic form automation.

## Tech Stack

- **Python 3.11+**
- **Selenium WebDriver** — browser automation
- **pytest** — test runner and fixtures
- **pytest-html** — HTML test reporting
- **webdriver-manager** — automatic chromedriver version management


## Setup

```bash
# Clone the repo
git clone https://github.com/sasindi200/selenium-the-internet-tests.git
cd selenium-the-internet-tests

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

Chrome must be installed locally — `webdriver-manager` handles downloading the matching chromedriver automatically, so no manual driver setup is needed.

## Running the Tests

Run the full suite:
```bash
pytest tests/ -v
```

Run a single file:
```bash
pytest tests/test_login.py -v
```

Generate an HTML report:
```bash
pytest tests/ --html=report.html --self-contained-html
```
Open `report.html` in a browser to view results. Failed tests automatically save a screenshot to `screenshots/` via a custom pytest hook in `conftest.py`.

## Test Coverage

| Page | Scenario | WebDriver Skill Demonstrated |
|---|---|---|
| Login | Valid login, invalid login, parametrized invalid credential sets | Form interaction, assertions, data-driven testing |
| Checkboxes | Default state check, toggle state | Element state (`is_selected()`) |
| Dropdown | Select by visible text | The `Select` class |
| Dynamic Loading | Both examples (hidden vs. rendered elements) | Explicit waits (`WebDriverWait` + `expected_conditions`) |
| JavaScript Alerts | Accept alert, dismiss confirm | Native alert handling (`switch_to.alert`) |
| Multiple Windows | Open new window, switch context, verify title | Window handle management |
| iFrame | Clear and type into a rich-text editor | Frame switching, JavaScript executor fallback for unreliable native interactions |
| File Upload | Upload a dynamically created file | `send_keys()` on file inputs |
| Drag and Drop | Swap two columns | `ActionChains` |
| Hovers | Reveal and read hidden caption content | Mouse-over actions |
| Add/Remove Elements | Add and delete dynamically created elements | Handling elements not present at page load |

**19 tests, all passing.**

## Notable Debugging Notes

A few real issues hit and resolved during development — kept here because they're more useful than a clean "everything worked" story:

- **Login redirect timing:** asserting on `current_url` immediately after clicking submit was flaky, since the redirect hadn't completed yet. Fixed with an explicit `EC.url_contains()` wait rather than a hard sleep.
- **Hover caption assumption:** initial test assumed the caption text included "View profile," but that text lives in a separate `<a>` tag from the name `<h5>`. Fixed by asserting against the actual DOM structure instead of an assumed one.
- **iFrame + contenteditable:** the rich-text editor inside the iframe is a `contenteditable` div, not a real `<input>`, so `.clear()` and native click-then-type were unreliable (`InvalidElementStateException` and `ElementClickInterceptedException` from TinyMCE's floating toolbar overlapping the iframe). Resolved by using Selenium's JavaScript executor (`driver.execute_script()`) to set content directly — a legitimate fallback when native interaction with a third-party widget is unreliable.

