from requests_html import HTMLSession
import json
import time


with open('api.json', 'r') as f:
    api = json.load(f)
location = '&location=10.779614,106.69925'
radius = '&radius=5000'
type = '&type=cafe'
key = '&key=' + api['api_key']
query = 'query=coffee'
link = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
final_link = '{}{}{}{}{}{}'.format(link, query, location, radius, type, key)
next_page = True
results = []
while next_page:
    session = HTMLSession()
    r = session.get(final_link)
    json_format = r.json()
    third_key = json_format['results']
    for coffee in third_key:
        results.append(coffee['name'])
    if 'next_page_token' in json_format:
        page_token = 'pagetoken='
        final_link = '{}{}{}{}'.format(link, page_token, json_format['next_page_token'], key)
        time.sleep(20)
        # 20 can be change to another value , I used 20 to make sure the next_page_token works
    else:
        next_page = False
with open('hcm_coffee.json', 'w+', encoding='utf-8') as file:
    data = json.dumps(results[:50], ensure_ascii=False)
    file.write(data)