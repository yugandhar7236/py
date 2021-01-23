from collections import OrderedDict
f=open("C:/Users/yugandhar/OneDrive/Desktop/airlines.csv","r")
c=0
d=OrderedDict()
for line in f:
    if c==0:
        c+=1
        continue
    l=[x for x in line.split(',')]
    name=l[1]+','+l[2]
    if name in d:
        d[name]+=1
    else:
        d[name]=1
print('{')        
for i in d:
    print(i+': '+str(d[i]))
print('}')    
maxi=max(d.values()) 
mini=min(d.values())
for i in d:
    if d[i]==maxi:
        print(i+': '+str(d[i]))
        break
for i in d:
    if d[i]==mini:
        print(i+': '+str(d[i]))
        break        
