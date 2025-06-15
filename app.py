import asyncio
import subprocess
subprocess.run(["playwright", "install", "chromium"])

from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
async def main():
    browser_config = BrowserConfig()
    run_config = CrawlerRunConfig()
    output_text = ""

    async with AsyncWebCrawler(config=browser_config) as crawler:
        for page in range(1, 6):  # Pages 1 to 5
            url = f"https://www.amazon.in/s?k=smartphones&page={page}"
            print(f"Crawling: {url}")
            result = await crawler.arun(url=url, config=run_config)
            output_text += f"\n\n--- Page {page} ---\n\n"
            output_text += result.markdown

    # Save to file
    with open("smartphones_amazon_pages.txt", "w", encoding="utf-8") as f:
        f.write(output_text)
    print("Crawling complete. Output saved to smartphones_amazon_pages.txt")

if __name__ == "__main__":
    asyncio.run(main())
