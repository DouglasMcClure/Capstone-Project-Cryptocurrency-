import json

from six.moves import urllib

url = "https://data.messari.io/api/v1/news"
res = urllib.request.urlopen(url).read()
data = json.loads(res)
data = json.dumps(data)
f = open("DougOutput.json", "w")
f.write(data)
f.close()

# open and read the file after the appending:
f = open("DougOutput.json", "r")
print(f.read())
