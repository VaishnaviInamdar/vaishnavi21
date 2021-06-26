import dbConnection as dc
available=dc.getAllAvailable()
import json
print(available)
data=""
for row in available:
        data= data+"#"+str(row[0])+"@"+str(row[1])+"@"+str(row[2])+"@"+str(row[3])+"@"+str(row[4])+"@"+str(row[5])
        
        
    

#print(stud_json)


    
x={"value":str(data[1:])}
print(json.dumps(x))
    
