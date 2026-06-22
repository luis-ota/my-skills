"""
Example Playwright test: log in to a web app and verify the dashboard loads.

This script assumes a local dev server is running on http://localhost:5173
with a /login page and a /dashboard page.

Run with:
    uv run --with playwright python examples/test_example.py
"""

from playwright.sync_api import sync_playwright, expect


def test_login_and_dashboard():
    with sync_playwright() as p:
        # Launch headless Chromium. Use headless=False to watch the browser.
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        try:
            base_url = "http://localhost:5173"

            # 1. Navigate to the login page and wait for it to settle.
            page.goto(f"{base_url}/login")
            page.wait_for_load_state("networkidle")
            page.screenshot(path="/tmp/01_login_page.png")

            # 2. Fill in the login form.
            page.locator('input[name="username"]').fill("admin")
            page.locator('input[name="password"]').fill("secret")

            # 3. Submit the form.
            page.locator('button[type="submit"]').click()

            # 4. Wait for navigation to the dashboard.
            page.wait_for_url("**/dashboard")
            page.wait_for_load_state("networkidle")
            page.screenshot(path="/tmp/02_dashboard.png", full_page=True)

            # 5. Assert the dashboard is visible.
            expect(page.locator("h1")).to_be_visible()
            dashboard_heading = page.locator("h1").inner_text()
            assert "dashboard" in dashboard_heading.lower(), (
                f"Expected dashboard heading, got: {dashboard_heading}"
            )

            # 6. Inspect a list of navigation links for debugging.
            links = page.locator("nav a").all()
            print("Navigation links:")
            for link in links:
                print(f"  - {link.inner_text().strip()}: {link.get_attribute('href')}")

            print("Test passed: login and dashboard are working.")

        finally:
            context.close()
            browser.close()


if __name__ == "__main__":
    test_login_and_dashboard()
