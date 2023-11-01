import asyncio
from pyppeteer import launch
from LinksLast4Years import links
from bs4 import BeautifulSoup

async def main(website):
        browser = await launch()
        page = await browser.newPage()
        await page.goto(website)
        await asyncio.sleep(3)
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        await browser.close()
        return html

# for website in links:
#     result = asyncio.get_event_loop().run_until_complete(main('https://www.espncricinfo.com'+website))
#     open(website.split('/')[2]+'.html','w').write(result)
# print(result)

a=[]
for website in links:
    with open('./ListHtml/'+website.split('/')[2]+'.html','r') as file:
        soup=BeautifulSoup(file,features="html.parser")
        div = soup.findAll('div',class_='ds-p-4 ds-border-y ds-border-line')
        for i in div:
            a.append(i.find('a')['href'])
# print(a)

ScoreCardLink=[]

for i in a:
    if i.find('india')!=-1:
        ScoreCardLink.append(i)

print(ScoreCardLink,len(ScoreCardLink))
with open('ScoreCardLinks.txt','w') as f:
    for i in ScoreCardLink:
        f.write(i+'\n')
# for website in ScoreCardLink:
#     try:
#         result = asyncio.get_event_loop().run_until_complete(main('https://www.espncricinfo.com'+website))
#         open(website.split('/')[-2]+'.html','w').write(result)
#     except:
#         print(website)
#         open('sri-lanka-vs-india-1st-odi-1262755.html','w', encoding='utf-8').write(result)
#         
# print(result)
