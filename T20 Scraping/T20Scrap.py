from bs4 import BeautifulSoup
import pandas as pd
with open('ODI 7-09\T20 Scraping\T20ScoreCardList.txt','r',encoding='utf-8', errors='ignore') as f:
    links = f.readlines()

for i in range(len(links)):
    links[i] = links[i].strip('\n')


mainDfBat = pd.DataFrame()
mainDfBowl = pd.DataFrame()


for link in links:
    file = open('ODI 7-09\T20 Scraping\T20ScoreCard\\'+link.split('/')[-2]+'.html','r',encoding='utf-8', errors='ignore')
    soup=BeautifulSoup(file,features="lxml")
    BatsmenName = []
    Runs = []
    matchName=[]
    Balls,Fours,Sixes,SR = [],[],[],[]
    Out_NotOut = []
    matchId = []
    temp=[]
    Wickets = []
    BowlerName = []
    Bowler_MatchName=[]
    Bowler_MatchId=[]
    Overs,Maiden,BowlRuns,ECON,Wide,NB=[],[],[],[],[],[]
    Zeroes,BowlFours,BowlSixes = [],[],[]
    divs = soup.findAll('div',class_='ds-rounded-lg ds-mt-2')
    link_name = link.strip('\n')
    temp_name = link_name.split('/')[-2].split('-')[:-3]
    table = soup.findAll('table',class_='ds-w-full ds-table ds-table-sm ds-table-auto')
    
    for i in table:
        td = i.findAll('td',class_='ds-min-w-max ds-text-typo')
        for j in td:
            a = j.findAll('a',class_='ds-inline-flex ds-items-start ds-leading-none')
            for k in a:
                temp.append(k.text.strip())
    
    for i in range(len(temp)):
        if temp[i].startswith('T20') and temp[i][8]!='0':
            tempid=temp[i]
    for div in divs:
        span = div.find('span',class_='ds-text-title-xs ds-font-bold ds-capitalize')
        if span.text == 'India':
            table = div.findAll('table',class_='ds-p-0 ds-table')
            # print(table)
            for i in table:
                td = i.findAll('span',class_='ds-text-tight-s ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block')
                for j in td:
                    # print(j.text.strip())
                    BatsmenName.append(j.text.strip())
                    matchName.append(' '.join(temp_name))
                    matchId.append(tempid)
                run = i.findAll('td',class_='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-right ds-text-typo')
                for j in run:
                    Runs.append(j.text.strip())
                BFSS=[]
                BFSS = i.findAll('td',class_='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-right')
                for j in range(len(BFSS)):
                    if j%4==0:
                        Balls.append(BFSS[j].text.strip())
                    elif j%4==1:
                        Fours.append(BFSS[j].text.strip())
                    elif j%4==2:
                        Sixes.append(BFSS[j].text.strip())
                    elif j%4==3:
                        SR.append(BFSS[j].text.strip())
                out_notout = i.findAll('td',class_='ds-min-w-max ds-hidden')[:-1]
                for i in out_notout:
                    if i.text.strip() == 'not out':
                        Out_NotOut.append('Not Out')
                    else:
                        Out_NotOut.append('Out')
            df = pd.DataFrame(list(zip(matchName,matchId,BatsmenName,Out_NotOut,Runs,Balls,Fours,Sixes,SR)),columns=['Match','Match_id','Name','Out/NotOut','Runs','Balls','4s','6s','SR'])
            mainDfBat = pd.concat([mainDfBat,df])
        else:
            table = div.findAll('table',class_='ds-w-full ds-table ds-table-xs ds-table-auto')
            for i in table:
                td = i.findAll('td',class_='ds-flex ds-items-center')
                for j in td:
                    BowlerName.append(j.text.strip())
                    Bowler_MatchName.append(' '.join(temp_name))
                    Bowler_MatchId.append(tempid)

                OMREWN = i.findAll('td',class_='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-right')
                for j in range(len(OMREWN)):
                    if j%6==0:
                        Overs.append(OMREWN[j].text.strip())
                    elif j%6==1:
                        Maiden.append(OMREWN[j].text.strip())
                    elif j%6==2:
                        BowlRuns.append(OMREWN[j].text.strip())
                    elif j%6==3:
                        ECON.append(OMREWN[j].text.strip())
                    elif j%6==4:
                        Wide.append(OMREWN[j].text.strip())
                    elif j%6==5:
                        NB.append(OMREWN[j].text.strip())
                wickets = i.findAll('td',class_='ds-w-0 ds-whitespace-nowrap ds-text-right')
                for j in wickets:
                    Wickets.append(j.text.strip())
                ZFS = i.findAll('td',class_='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-right ds-hidden')
                for j in range(len(ZFS)):
                    if j%3==0:
                        Zeroes.append(ZFS[j].text.strip())
                    elif j%3==1:
                        BowlFours.append(ZFS[j].text.strip())
                    elif j%3==2:
                        BowlSixes.append(ZFS[j].text.strip())
            df = pd.DataFrame(list(zip(Bowler_MatchName,Bowler_MatchId,BowlerName,Overs,Maiden,BowlRuns,Wickets,ECON,Zeroes,BowlFours,BowlSixes,Wide,NB)),columns=['Match','Match_id','Name','Overs','Maiden','Runs','Wickets','ECON','0s','4s','6s','Wide','NB'])
            mainDfBowl = pd.concat([mainDfBowl,df])    

mainDfBat.to_csv('T20BattingSummaryINDIA.csv')
mainDfBowl.to_csv('T20BowlingSummaryINDIA.csv')