import requests

api_key = ''
base_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

# data = {
#   "name": "Just Demo UPDATED",
#   "email": "sample@gmail.com",
#   "phone": "123456",
#   "website": "demo.com"
# }

res = requests.delete(base_url + 'users/11')
print(res.json())