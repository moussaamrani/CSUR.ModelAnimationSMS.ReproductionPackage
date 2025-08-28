import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'
#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
#data = pd.read_excel(url,sheet_name=sheet_name)
data = pd.read_csv('CORPUS-Final.csv')


target = data["MTL Type"]

GBT= 0
MP= 0
#TEMP= 0
GPPL= 0
GPML= 0
LOGIC= 0
ALGEBRAIC= 0
META=0

for i in range(len(target)):
    if (target[i]=="GBT"): 
        GBT  += 1   
    if (target[i]=="MP"): 
        MP+= 1
   # if (target[i]=="TEMP"): 
    #    TEMP+= 1
    if (target[i]=="GPPL"): 
        GPPL+= 1
    if (target[i]=="META"): 
          META+= 1    
    if (target[i]=="GPML"): 
        GPML+= 1
    if (target[i]=="LOGIC"): 
        LOGIC+= 1
    if (target[i]=="ALGEBRAIC"): 
        ALGEBRAIC+= 1     



GBT = 0
MP = 0
# TEMP = 0
GPPL = 0
GPML = 0
LOGIC = 0
ALGEBRAIC = 0
META=0
for i in range(len(target)):
    if "GB" in str(target[i]).upper(): 
        GBT += 1
    if "META" in str(target[i]).upper(): 
        META += 1    
    if "MP" in str(target[i]).upper(): 
        MP += 1
    # if "TEMP" in str(target[i]).upper():
    #     TEMP += 1
    if "GPP" in str(target[i]).upper(): 
        GPPL += 1
    if "GPM" in str(target[i]).upper(): 
        GPML += 1
    if "LOG" in str(target[i]).upper(): 
        LOGIC += 1
    if "ALG" in str(target[i]).upper(): 
        ALGEBRAIC += 1


Total=GBT+ MP + GPPL+ GPML+LOGIC+ALGEBRAIC  

rateGBT= GBT/Total*100
rateMP= MP/Total*100
#rateTEMP= TEMP/Total*100
rateGPPL= GPPL/Total*100
rateGPML= GPML/Total*100
rateLOGIC= LOGIC/Total*100
rateALGEBRAIC= ALGEBRAIC/Total*100
rateMETA= META/Total*100



Rate = [GBT, MP,GPPL,GPML,LOGIC,ALGEBRAIC,META]

print(Rate)

print(sum(Rate))





my_labels = 'GBT', 'MP','GPPL', 'GPML', 'LOGIC','ALGEBRAIC','META'




my_colors = ['#9f6dd1','#e69191','#ffb84d','#edc9ff','#dccae6','#ffec52','#00ff00']

#purple', 'black', 'pink', 'aqua'

my_explode = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
plt.pie(Rate, labels=my_labels, autopct='%1.1f%%', startangle=180, colors=my_colors,explode=my_explode,  textprops={'fontsize': 20},wedgeprops= {"edgecolor":"black", 'linewidth': 1.7})




# Capture each of the return elements.


#plt.title('Papers distribution: Venue')
plt.title('')
plt.axis('equal')

plt.legend(my_labels, bbox_to_anchor = (1., .95),  title="MTL Type")


plt.savefig("Animation Features-MTL-Type.pdf",dpi=600)
plt.show()