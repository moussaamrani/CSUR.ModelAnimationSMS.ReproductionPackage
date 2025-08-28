import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCratio2NA6s"
#sheet name
#sheet_name = 'CORPUS'
#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
#data = pd.read_excel(url,sheet_name=sheet_name)
data = pd.read_csv('CORPUS-Final.csv')

target = data["Unnamed: 12"]

# set null 
TOPCASED= 0
GEMOC= 0
ATOMPM= 0
MEEDUSE= 0
VMTS= 0
RMT= 0
DiaMeta= 0
TROPIC= 0
GenGED= 0
OTHER= 0


for i in range(len(target)):
    if (target[i]=="TOPCASED"): 
        TOPCASED   += 1   
    if (target[i]=="GEMOC"): 
        GEMOC += 1 
    if (target[i]=="ATOMPM"): 
        ATOMPM += 1 
    if (target[i]=="MEEDUSE"): 
        MEEDUSE += 1 
    if (target[i]=="VMTS"): 
        VMTS += 1 
    if (target[i]=="RMT"): 
        RMT += 1 
    if (target[i]=="DiaMeta"): 
        DiaMeta += 1 
    if (target[i]=="TROPIC"): 
        TROPIC += 1 
    if (target[i]=="GenGED"): 
        GenGED += 1 
    if (target[i]=="OTHER"): 
        OTHER += 1  



TOPCASED = 0
GEMOC = 0
ATOMPM = 0
MEEDUSE = 0
VMTS = 0
RMT = 0
DiaMeta = 0
TROPIC = 0
GenGED = 0
OTHER = 0
AltaRica= 0

for i in range(len(target)):
    if "TOP" in str(target[i]).upper():
        TOPCASED += 1
    if "GEM" in str(target[i]).upper():
        GEMOC += 1
    if "ATO" in str(target[i]).upper():
        ATOMPM += 1
    if "MEE" in str(target[i]).upper():
        MEEDUSE += 1
    if "VM" in str(target[i]).upper():
        VMTS += 1
    if "RM" in str(target[i]).upper():
        RMT += 1
    if "DI" in str(target[i]).upper():
        DiaMeta += 1
    if "TR" in str(target[i]).upper():
        TROPIC += 1
    if "GEN" in str(target[i]).upper():
        GenGED += 1
    if "OTH" in str(target[i]).upper():
        OTHER += 1
    if "Alt" in str(target[i]).upper():
         AltaRica += 1



print("------------")

        
#TOPCASED= 2
#GEMOC= 7
#ATOMPM= 5
#MEEDUSE= 4
#VMTS= 3
#RMT= 3
#DiaMeta= 2
#TROPIC= 3
#GenGED= 2
#OTHER= 11

Total= GEMOC+ ATOMPM+ MEEDUSE+ VMTS+ RMT+ DiaMeta+ TROPIC+ GenGED+ OTHER+TOPCASED+ AltaRica
print(Total)
ratio1= TOPCASED/Total*100
ratio2= GEMOC/Total*100
ratio3= ATOMPM/Total*100
ratio4= MEEDUSE/Total*100
ratio5= VMTS/Total*100
ratio6= RMT/Total*100
ratio7= DiaMeta/Total*100
ratio8= TROPIC/Total*100
ratio9= GenGED/Total*100
ratio10= OTHER/Total*100
ratio11= AltaRica/Total*100



Ratio = [ratio1, ratio2,ratio3,ratio4,ratio5,ratio6,ratio7,ratio8,ratio9,ratio10,ratio11]

print(Ratio)

print(sum(Ratio))



my_labels = 'TOPCASED','GEMOC','ATOMPM','MEEDUSE','VMTS','RMT','DiaMeta','TROPIC','GenGED','OTHER','AltaRica'




my_colors =  ['#ccda62','#e69191','#ffb84d','lavender','#bdff00','#ffec52','#f8e5d8','#43bccd','olive','peru','#ff0000']

#purple', 'black', 'pink', 'aqua'

my_explode = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
plt.pie(Ratio, labels=my_labels, autopct='%1.1f%%', startangle=180, colors=my_colors,explode=my_explode,  textprops={'fontsize': 16},wedgeprops= {"edgecolor":"black", 'linewidth': 1.7})




# Capture each of the return elements.


#plt.title('Papers distribution: Venue')
plt.title('')
plt.axis('equal')

#plt.legend(my_labels, bbox_to_anchor = (1., .95),  title="MTL Cluster")


plt.savefig("Distribution-Clusters-Tools.pdf",dpi=600)
plt.show()