# # import requests

# # Specify the URL of the API
# url = "https://jsonplaceholder.typicode.com/users/1"

# # Send a GET request to the API
# # response = requests.get(url)

# # Check if the request was successful (status code 200)
# # if response.status_code == 200:
#     # Print the response content
#     ##### FOR FUTURE REFERENCE, this response will actually be of type "list". For practice I am converting it to a string, lists are a big subject and will be revisited another day #####
#     # print(type(str(response.json())))
#     # json_string = str(response.json())

# else:
#     # Print an error message
#     print("Error: Failed to retrieve data from the API")


# data = {
#   "id": 1,
#   "name": "Leanne Graham",
#   "username": "Bret",
#   "email": "Sincere@april.biz",
#   "address": {
#     "street": "Kulas Light",
#     "suite": "Apt. 556",
#     "city": "Gwenborough",
#     "zipcode": "92998-3874",
#     "geo": {
#       "lat": "-37.3159",
#       "lng": "81.1496"
#     }
#   },
#   "phone": "1-770-736-8031 x56442",
#   "website": "hildegard.org",
#   "company": {
#     "name": "Romaguera-Crona",
#     "catchPhrase": "Multi-layered client-server neural-net",
#     "bs": "harness real-time e-markets"
#   }
# }


# print(type(data.name))
# json_string = str(data)