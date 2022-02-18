from six.moves import urllib

url = "https://data.messari.io/api/v1/news"
res = urllib.request.urlopen(url).read()
print(res)
file_path = ""
f = open(file_path, "w")
f.write(res)
f.close()

# open and read the file after the appending:
f = open(file_path, "r")
print(f.read())
