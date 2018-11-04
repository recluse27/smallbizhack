from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
#from tsheets.api import TSheets
import requests
import datetime

app = ClarifaiApp(api_key='26e76b22e8394454a9e38befc4ac6fb5')
# api = TSheets("S.7__f44260bbed17560d74945e576b802071531cc39b")

model = app.models.get('celeb-v1.3')
# image = ClImage(url='https://samples.clarifai.com/celebrity.jpeg')
image = ClImage(file_obj=open('C:/st.jpg', 'rb'))
m = model.predict([image])

# print(m['outputs'])


def get_persons(m):
    pers = []

    for i in m['outputs'][0]['data']['regions']:
        if i['data']['face']['identity']['concepts'][0]['value'] > 0.5:
            pers.append(i['data']['face']['identity']['concepts'][0]['name'])
        # print(i)
    return pers


def is_emp(prn):
    r = requests.get("https://rest.tsheets.com/api/v1/users", headers={'Authorization': "Bearer S.7__f44260bbed17560d74945e576b802071531cc39b"})
    # print(r.json()['results']['users'])
    data = r.json()['results']['users']
    for i in data:
        if data[i]['first_name'].lower() == prn[0] and data[i]['last_name'].lower() == prn[1]:
            # print(i)
            return i
    return 0


# print(m['outputs'][0]['data']['regions'])
print(get_persons(m))

# list_of_results = api.timesheets.where(start_date=, end_date=some_end).all()
# list_of_results = api.timesheets.all()
# for item in list_of_results:
#     print(item)
# r = requests.get("https://rest.tsheets.com/api/v1/users", headers={'Authorization': "Bearer S.7__f44260bbed17560d74945e576b802071531cc39b"})
# print(r.json()['results']['users'])

res = is_emp(get_persons(m)[0].split(' '))
if res:
    print(res)
    # r = requests.post(
    #     {
    #         "data": [
    #             {
    #                 "user_id": res,
    #                 "type": "manual",
    #                 "date": "2018-11-03",
    #                 "jobcode_id": 0,
    #                 "duration": 28800
    #             }]
    #     }, "https://rest.tsheets.com/api/v1/timesheets", headers={'Authorization': "Bearer S.7__f44260bbed17560d74945e576b802071531cc39b",
    #                                                               'Content-Type': "application/json"})
    # {
    #     "data":
    #         [
    #             {
    #              "user_id": res,
    #              "type": "regular",
    #              # "start": datetime.datetime.now(),
    #              "start": "2013-07-23T10:00:00-07:00",
    #              "end": "2013-07-23T13:10:23-07:00",
    #              "jobcode_id": "0",
    #              "notes": "This is a test of the emergency broadcast system"
    #              #    ,
    #              # "customfields": {
    #              #  "19142":"Item 1",
    #              #  "19144":"Item 2"
    #              # }
    #                 # ,
    #              # "attached_files": [
    #              #  50692,
    #              #  44878
    #              # ],
    #             }
    #           ]
    # }, headers={'Authorization': "Bearer S.7__f44260bbed17560d74945e576b802071531cc39b"})
# print(r)