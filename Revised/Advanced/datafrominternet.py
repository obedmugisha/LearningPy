from urllib import request

r = request.urlopen('https://www.linkedin.com/feed/')
print(r.getcode()) # if we get 200 mean everthing is okay we can access the data


print(r.read()) #reading each and every code js , html from the specified website
