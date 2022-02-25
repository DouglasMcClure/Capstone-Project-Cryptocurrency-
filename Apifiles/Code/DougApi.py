import json
from six.moves import urllib

url = "https://data.messari.io/api/v1/news"
res = urllib.request.urlopen(url).read()
with open('DougOutput.json') as json_file:
    data = json.load(json_file)