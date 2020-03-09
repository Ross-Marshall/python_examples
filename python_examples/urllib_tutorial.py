from urllib import request

from urllib import parse

resp = request.urlopen("https://news.google.com")

print(type(resp))

print(dir(resp))

print(resp.length)

print(resp.code)

print(resp.peek())


data = resp.read()

print(len(data))

url = "https://www.youtube.com/watch?v=c09m5f7Gnic"

params = {"v" : "c09m5f7Gnic"}

querystring = parse.urlencode(params)
print(querystring)

url2 = "https://meaningoflife.tv/videos/42568?in=30:57&out="
params = {"in": "30:56", "out": ""}
querystring = parse.urlencode(params)
print(querystring)