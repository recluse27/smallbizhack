from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


app = ClarifaiApp(api_key='26e76b22e8394454a9e38befc4ac6fb5')
model = app.models.get('face-v1.3')
image = ClImage(url='https://samples.clarifai.com/face-det.jpg')
m = model.predict([image])

# print(m['status']['description'] == "Ok") #CHECK
# print(m['outputs'][0]['data']['regions'])


def get_boxes(m):
    boxes = []

    for i in m['outputs'][0]['data']['regions']:
        boxes.append(i['region_info']['bounding_box'])
        # print(i)
    return boxes


print(get_boxes(m))
