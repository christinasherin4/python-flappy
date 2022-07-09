print("L.CHRISTINA SHERIN")
print("URK19CS1063")
import re 
loadr=0
with open("input3.txt") as f: 
    for line in f:
        data=line.split("^") 
        if(data[0]=="H"):
            s=str(input("Enter program name:")) 
            s.format("sample")
            print("Name from object: {}".format(data[1])) 
            loadr=int(data[2])
        elif (data[0]=="T"):
            if (loadr != data[1]): 
                loadr = int(data[1])
            add=data[3] 
            ad=re.findall(r'\d\d', add) 
            for ob in ad:
                print("00{} {}".format(loadr, ob)) 
                loadr +=1
            try:
                if(data[4]):
                    add2=data[4] 
                ad2=re.findall(r"\d\d", add2) 
                for ob in ad2:
                    print("00{} {}".format(loadr,ob)) 
                    loadr +=1
            except IndexError: 
                pass
            continue