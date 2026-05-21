l1=list()
def add_task(a):
    l1.append(a)
def show_task():
    print(l1)

i=1
while(i>0):
 c=int(input("Choice :"))
 if c==1:
   b=input("task")
   add_task(b)
 if c==2:
   show_task()
 if c==3:
    break