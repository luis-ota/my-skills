---
name: playwright-frontend-tester
description: Use Playwright to fix frontend bugs and test web apps directly. Supports local and remote sites, DOM inspection, screenshots, element assertions, and login flows.
---

# Playwright Frontend Tester

Use this skill whenever you need to test a web application, reproduce a frontend bug, inspect the DOM, capture screenshots, or assert that UI elements behave correctly. It works for both local development servers and remote URLs.

## When to use

- A user reports a frontend bug and you need to reproduce it in a browser.
- You want to verify that a page renders or that an element is visible/clickable.
- You need to test a login flow or form submission end-to-end.
- You want to capture a screenshot before and after a code change.

## Installation

Install Playwright and its browsers (run once per environment):

```bash
uv run --with playwright python -m playwright install chromium
```

## Quick start

Run a minimal smoke test against a URL:

```bash
uv run --with playwright python -c "
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://example.com')
    page.wait_for_load_state('networkidle')
    assert page.locator('h1').is_visible()
    page.screenshot(path='/tmp/smoke.png')
    browser.close()
"
```

## Decision tree

```
User asks for frontend test / bug fix
    |
    +-- Is the target a local dev server?
    |       +-- Yes -> Start the server first, then run Playwright against http://localhost:<port>
    |       +-- No  -> Run Playwright against the provided remote URL
    |
    +-- Inspect the page:
    |       page.wait_for_load_state('networkidle')
    |       page.screenshot(path='/tmp/step1.png')
    |       page.content()  # full DOM
    |
    +-- Reproduce / assert:
    |       page.locator(...).click()
    |       page.locator(...).fill('value')
    |       expect(page.locator(...)).to_be_visible()
```

## Common patterns

### Wait for dynamic content

Always wait for `networkidle` (or a specific selector) before inspecting a dynamic page:

```python
page.goto(url)
page.wait_for_load_state('networkidle')
```

### Discover selectors

```python
# List all buttons
for btn in page.locator('button').all():
    print(btn.inner_text(), btn.get_attribute('id'), btn.get_attribute('class'))

# Query by text, role, or CSS
page.locator('text=Submit')
page.locator('role=button[name="Submit"]')
page.locator('#login-button')
```

### Take screenshots

```python
page.screenshot(path='/tmp/page.png', full_page=True)
element = page.locator('.error-message')
element.screenshot(path='/tmp/error.png')
```

### Assert element visibility

Use Playwright's built-in auto-retrying assertions:

```python
from playwright.sync_api import expect

expect(page.locator('h1')).to_be_visible()
expect(page.locator('.error')).to_have_text('Invalid credentials')
```

### Handle login forms

```python
page.goto('http://localhost:5173/login')
page.wait_for_load_state('networkidle')
page.locator('input[name="username"]').fill('admin')
page.locator('input[name="password"]').fill('secret')
page.locator('button[type="submit"]').click()
page.wait_for_url('**/dashboard')
```

## Best practices

- Prefer `headless=True` for automated tests unless the user explicitly needs a headed browser.
- Use `expect(...)` assertions instead of raw `is_visible()` checks so Playwright retries automatically.
- Take screenshots at each debugging step when fixing a frontend bug.
- Keep selectors stable: prefer `data-testid`, IDs, or ARIA roles over brittle CSS classes.
- Always `browser.close()` (use a context manager or `try/finally`).

## Reference files

- `examples/test_example.py` - Full example: login and verify dashboard visibility.
- `README.md` - Skill overview and setup instructions.
