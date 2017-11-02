import requests
from requests.auth import HTTPBasicAuth

clientid='yDLgq2WYfsOc5UU1ViKaOSy5zJxVZNY0X8tBYyux'
clientsecret=('9u1ADN7BtsU1TSlzXzPo3QhnNQkwfs76Ghv60bEsLtD1XGq2nz68IGQNHhsuNd1vxspyJRjY2jxNDBy4WucJnfXn0OV6Bd7mLPDsUibkhPYB8cSvtU94n7ge3olE8qW9')
auth=('Basic eURMZ3EyV1lmc09jNVVVMVZpS2FPU3k1ekp4VlpOWTBYOHRCWXl1eDo5dTFBRE43QnRzVTFUU2x6WHpQbzNRaG5OUWt3ZnM3NkdodjYwYkVzTHREMVhHcTJuejY4SUdRTkhoc3VOZDF2eHNweUpSalkyanhOREJ5NFd1Y0puZlhuME9WNkJkN21MUERzVWlia2hQWUI4Y1N2dFU5NG43Z2Uzb2xFOHFXOQ==')
params=('marketing&price=price-paid&is_affiliate_agreed=True&is_percentage_deals_agreed=True&language=en')
url='https://www.udemy.com/api-2.0/'

r = requests.post(url, auth=HTTPBasicAuth('clientid', 'clientsecret'))
r=requests.post("Authorization: Basic {auth}https://www.udemy.com/api-2.0/courses")

r.request.headers['Authorization']

print(r)
