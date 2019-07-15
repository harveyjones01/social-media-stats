#https://twitter.com/Harveyjones01?lang=en-gb
#https://twitter.com/Twitter?lang=en-gb
#https://twitter.com/katyperry?lang=en-gb

#https://twitter.com/ + twitter_handle + ?lang=en-gb
import urllib.request
import urllib.parse
import re




def twitter_stats(twitter_handle):
    x = urllib.request.urlopen('https://twitter.com/' + twitter_handle)
    html = x.read()
    info = re.findall(r'data-count=(.*?) ', str(html))
    return info
    


try:
    twitter_handle = input('twitter name --->')
    info = twitter_stats(twitter_handle)
    print('tweets =',info[0], ' ','following =', info[1], ' ','followers =', info[2], ' ','likes =', info[3])



except Exception as e:
    print(e)
