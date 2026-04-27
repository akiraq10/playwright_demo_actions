import asyncio
from playwright.async_api import async_playwright, expect, Playwright, Page
import demo1 as dm1


async def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()

    # Case: Not a Select Element
    await page.goto("https://maru.asia:444/")

    installation_menu = page.locator(".i_Packages")
    sd_installation_menu = page.locator("#Actions_Type_Package_SD_Installers")
    sd_x64_option_menu = page.get_by_text("SecureDoc x64", exact=True)

    await dm1.login_fea(page, "admin", "1")

    await dm1.highlight_and_click(installation_menu)
    await dm1.highlight_and_click(sd_installation_menu)

    async with page.expect_download() as download_info:
        await dm1.highlight_and_click(sd_x64_option_menu)
    download = await download_info.value

    await download.save_as("./download_folder/" + download.suggested_filename)
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
