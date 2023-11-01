# from bs4 import BeautifulSoup

# file=open('Odis.html')
# soup=BeautifulSoup(file,features="html.parser")
# table = soup.findAll('table',class_='ds-w-full ds-table ds-table-xs ds-table-auto ds-w-full ds-overflow-scroll ds-scrollbar-hide')
# l = []
# for t in table:
#     links = t.findAll('a',class_='ds-inline-flex ds-items-start ds-leading-none')
#     for link in links:
#             l.append(link['href'])
# links = [l[i] for i in range(len(l)) if i >= 218]
#  print(links)