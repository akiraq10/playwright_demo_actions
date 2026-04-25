import asyncio
from playwright.async_api import async_playwright, expect, Playwright


async def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()

    # Case: Not a Select Element
    await page.goto("https://maru.asia:444/")

    user_name = page.locator("#UserName")
    password = page.locator("#password-input")
    login_btn = page.locator("#ses-submit-btn")
    logged_in_status = page.locator("#LoggedInUserName")

    await highlight_and_fill(user_name, "admin")
    await highlight_and_fill(password, "1")

    await highlight_and_click(login_btn)

    assert await logged_in_status.is_visible()
    await expect(logged_in_status).to_have_text("admin")

    await page.wait_for_timeout(2000)
    await page.close()


async def highlight_and_fill(locator, value: str):
    await locator.highlight()
    await locator.fill(value)


async def highlight_and_click(locator):
    await locator.highlight()
    await locator.click()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
