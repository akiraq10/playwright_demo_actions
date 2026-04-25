import asyncio
from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://www.saucedemo.com/")
    user_name = page.get_by_role("textbox", name="Username")
    password = page.get_by_role("textbox", name="Password")
    login_btn = page.get_by_role("button", name="Login")
    await user_name.highlight()
    await user_name.fill("standard_user")

    await password.highlight()
    await password.fill("secret_sauce")

    await login_btn.click()

    await page.wait_for_timeout(5000)
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
