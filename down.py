name = "vfghjsdfghjk"
if len(name)<3:
    print("Name must be atleast 3 characters")
elif len(name)>50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")
    
weight = int(input("Weight:"))
unit = input('(L)bs or (K)g:')
if unit.upper() == "L":
   converted =  weight*0.45
   print(f"You are {converted} kilos")
else:
    converted = weight/0.45
    print(f"You are {converted} pounds")
  
i = 1
while i <= 5:
    print('*' * i)
    i=i+1
print("Done")
    

 
 