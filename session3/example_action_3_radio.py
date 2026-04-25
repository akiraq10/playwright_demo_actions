import asyncio
from playwright.async_api import async_playwright, expect, Playwright


async def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/radio-button")
    # Example Click
    yes_radio = page.locator("//label[@for='yesRadio']")
    impressive_radio = page.locator("//label[@for='impressiveRadio']")
    no_radio = page.locator("//label[@for='noRadio']")
    await yes_radio.highlight()
    await yes_radio.check()
    # await yes_radio.click()
    assert await yes_radio.is_checked()
    assert not await impressive_radio.is_checked()
    assert not await no_radio.is_checked()

    await expect(page.locator("//label[@for='noRadio']")).not_to_be_checked()

    await page.wait_for_timeout(2000)
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
