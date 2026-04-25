from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to "https://playwright.dev/"
    page.goto("https://playwright.dev/")
    # Click on Docs textlink
    doc_link = page.get_by_role("link", name="Docs")
    doc_link.click()
    # Get URL and verify
    print("Docs: ", page.url)
    page.close()
