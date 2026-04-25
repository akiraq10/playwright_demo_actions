import asyncio
from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    # Case: Dropdown - Select element
    await page.goto("https://demoqa.com/webtables")
    await page.locator(".form-control:last-child").highlight()
    await page.locator(".form-control:last-child").select_option("30")

    await page.wait_for_timeout(2000)
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
