import asyncio
from pyppeteer import launch

async def main(website):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(website)
    await asyncio.sleep(3)
    html = await page.content()
    await browser.close()
    return html

with open('ODI 7-09\T20 Scraping\T20ScoreCardList.txt', 'r', encoding='utf-8', errors='ignore') as f:
      links = f.readlines()
      for i in range(len(links)):
            links[i] = links[i].strip('\n') 

for website in links:
    result = asyncio.get_event_loop().run_until_complete(main('https://www.espncricinfo.com'+website))
    print(website)
    open(website.split('/')[-2]+'.html','w', encoding='utf-8', errors='ignore').write(result)

print(result)
