from requests_html import HTMLSession
import sys

session = HTMLSession()
r = session.get('http://ketqua.net')

prize = {
            'giai dac biet':'rs_0_0',
            'giai 1':'rs_1_0',
            'giai 2':['rs_2_0', 'rs_2_1'],
            'giai 3':['rs_3_0', 'rs_3_1', 'rs_3_2', 'rs_3_3', 'rs_3_4', 'rs_3_5'],
            'giai 4':['rs_4_0', 'rs_4_1', 'rs_4_3', 'rs_4_3'],
            'giai 5':['rs_5_0', 'rs_5_1', 'rs_5_2', 'rs_5_3', 'rs_5_4', 'rs_5_5'],
            'giai 6':['rs_6_0', 'rs_6_1', 'rs_6_2'],
            'giai 7':['rs_7_0', 'rs_7_1', 'rs_7_2', 'rs_7_3']
        }
kq = {}
for prizename, id in prize.items():
    if isinstance(id, list):
        kq[prizename] = [r.html.find('#'+_)[0].text for _ in id]
    else:
        kq[prizename] = r.html.find('#'+id)[0].text

lo = {}
for key, value in kq.items():
    if isinstance(value, list):
        lo[key] = ', '.join([value[i][-2:] for i in range(len(value))])
    else:
        lo[key] = value[-2:]

if len(sys.argv) < 2:
    for key, value in kq.items():
        print('{} hom nay la {}'.format(key.title(), value))
else:
    lo1, *rest = sys.argv[1:]
    all_argument = [lo1, *rest]
    for result in all_argument:
        if result in lo.values():
            print('Ban da trung lo voi so {}'.format(result))
        else:
            print('Chuc may man lan sau')