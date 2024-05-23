import time
x = time.time()
print(time.ctime(x))# ctime current timing since epoch in 1st january 1970
#when we are working with time and date we need to import time in our codes so we are now having access tothe time.
print(time.gmtime(x)) #gmt time printing in python
help(time.gmtime)