# playwright-frontend-tester

An [OpenCode](https://opencode.ai/) skill for using [Playwright](https://playwright.dev/python/) to test web applications and fix frontend bugs directly in a real browser.

## What it does

- Automates local and remote web apps with Playwright.
- Inspects rendered DOM, captures screenshots, and asserts element visibility.
- Provides a reusable pattern for login flows and end-to-end smoke tests.
- Helps reproduce and verify frontend bug fixes.

## Files

| File | Description |
|------|-------------|
| `SKILL.md` | OpenCode skill instructions and decision tree. |
| `examples/test_example.py` | Example script: log in and verify the dashboard. |
| `README.md` | This file. |

## Setup

Install Playwright and the Chromium browser:

```bash
uv run --with playwright python -m playwright install chromium
```

## Usage

Run the example against a local dev server:

```bash
uv run --with playwright python examples/test_example.py
```

Run a one-off smoke test against any URL:

```bash
uv run --with playwright python -c "
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://example.com')
    page.wait_for_load_state('networkidle')
    page.screenshot(path='/tmp/smoke.png')
    browser.close()
"
```

## License

MIT
