api_response = {
    "first_name":"SAI",
    "age": 26,
    "last_name" : "kumar",
    "email": "password123@gmail.com",
    "password": "Test@4321",
    "comission": 10,
    "roles": [
        4
    ]
}

print(api_response)
print(type(api_response))
print(api_response.get("password"))
print(api_response["roles"])
print(api_response.get('roles'))

api_response['age'] = 26
print(api_response)
for key , value in api_response.items():
    print(key.value)