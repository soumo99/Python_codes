import requests #used for fetvhing the content  from the url
from bs4 import BeautifulSoup # Beautiful Soup is a Python library for pulling data out of HTML and XML files

req = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

soup = BeautifulSoup(req.content,'html.parser') #html.parser used to parse the html files 

res = soup.title

'''The prettify() method will turn a Beautiful Soup parse tree into a nicely formatted Unicode string, 
with a separate line for each tag and each string'''
# print(soup.prettify()) 

'''The get_text() method returns the text inside the Beautiful Soup or Tag object as a single Unicode string.'''
# print(soup.get_text) 

# print(res.prettify()) # with the title tag 

print(res.get_text()) # without the title tag 