from requests_html import HTMLSession
import sys
import json

session = HTMLSession()
number = sys.argv[1]
tag = sys.argv[2]
link = 'http://api.stackexchange.com/2.2/questions?pagesize={}&order=desc&sort=votes&tagged={}&site=stackoverflow'.format(number, tag)
r = session.get(link)
json_format = json.loads(r.text)
first_key = json_format['items']
print(len(first_key))
title_question = first_key[0]['title']
print('Highest question title:', title_question)

answer_to_question = '{}#{}'.format(first_key[0]['link'], str(first_key[0]['accepted_answer_id']))
print('Link to answer', answer_to_question)
