import requests

# endpoint = "https://httpbin.org/anything"
# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"

get_response=requests.post(endpoint , json={"title":"Abc", "content":"Hello world", "price":120})
print(get_response.text)
print(get_response.status_code)
print(get_response.json())

# print(get_response.headers)
# print(get_response.text)
# print(get_response)