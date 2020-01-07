#Frank Tancredi 7/19/2017

import bs4 as bs
import urllib

for a in range(0, 27): #end of URL increments since there are 27 pages
    if a <= 25:
        source = urllib.urlopen('https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=browseByLetter.page&productLetter=' + chr(ord('A') + a)).read()
    else:
        source = urllib.urlopen('https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=browseByLetter.page&productLetter=0-9').read()
        
    soup = bs.BeautifulSoup(source,'lxml')

    drug = [] 
    drugblocks = soup.find_all('div', {"class":"col-md-12"})
    length = len(drugblocks)
    
     #Range begins at 6 and ends 2 before length because the elements
     #those represent contain useless text encapsulated in the same path 
     #as all drug names. Quick fix.
    for c in range(6,length-2):
        drug.append(drugblocks[c].a.text)
        fdaList = open("FDAApprovedDrugs.txt", 'a')
        fdaList.write(drug[c-6])
        


    

