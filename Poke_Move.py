import requests
name=input("Enter the name of the Pokemon: ")
url="https://pokeapi.co/api/v2/pokemon/{name}".format(name=name)
response = requests.get(url)
dict1=response.json()
print("What do you want to know about",name,"?")
print("1. Abilities")
print("2. Base Experience")
print("3. Height")
print("4. Moves")
print("5. Order")
print("6. Species")
print("7. Stats")
print("8. Types")
print("9. Weight")

a=1
while(a>0):
 choice=int(input("Enter your choice: "))
 if choice==1:
    print("Abilities of",name,"are:", end=" ")
    for i in range(len(dict1["abilities"])):
        print(dict1["abilities"][i]["ability"]["name"])
 elif choice==2:
    print("Base Experience of",name,"is:", dict1["base_experience"])
 elif choice==3:
    print("Height of",name,"is:", dict1["height"])
 elif choice==4:
    print("Moves of",name,"are:", end=" ")
    for i in range(len(dict1["moves"])):
        print(dict1["moves"][i]["move"]["name"])
 elif choice==5:
    print("Order of",name,"is:", dict1["order"])
 elif choice==6:
    print("Species of",name,"is:", dict1["species"]["name"])    
 elif choice==7:
    print("Stats of",name,"are:", end=" ")
    for i in range(len(dict1["stats"])):
        print(dict1["stats"][i]["stat"]["name"])
 elif choice==8:
    print("Types of",name,"are:", end=" ")
    for i in range(len(dict1["types"])):
        print(dict1["types"][i]["type"]["name"])
 elif choice==9:
    print("Weight of",name,"is:", dict1["weight"])
 elif choice==10:
    break
 else:
    print("Invalid choice")