import pandas as pd
import matplotlib.pyplot as plt
plt.figure(figsize=(13,6.5))
#gsheetkey = "1XfhT6hZ05RLzMdviMJPjE0E8DPVibb3HRsMWCR2NA6s"
#sheet name
#sheet_name = 'CORPUS'
#url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
#data = pd.read_excel(url,sheet_name=sheet_name)
data = pd.read_csv('CORPUS-Final.csv')


x = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
total = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nbJOUR = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nbCONF = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nbWSHOP = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

target = data["Venue Type"]
target2 = data["Year"]


#for i in range(len(target)):
#    if (target[i]=="CONF" ): 
#        for j in range(len(x)):
#            if (x[j]==target2[i]): 
#                nbCONF[j] += 1   
#    if (target[i]=="WSHOP"): 
#        for j in range(len(x)):
#            if (x[j]==target2[i]):
#                nbWSHOP[j]+= 1 
#    if (target[i]=="JOUR"): 
#        for j in range(len(x)):
#            if (x[j]==target2[i]): 
#                nbJOUR[j] += 1 
                
for i in range(len(target)):
    if str(target[i]).upper().startswith("C"):
        for j in range(len(x)):
            if x[j] == target2[i]:
                nbCONF[j] += 1
    elif str(target[i]).upper().startswith("W"):
        for j in range(len(x)):
            if x[j] == target2[i]:
                nbWSHOP[j] += 1
    elif str(target[i]).upper().startswith("J"):
        for j in range(len(x)):
            if x[j] == target2[i]:
                nbJOUR[j] += 1
                

total = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nbJOUR = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nbCONF = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nbWSHOP = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


for i in range(len(target)):
    if "C" in str(target[i]).upper():  # Vérifie si 'CONF' est contenu
        for j in range(len(x)):
            if x[j] == target2[i]:
                nbCONF[j] += 1   

    if "W" in str(target[i]).upper():  # Vérifie si 'WSHOP' est contenu
        for j in range(len(x)):
            if x[j] == target2[i]:
                nbWSHOP[j] += 1 

    if "J" in str(target[i]).upper():  # Vérifie si 'JOUR' est contenu
        for j in range(len(x)):
            if x[j] == target2[i]:
                nbJOUR[j] += 1


for i in range(25):            
    total[i]=nbJOUR[i]+ nbCONF[i]+nbWSHOP[i]


#---------------------------
#total[7]=2
#total[9]=5
#total[10]=2
#total[15]=3
#total[16]=6
#total[18]=3
#total[19]=3
#total[20]=3

print(total)
print(nbWSHOP)
print(nbJOUR)
print(nbCONF)

print("TOTAL: ", sum(total))
print("WSHOP: ", sum(nbWSHOP))
print("CONF: ", sum(nbCONF))
print("JOUR: ",sum(nbJOUR))

print(sum(nbCONF)+sum(nbWSHOP)+sum(nbJOUR))



plt.plot(x,total,'--',label='Total',linewidth=5,marker='o',color='b')
plt.plot(x,nbJOUR,'-',label='Journal',linewidth=4.5,marker='o',color='#ffcc00')
plt.plot(x,nbCONF,'-',label='Conference',linewidth=4.5,marker='o',color='#ea8b3e')
plt.plot(x,nbWSHOP,'-',label='Workshop',linewidth=4.5,marker='o',color='#8b3eea')

#plt.plot(x,nbWSHOP,'--',label='Workshop',linewidth=1,marker='o')

plt.xlim(2000,2022)
plt.ylim(0,8)

plt.xticks( range(2000,2026,1) ,fontsize = 18, rotation = 45)   # Put x axis ticks every 10 units.
plt.yticks( fontsize = 18)   

#plt.plot(x,nbWSHOP, 'r--', label=(r'$\lambda = 0.3$'))
#plt.plot(x,nbWSHOP,'y',label='KTM',linewidth=1)
#plt.axvline(x = 40.5, ymin = 0.25, ymax = 0.75,linewidth = 4, linestyle ="--", color ='red') 
#plt.axvline(x = 60, ymin = 0.25, ymax = 0.75, linewidth = 4, linestyle ="--", color ='red') 
#plt.title(' Robustness of Cost Models ')
plt.ylabel('Publications Number', fontsize=34)
plt.xlabel('Years', fontsize=28)
plt.legend(prop={'size':18})
plt.grid(linestyle="dotted",color="black")


plt.savefig("Distribution-over-time.pdf",dpi=600)