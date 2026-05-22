name=['Arpan','Satyarth','Shivam','Rohit']
age=[19,20,21,22]
city=['Delhi','Mumbai','Bangalore','Chennai']
d1={'Name':name,'Age':age,'City':city}
choice=input("What do you want to know about the students? (Name/Age/City): ")
if choice in d1:
    print(d1[choice])
else:
    print("Invalid choice.")