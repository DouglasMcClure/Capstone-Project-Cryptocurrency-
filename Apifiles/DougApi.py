from six.moves import urllib
url = "https://data.messari.io/api/v1/news"
print(urllib.request.urlopen(url).read())