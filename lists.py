jarjend=[]
elemendid=["Ag","Au","Pt","Cu"]
gaasid=["O2","CO2","He","CH4"]
elemendid_list=list(elemendid)
print(elemendid_list)
while True:
    print("1-lisa element ")
    print("2-liimi kokku ")
    print("3-lisa esikohale ")
    print("4-eemalda element ")
    valik=int(input())
    if valik==1:
        a=input("lisa metall ")
        elemendid_list.append(a)
        print(f"lisatud {a}" ,elemendid_list)
    elif valik==2:
        elemendid_list.extend(gaasid)
        print(elemendid_list)
    elif valik==3:
        a=input("lisa element ")
        i=int(input("kirjuta number 1 "))
        elemendid_list.insert(i-1,a)
        print(elemendid_list)
    elif valik==4:
        a=input("Element,mida soovid eemaldada")
        n=elemendid_list.count(a)
        if n>0:
          for in range(n):
           elemendid_list.remove(a)
        else:
         print("puudub nimekirjas")
        print(elemendid_list)

       
