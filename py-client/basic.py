import requests

# endpoint = "https://httpbin.org/anything"
# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"

get_request=requests.get(endpoint , json={"product_id":1})
# print(get_request.text)
# print(get_request.status_code)

print(get_request.json())