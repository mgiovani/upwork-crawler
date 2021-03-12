import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()
    await page.goto('https://google.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.run(main())
