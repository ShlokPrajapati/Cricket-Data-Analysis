from bs4 import BeautifulSoup
import pandas as pd
with open('ODI Scraping\ODI\Scrapper\ScoreCardLinks.txt','r',encoding='utf-8', errors='ignore') as f:
    links = f.readlines()

main_df = pd.DataFrame()

for link in links:
    file = open('ODI Scraping/ODI/ScoreCard/'+link.split('/')[-2]+'.html','r',encoding='utf-8', errors='ignore')
    soup=BeautifulSoup(file,features="lxml")
    BatsmenName,Out_NotOut, matchDate = [], [], []
    matchName = []
    Runs = []
    link_name = link.strip('\n')
    temp_name = link_name.split('/')[-2].split('-')[:-3]
    divs = soup.findAll('div',class_='ds-rounded-lg ds-mt-2')
    for div in divs:
        span = div.find('span',class_='ds-text-title-xs ds-font-bold ds-capitalize')
        if span.text == 'India':
            table = div.findAll('table',class_='ds-w-full ds-table ds-table-xs ds-table-auto ci-scorecard-table')
            for i in table:
                td = i.findAll('span',class_='ds-text-tight-s ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block')
                for j in td:
                    BatsmenName.append(j.text.strip())
                    matchName.append(' '.join(temp_name))
                out_notout = i.findAll('td',class_='ds-min-w-max ds-hidden')[:-1]
                for k in out_notout:
                    if k.text.strip() == 'not out':
                        Out_NotOut.append('Not Out')
                    else:
                        Out_NotOut.append('Out')
                run = i.findAll('td',class_='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-right ds-text-typo')
                for j in run:
                    Runs.append(j.text.strip())
    table = soup.findAll('table',class_='ds-w-full ds-table ds-table-sm ds-table-auto')
    temp_date=[]
    for i in table:
        td = i.findAll('td',class_='ds-min-w-max ds-text-typo')
        for j in td:
            temp_date.append(j.text.strip())
    
    for i in range(len(temp_date)):
        if temp_date[i].endswith('(50-over match)'):
            date = temp_date[i].split('-')[0].strip()

    for i in BatsmenName:
        matchDate.append(date)
    
    df = pd.DataFrame(list(zip(matchName, matchDate, BatsmenName, Runs, Out_NotOut)), columns=['Match', 'Date', 'Batsman', 'Runs', 'Out'])
    main_df = pd.concat([main_df, df])

print(main_df)
