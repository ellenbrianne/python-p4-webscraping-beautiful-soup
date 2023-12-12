from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

header = doc.select('.heading-primary')

# print(header)
# print(type(header))

# print(header[0].text.strip())

courses = doc.select('.column-item.col-lg-3.col-sm-6')[0].attrs

# for c in courses:
#     print(c.text.strip())

print(courses)