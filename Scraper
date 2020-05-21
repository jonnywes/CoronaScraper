from bs4 import BeautifulSoup
from urllib.request import urlopen
import string



url = "https://www.worldometers.info/coronavirus/country/us/"

# We use try-except incase the request was unsuccessful because of 
# wrong URL
try:
   page = urlopen(url)
except:
   print("Error opening the URL")

soup = BeautifulSoup(page, 'html.parser')

#use BeautifulSoup’s soup.find() method to search for the tag <span style="color:#aaa">38,164        </span>

content = soup.find('span', {'style': 'color:#aaa">38,164        </span>'})


num = string.digits
for i in content.findAll('Coronavirus'):
    article = article + ' ' +  i.text
print(article)
'''

#saving
with open('scrape_info.txt', 'w') as file:
        file.write(article)
'''

