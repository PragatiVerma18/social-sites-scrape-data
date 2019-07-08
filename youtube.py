from bs4 import BeautifulSoup as bs
import requests
import json

base = "https://www.youtube.com/results?search_query="
qstring = "oneplus+advert"
r = requests.get(base+qstring)

page = r.text
soup=bs(page,'html.parser')
#print(soup.prettify())
vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})


videolist=[]
ownerlist = []
titles = []
info_time = []
info_view = []
yt_details = {}

for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)
#print(videolist)

for title in soup.findAll('h3', attrs={'class': 'yt-lockup-title'}):
    titles.append(title.find('a').get_text().strip())
    
for owner in soup.findAll('div',attrs={'class':"yt-lockup-byline"}):
    tmp = owner.get_text().strip()
    ownerlist.append(tmp)
#print(ownerlist)

for info in soup.findAll('ul',attrs={'class':"yt-lockup-meta-info"}):
  children = info.findChildren("li" , recursive=False)
  for i in range(len(children)):
    if i%2 == 0:
      info_time.append(children[i].get_text())
    else:
      info_view.append(children[i].get_text())
#print(info_time,info_view)

#making a dictionary with all data
#for i in vids:



# writing in a JSON file
#with open('personal.json', 'w') as json_file:  
    #json.dump(yt_details, json_file)
