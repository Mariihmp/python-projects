#http requests
#requests.get()
import requests
from datetime import datetime
#requests.post() give external system data
#tweeter api to post the tweet ,send your programm
#put update the data
#delete to delete a piece of data

pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = "hj34sdfhsh3443"
USER_NAME = 'xenocyber'
GRAPHID = 'graph1'
date = datetime.now().strftime('%Y%m%d')

pixela_params = {
    'token':TOKEN,#this is like api key the token
    'username':USER_NAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'


}
'''------------------------------making user'''
# response =requests.post(pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
#making post request
graph_param = {
    "id":'graph1',
    "name":'Coding Graph',
    "unit":'h',
    "type":'float',
    "color":'sora',
}
headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(graph_endpoint,json=graph_param,headers=headers)

'''---------------------------------------creating pixel'''
pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPHID}"

today = datetime(year=2023,month=8,day=18)

pixel_data = {
    'date':datetime.now().strftime('%Y%m%d'),
    'quantity':input('how many hours did you code today?'),

}
response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)

'''-----------------------updating the pixel'''
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPHID}/{date}"

new_pixel_data = {
    "quantity":"19"
}
#
# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

'''-----------------------------------------deleting pixel'''
response = requests.delete(url=update_endpoint,headers=headers)
