#instagram stats

import urllib.request
import urllib.parse
import re


def instagram_stats():
    x = urllib.request.urlopen('https://www.instagram.com/' + instagram_handle + '/') #saves the raw html page to the variable
    html = x.read()
    iso_info = re.findall(r'<meta content(.*?)- See Instagram photos', str(html)) #using regex to isolate the needed part of the HTML
    info = str(iso_info)
    followers = re.findall(r'"(.*?) Followers', info)
    following = re.findall(r', (.*?) Following', info)
    posts = re.findall(r'Following, (.*?) Posts', info)
    followers_2 = str(followers[0])
    following_2 = str(following[0])
    posts_2 = str(posts[0])
    return followers_2, following_2, posts_2
    




instagram_handle = input('instagram name --->')


try:
    followers_2, following_2, posts_2 = instagram_stats()
    print('followers =',followers_2, ',', 'following =', following_2, ',','posts =',posts_2)
        
        

    
  
except Exception as e:
    print(e)






