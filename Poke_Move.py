import requests
name=input("Enter the name of the Pokemon: ")
url="https://pokeapi.co/api/v2/pokemon/{name}".format(name=name)
response = requests.get(url)
dict1=response.json()
print("One Move of",name, "is:", end=" ")
print(dict1["moves"][0]["move"]["name"])