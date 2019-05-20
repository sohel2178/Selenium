from bs4 import BeautifulSoup
import requests

url = 'https://www.linkedin.com/in/sweetkks/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAA8GWycBNccKNYrn_FzfunZUhNSZ-hXMtjU'

source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')

print(soup.prettify())