import asyncio
from playwright.async_api import async_playwright, expect, Playwright, Page
import demo1 as dm1


async def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()

    # Case: Not a Select Element
    await page.goto("https://maru.asia:444/")

    user_name = page.locator("#UserName")
    password = page.locator("#password-input")
    login_btn = page.locator("#ses-submit-btn")
    system_menu = page.locator(".i_Systems")
    notification_opt = page.get_by_title("Notification", exact=True)
    config_menu = page.get_by_role("link", name="Configuration ▾")
    config_opt = page.locator("#Actions_Notification_Configuration")
    notifcation_level_dropdown = page.locator(
        "//span[@aria-controls='SeverityLevel_listbox']"
    )

    save_btn = page.get_by_text("Save")
    yes_btn = page.get_by_text("Yes")
    no_btn = page.get_by_text("No", exact=True)
    confirmation_msg = page.locator(".jconfirm-content")

    await dm1.highlight_and_fill(user_name, "admin")
    await dm1.highlight_and_fill(password, "1")

    await dm1.highlight_and_click(login_btn)

    await dm1.highlight_and_click(system_menu)
    await dm1.highlight_and_click(notification_opt)
    await dm1.highlight_and_click(config_menu)
    await dm1.highlight_and_click(config_opt)
    await dm1.highlight_and_click(notifcation_level_dropdown)
    await select_notification_option(page, "No notification")
    await dm1.highlight_and_click(save_btn)

    await isCheckNotification(
        confirmation_msg, "Would you like to save the notification configuration?"
    )

    await dm1.highlight_and_click(no_btn)

    await page.wait_for_timeout(2000)
    await page.close()


async def select_notification_option(page: Page, option: str):
    notification_option = page.get_by_text(option, exact=True)
    await dm1.highlight_and_click(notification_option)


async def isCheckNotification(locator, msg: str):
    await expect(locator.get_by_text(msg)).to_be_visible()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
