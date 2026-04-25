import asyncio
from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/checkbox")
    # Example Click
    folder_checkbox = page.get_by_role("checkbox", name="Select Home")
    await folder_checkbox.highlight()
    await folder_checkbox.check()
    await folder_checkbox.click()
    await folder_checkbox.check()
    await folder_checkbox.uncheck()

    await page.wait_for_timeout(2000)
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
