name=['Arpan','Satyarth','Shivam','Rohit']
age=[19,20,21,22]
city=['Delhi','Mumbai','Bangalore','Chennai']
d1={'Name':name,'Age':age,'City':city}
choice=input("Who do you want to know about? ")
if choice in name:
    print(d1['Name'][name.index(choice)],"is",d1['Age'][name.index(choice)],"years old and lives in",d1['City'][name.index(choice)]);
else:    
    print("Sorry, we don't have information about", choice)