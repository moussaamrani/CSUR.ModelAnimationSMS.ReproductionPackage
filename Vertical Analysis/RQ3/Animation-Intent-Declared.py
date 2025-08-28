import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('CORPUS-Final.csv')

target1 = data["Unnamed: 14"]
target2 = data["Unnamed: 15"]
target3 = data["Unnamed: 16"]

isDeclared = data["Intent"]
print(isDeclared)

nbUNDERSTAND = 0
nbDEBUG = 0
nbEDUCATE=0
for i in range(len(target1)):
    if (target1[i]=="DEBUG" and isDeclared[i]=="YES"): 
        nbDEBUG  += 1   
    if (target1[i]=="UNDERSTAND" and isDeclared[i]=="YES"): 
        nbUNDERSTAND+= 1
    if (target1[i]=="EDUCATE" and isDeclared[i]=="YES"): 
        nbEDUCATE+= 1
      
for i in range(len(target2)):
    if (target2[i]=="DEBUG" and isDeclared[i]=="YES"): 
        nbDEBUG  += 1   
    if (target2[i]=="UNDERSTAND" and isDeclared[i]=="YES"): 
        nbUNDERSTAND+= 1
    if (target2[i]=="EDUCATE" and isDeclared[i]=="YES"): 
        nbEDUCATE+= 1
        
for i in range(len(target3)):
    if (target3[i]=="DEBUG" and isDeclared[i]=="YES"): 
        nbDEBUG  += 1   
    if (target3[i]=="UNDERSTAND" and isDeclared[i]=="YES"): 
        nbUNDERSTAND+= 1
    if (target3[i]=="EDUCATE" and isDeclared[i]=="YES"): 
        nbEDUCATE+= 1
        
print(nbUNDERSTAND)
print(nbDEBUG)
print(nbEDUCATE)

TotalPub=nbUNDERSTAND+ nbDEBUG+nbEDUCATE

rateUNDERSTAND= nbUNDERSTAND/TotalPub
rateDEBUG= nbDEBUG/TotalPub
rateEDUCATE= nbEDUCATE/TotalPub




ratio = [rateDEBUG,rateUNDERSTAND,rateEDUCATE]








my_labels = 'DEBUG', 'UNDERSTAND', 'EDUCATE'




my_colors = ['#ccff33','#f0fff1','#00f59b']

#purple', 'black', 'pink', 'aqua'

my_explode = (0, 0.1, 0.1)
plt.pie(ratio, labels=my_labels, autopct='%1.1f%%', startangle=180,shadow = True, colors=my_colors,explode=my_explode, wedgeprops= {"edgecolor":"black", 'linewidth': 1.7})




# Capture each of the return elements.


#plt.title('Papers distribution: Venue')
plt.title('')
plt.axis('equal')

plt.legend(my_labels, bbox_to_anchor = (1., .95),  title="Intent")


plt.savefig("Animation-intent-Declared.pdf",dpi=600)
plt.show()