import play_scraper
from csv import writer

with open('spotify.csv', 'w', encoding = "utf-8") as csv_file:
  csv_writer = writer(csv_file)
  headers = ["Details", "Similar", "Search", "Trending"]
  csv_writer.writerow(headers)

  details = play_scraper.details('com.spotify.music',hl='en', gl='in')
  similar = play_scraper.developer('Spotify Ltd.', results=5, hl='en', gl='in')
  search = play_scraper.search('com.spotify.music',detailed=True, hl='en', gl='in')
  collection = play_scraper.collection(collection='TRENDING',category='MUSIC_AND_AUDIO',results=10,hl='en',gl = 'in',page=1)
  csv_writer.writerow([details, similar, search, collection])

#print(play_scraper.details('com.spotify.music'))

#print(play_scraper.collection(collection='TRENDING',category='MUSIC_AND_AUDIO',results=10,hl='en',gl = 'in',page=1))
#print(play_scraper.search('com.spotify.music',detailed=True, hl='en', gl='in'))

#print(play_scraper.developer('Spotify Ltd.', results=5))