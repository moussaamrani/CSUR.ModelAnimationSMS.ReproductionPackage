import matplotlib.pyplot as plt
import pandas as pd
#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'
#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
#data = pd.read_excel(url,sheet_name=sheet_name)

data = pd.read_csv('CORPUS-Final.csv')

target1 = data["Intent"]

NbDeclared = 0
NbNotDeclared = 0
Total=0
for i in range(len(target1)):
    if (target1[i]=="YES"): 
        NbDeclared  += 1   
    if (target1[i]=="NO" ): 
        NbNotDeclared+= 1

Total=NbDeclared+ NbNotDeclared

rateDeclared= NbDeclared/Total*100
rateNbNotDeclared= NbNotDeclared/Total*100        

print(rateDeclared)      
print(rateNbNotDeclared)   
print(rateDeclared+rateNbNotDeclared)   
  
group_names=['Declared', 'Not Declared']
group_size=[rateDeclared,rateNbNotDeclared]
subgroup_names=['DEBUG', 'UNDERSTAND', 'EDUCATE', '']


target1 = data["Unnamed: 14"]
target2 = data["Unnamed: 15"]
target3 = data["Unnamed: 16"]

isDeclared = data["Intent"]

NbUNDERSTANDYES = 0
NbDEBUGYES = 0
NbEDUCATEYES=0
for i in range(len(target1)):
    if (target1[i]=="DEBUG" and isDeclared[i]=="YES"): 
        NbDEBUGYES  += 1   
    if (target1[i]=="UNDERSTAND" and isDeclared[i]=="YES"): 
        NbUNDERSTANDYES+= 1
    if (target1[i]=="EDUCATE" and isDeclared[i]=="YES"): 
        NbEDUCATEYES+= 1
      
for i in range(len(target2)):
    if (target2[i]=="DEBUG" and isDeclared[i]=="YES"): 
        NbDEBUGYES  += 1   
    if (target2[i]=="UNDERSTAND" and isDeclared[i]=="YES"): 
        NbUNDERSTANDYES+= 1
    if (target2[i]=="EDUCATE" and isDeclared[i]=="YES"): 
        NbEDUCATEYES+= 1
        
for i in range(len(target3)):
    if (target3[i]=="DEBUG" and isDeclared[i]=="YES"): 
        NbDEBUGYES  += 1   
    if (target3[i]=="UNDERSTAND" and isDeclared[i]=="YES"): 
        NbUNDERSTANDYES+= 1
    if (target3[i]=="EDUCATE" and isDeclared[i]=="YES"): 
        NbEDUCATEYES+= 1
        
print(NbUNDERSTANDYES)
print(NbDEBUGYES)
print(NbEDUCATEYES)

TotalPub=NbUNDERSTANDYES+ NbDEBUGYES+NbEDUCATEYES

rateUNDERSTAND= NbUNDERSTANDYES/TotalPub*100
rateDEBUG= NbDEBUGYES/TotalPub*100
rateEDUCATE= NbEDUCATEYES/TotalPub*100

print(rateUNDERSTAND)
print(rateDEBUG)

print(rateEDUCATE)





X1= 63*rateDeclared/100
X2= 33*rateDeclared/100
X3= 4*rateDeclared/100
X4=27




subgroup_size=[X1,X2,X3,X4]

# Create colors
a, b, c=[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]

# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors= 
['lightblue', 'silver'], textprops={'fontsize': 22,'weight':'bold'} )
plt.setp( mypie, width=0.3, edgecolor='white')

# Second Ring (Inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3, 
labels=subgroup_names, labeldistance=0.7, colors=['#ea8b3e', '#4a8123', 
'#62d914', 'white', b(0.4)], textprops={'fontsize': 20})
plt.setp( mypie2, width=0.4, edgecolor='white')
plt.margins(0,0)

# ['silver','lightblue','#9f6dd1']
colorsP=['#fa8620', '#4a8123', '#62d914']
subgroup_names_legs=['DEBUG', 'UNDERSTAND', 'EDUCATE']
#plt.legend(subgroup_names_legs,loc='best',edgecolor='black')



import pylab as plot
params = {'legend.fontsize': 20,
          'legend.handlelength': 2}
plot.rcParams.update(params)


# show it
plt.savefig("Intent-DeclarationVs-non-declaration.pdf",dpi=600)
plt.show()
