import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'
#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
#data = pd.read_excel(url,sheet_name=sheet_name)
data = pd.read_csv('CORPUS-Final.csv')

target = data["CLUSTER"]

MTL = ['FSM','REWRITE','KERMETA','PN','XTEND/JAVA','B','VARIOUS','OTHER']



B=0
FSM=0
KERMETA=0
OTHER=0
PN=0
REWRITE=0
VARIOUS=0
XTENDJAVA=0
        

for i in range(len(target)):
    if (target[i]=="B"): 
        B+= 1   
    if (target[i]=="FSM"): 
        FSM += 1 
    if (target[i]=="KERMETA"): 
        KERMETA += 1 
    if (target[i]=="OTHER"): 
        OTHER += 1 
    if (target[i]=="PN"): 
        PN += 1 
    if (target[i]=="REWRITE"): 
        REWRITE += 1 
    if (target[i]=="VARIOUS"): 
        VARIOUS += 1 
    if (target[i]=="XTENDJAVA"): 
        XTENDJAVA += 1 




Total= B + FSM + KERMETA+ OTHER+ PN+ REWRITE+ VARIOUS+ XTENDJAVA

print(PN/Total*100)

print("------------")
#B=6
#FSM=3
#KERMETA=5
#OTHER=4
#PN=7
#REWRITE=12
#VARIOUS=2
#XTENDJAVA=3
        


Total= B+ FSM+ KERMETA+ OTHER+ PN+ REWRITE+ VARIOUS+ XTENDJAVA
print('Total=', Total)



r1= (FSM/Total)*100
r2= (REWRITE/Total)*100
r3= (KERMETA/Total)*100
r4= (PN/Total)*100
r5=  (XTENDJAVA/Total)*100
r6= (B/Total)*100
r7= (VARIOUS/Total)*100
r8= (OTHER/Total)*100


Ratio = [r1, r2,r3,r4,r5,r6,r7,r8]

print(Ratio)

print(sum(Ratio))



my_labels ='FSM','REWRITE','KERMETA','PN','XTEND/JAVA','B','VARIOUS','OTHER'



my_colors = ['#ccda62','#e69191','#ffb84d','#edc9ff','#bdff00','#ffec52','#f8e5d8','#43bccd']

#purple', 'black', 'pink', 'aqua'

my_explode = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

B=6
FSM=3
KERMETA=5
OTHER=4
PN=7
REWRITE=12
VARIOUS=2
XTENDJAVA=3
        
Total= B+ FSM+ KERMETA+ OTHER+ PN+ REWRITE+ VARIOUS+ XTENDJAVA

Ratio = [(FSM/Total)*100, (REWRITE/Total)*100,(KERMETA/Total)*100,(PN/Total)*100,(XTENDJAVA/Total)*100,(B/Total)*100,(VARIOUS/Total)*100,(OTHER/Total)*100]

plt.pie(Ratio, labels=my_labels, autopct='%1.1f%%', startangle=180, colors=my_colors,explode=my_explode,  textprops={'fontsize': 14},wedgeprops= {"edgecolor":"black", 'linewidth': 1.7})

# Capture each of the return elements.
#plt.title('Papers distribution: Venue')
plt.title('')
plt.axis('equal')

#plt.legend(my_labels, bbox_to_anchor = (1., .95),  title="MTL Type")

plt.savefig("Distribution-Clusters-MTL.pdf",dpi=600)
plt.show()



