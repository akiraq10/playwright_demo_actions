import asyncio
from playwright.async_api import async_playwright


async def run():
    async with async_playwright() as playwright_instance:
        browser = await playwright_instance.chromium.launch(headless=False)
        page = await browser.new_page()

        url = "https://s3.amazonaws.com/BuildTeam/1.6.0/MagicEndpoint_Enterprise_x64_1.6.0.287.exe"

        # Initialize the download listener
        async with page.expect_download() as download_info:
            try:
                # This will trigger the 'Download is starting' error
                await page.goto(url)
            except Exception as e:
                # Check if it's the expected download error
                if "Download is starting" not in str(e):
                    raise e

        # Capture the finished download object
        download_handler = await download_info.value
        save_path = "./download_folder/" + download_handler.suggested_filename
        await download_handler.save_as(save_path)
        print(f"File saved successfully: {save_path}")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(run())
