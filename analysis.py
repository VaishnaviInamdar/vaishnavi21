import numpy as np
import matplotlib.pyplot as plt
import random
import json
veg_names={"Apple","Banana","Cucumber","Lemon","Pomegranate","Bell pepper","Chili pepper","Pumpkin","Tomato","Squash","Eggplant"}
N = 3
#r=
ind = np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars
val1=[]
val2=[]
val3=[]


data={"Apple":random.randint(20, 50)/50*100,"Banana":random.randint(20, 50)/50*100,"Cucumber":random.randint(20, 50)/50*100,"Lemon":random.randint(20, 50)/50*100,"Pomegranate":random.randint(20, 50)/50*100 ,"Bell_p":random.randint(20, 50)/50*100,"Chili":random.randint(20, 50)/50*100,"Pumpkin":random.randint(20, 50)/50*100,"Tomato":random.randint(20, 50)/50*100,"Squash":random.randint(20, 50)/50*100
   ,"Eggplant":random.randint(20, 50)/50*100}
print(data)

import numpy as np
import matplotlib.pyplot as plt 
 
  
# creating the dataset

##data = {'C':20, 'C++':15, 'Java':30, 
##        'Python':35}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='green', 
        width = 0.5)
 
plt.xlabel("Vegitable Names")
plt.ylabel("Correct Attempts(Accuraccy)")
plt.title("Vegetable Detection accuraccy")
plt.tight_layout()
plt.show()
