import requests
name=input("Enter the name of the Pokemon: ")
url="https://pokeapi.co/api/v2/pokemon/{name}".format(name=name)
response = requests.get(url)
dict1=response.json()
print("What do you want to know about",name,"?"
      )

print("One Move of",name, "is:", end=" ")
for i in range(len(dict1["moves"])):
    print(dict1["moves"][i]["move"]["name"])