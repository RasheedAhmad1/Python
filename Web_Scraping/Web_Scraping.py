from bs4 import BeautifulSoup
import requests
import pandas as pd 

pages = []
titles = []
prices = []
stars = []
urls = []

pages_to_scrap = 5

# Get the raw data
for i in range(1, pages_to_scrap+1):
    page_url = ('http://books.toscrape.com/catalogue/page-{}.html').format(i)
    pages.append(page_url)  
    # Parse the text
for item in pages:
    response = requests.get(item, timeout=(3.05, 5)) # get all content from the 'item'
    # if response: # response.status_code == 200
    #     print('Success!')
    # else: # elif response.status_code == 404
    #     print('Not Found.')
    soup = BeautifulSoup(response.text, 'html.parser') # take all the text from 'page' parse it and return onto the 'soup'
    # soup.prettify() # prettify() will give the actual indentation of the code also
    # Get text from all 'h3'
    for i in soup.findAll('h3'):
        title = i.getText()
        titles.append(title)
        # Get text from all 'h3'
    for j in soup.findAll('p', class_='price_color'):
        price = j.getText()
        prices.append(price) 
        # Get the star ratings for each
    for k in soup.findAll('p', class_='star-rating'):
        for m, n in k.attrs.items():
            star = n[1]
            stars.append(star)
    # Find URLs of all images
    divs = soup.findAll('div', class_='image_container')
    for thumb in divs:
        tags = thumb.find('img', class_='thumbnail')
        url = 'http://books.toscrape.com/'+str(tags['src'])
        clean_urls = url.replace('../', '')
        urls.append(clean_urls)

# Gather all the data in a dictionary
data = {'Titles':titles, 'Prices':prices, 'Star ratings':stars, 'URLs':urls}
# print(data)

# Create dataframe from the dictionary
my_data = pd.DataFrame(data=data)
# print(my_data)
 
# Reset the default index(starting from 0) to 1
my_data.index+=1
print(my_data)

# Export the data as Excel file
# my_data.to_excel('C:/Users/HP/Desktop/Python/Web Scraping/Output.xlsx')
