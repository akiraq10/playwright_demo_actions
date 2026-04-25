import asyncio
from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()
    # await page.goto("https://bootswatch.com/default/")

    await page.goto("https://www.saucedemo.com/")

    account_text = page.get_by_text("Accepted usernames are:")
    await account_text.highlight()

    await page.wait_for_timeout(5000)
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
