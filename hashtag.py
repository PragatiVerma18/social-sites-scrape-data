# Read https://buildmedia.readthedocs.org/media/pdf/instalooter/latest/instalooter.pdf
# Read https://github.com/althonos/InstaLooter
#
from instalooter.looters import ProfileLooter
# enter the profile to scrape data
#looter = ProfileLooter("virat.kohli")
#looter.download('~/Pictures', media_count=20)

# to get the link of images and videos linked to a hashatg
"""def links(media, looter):
  if media.get('__typename') == "GraphSidecar":
    media = looter.get_post_info(media['shortcode'])
    nodes = [e['node'] for e in media['edge_sidecar_to_children']['edges']]
    return [n.get('video_url') or n.get('display_url') for n in nodes]
  elif media['is_video']:
    media = looter.get_post_info(media['shortcode'])
    return [media['video_url']]
  else:
    return [media['display_url']]

from instalooter.looters import HashtagLooter
looter = HashtagLooter("harrypotter")
# top write the data obtained in a text file
with open("harrypotter.txt", "w") as f:
  for media in looter.medias():
    for link in links(media, looter):
      f.write("{}\n".format(link)) """

# to get the usernames from comments on a profile
"""from instalooter.looters import ProfileLooter
looter = ProfileLooter("selenagomez")
users = set()
for media in looter.medias():
  info = looter.get_post_info(media['shortcode'])
  for comment in post_info['edge_media_to_comment']['edges']:
    user = comment['node']['owner']['username']
    users.add(user) """