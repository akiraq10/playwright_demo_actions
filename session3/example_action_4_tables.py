import asyncio
from playwright.async_api import async_playwright, expect, Playwright


async def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/webtables")
    # Get and Verify all headers of Tables

    table_header = page.locator("//table/thead/tr/th")

    for i in range(await table_header.count()):
        await table_header.nth(i).highlight()

    table_header_size = await table_header.count()

    await expect(table_header).to_have_count(table_header_size)
    await expect(table_header.get_by_text("Salary")).to_be_visible()

    await page.wait_for_timeout(2000)
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
