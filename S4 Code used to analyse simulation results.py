import csv
import numpy as np
import pandas as pd 
import matplotlib as mpl
from scipy.interpolate import griddata
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import os


df = pd.read_csv ("20231003Paper.csv")         

########## 2D charts ##############
###part1#2D how task performance time and COP change with the task difficulty under the "Self Organising allocation"
filt1_df = df.loc[(df.Steps == 5) & (df.IOC == 0.1) & (df.IOA == 0.1) & (df.IOB == 0.1)& (df.MinMemKnow == 0.9) & (df.MT == 0)& (df.Tau == 0.1) & (df.Strategy == "2-Self_Organising")]
filt1_df.sort_values(by=['MinKnow'])              

x =  filt1_df.MinKnow
yy1 = filt1_df.AllocationTime     
yy2 = filt1_df.ExecutionTime
yy3 = filt1_df.PerformanceTime
yy4 = filt1_df.RoTalk 
fig, ax1 = plt.subplots()
plt.ylim(10,140)    
plt.xlim(0.03,0.97)
plt.bar(x,yy1, width= 0.02, color = 'deepskyblue',bottom=yy2)
plt.bar(x,yy2, width= 0.02, color = 'blue')
plt.plot(x,yy3,'x-',color = 'green')
a = np.arange (0.1,1,0.1)
b = range(0, 140, 20)
plt.legend(["Performance Time($T_{perf}$)","Coordination Time($T_{coor}$)","Execution Time ($T_{exec}$)"],loc='upper right',fontsize=12)     #,fontsize = 'small', loc='lower right'
plt.xlabel('Task Difficulty ($TK_H$)',fontsize=14)    
plt.ylabel('Performance Time',fontsize=14) 
plt.xticks(a)
plt.xticks(fontsize=14)
plt.yticks(b)
plt.yticks(fontsize=14)

ax2 = ax1.twinx()
ax2.plot(x, yy4, '*-',color='orangered')
ax2.set_xlim(0.03,0.97)
ax2.set_ylim(-5,95)
c=range(0, 100, 20)
plt.tight_layout()
plt.legend(["$PoC$ (%)"],loc='upper center',fontsize=12)     
plt.ylabel('Percentage of Coordination Time (PoC)(%)',fontsize=14) 
plt.yticks(c)
plt.yticks(fontsize=14)
plt.show()

# ##part1 2D how task performance time and COP change with the task difficulty under the "top down allocation"
filt1_df = df.loc[(df.Steps == 5)& (df.MinMemKnow == 0.6) & (df.IOC == 0.1) & (df.IOA == 0.1) & (df.IOB == 0.1) & (df.MT == 0)& (df.Tau == 0.1) & (df.Strategy == "1-Top_Down")]
filt1_df.sort_values(by=['MinKnow'])                  

x =  filt1_df.MinKnow
yy1 = filt1_df.AllocationTime 
yy2 = filt1_df.ExecutionTime
yy3 = filt1_df.PerformanceTime
yy4 = filt1_df.RoTalk 
fig, ax1 = plt.subplots()
plt.ylim(10,140)    #(0,0.4)   (0,100) 
plt.xlim(0.03,0.97)

plt.bar(x,yy1, width= 0.02, color = 'darkgray',bottom=yy2)
plt.bar(x,yy2, width= 0.02, color = 'gray')
plt.plot(x,yy3,'x-',color = 'black')
a = np.arange (0.1,1,0.1)
b = range(0, 140, 20)
plt.xlabel('Task Difficulty ($TK_H$)',fontsize=14)
plt.ylabel('Performance Time',fontsize=14) 
plt.xticks(a)
plt.yticks(b)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
ax2 = ax1.twinx()
ax2.plot(x, yy4, '*-',color='orangered')
ax2.set_xlim(0.03,0.97)
ax2.set_ylim(-5,70)
c=range(0, 75, 20)
plt.tight_layout()
plt.ylabel('Percentage of Coordination Time (PoC)(%)',fontsize=14) 
plt.yticks(c)
plt.yticks(fontsize=14)
plt.show()

# ##part1#2D Compare how task difficulty affect task performance time under two task allocation strategies
filt1_df = df.loc[(df.IOC == 0.1) & (df.IOA == 0.1) & (df.IOB == 0.1)& (df.MT == 0) & (df.Steps == 5)& (df.Tau == 0.1) ] 
y1 = filt1_df.loc[(filt1_df.MinMemKnow== 0.6) & (filt1_df.Strategy == "1-Top_Down")]      
y2 = filt1_df.loc[(filt1_df.MinMemKnow== 0.6) & (filt1_df.Strategy == "2-Self_Organising")]  
x =  y1.MinKnow
plt.figure(figsize=(6,4))
plt.ylim(0,140)   
plt.xlim(0.03,0.97)
yy11 = y1.AllocationTime 
yy12 = y1.ExecutionTime
yy13 = y1.PerformanceTime
plt.bar(x-0.0075,yy11, width= 0.015, label= '$HoTA$ $T_{coor}$', color = 'darkgray',bottom=yy12) 
plt.bar(x-0.0075,yy12, width= 0.015, label= '$HoTA$ $T_{exec}$', color = 'gray')  
plt.plot(x-0.0075,yy13,'.-',label='$HoTA$ $T_{perf}$', color = 'gray') 

yy21 = y2.AllocationTime 
yy22 = y2.ExecutionTime 
yy23 = y2.PerformanceTime 
plt.bar(x+0.0075,yy21, width= 0.015,label= '$SoTA$ $T_{coor}$',color = 'dodgerblue',bottom=yy22) #hatch='/', 2 3
plt.bar(x+0.0075,yy22, width= 0.015,label= '$SoTA$ $T_{exec}$',color = 'blue') 
plt.plot(x+0.0075,yy23,'x-',label= '$SoTA$ $T_{perf}$',color = 'blue') 
a = np.arange (0.1,1,0.1)
b = range(0, 141, 20)
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,2,3,1,4,5]

plt.xlabel('Task Difficulty ($TK_H$)',fontsize=14)
plt.ylabel('Performance Time ($T_{perf}$)',fontsize=14)       #Overall Satisfaction    !!!SSC2021 Fig3
plt.xticks(a)
plt.yticks(b)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# ###(part1)Compare how task difficulty affect group performance under two task allocation strategies
filt1_df = df.loc[(df.IOC == 0.1) & (df.IOA == 0.1) & (df.IOB == 0.1)& (df.MT == 0) & (df.Steps == 5)& (df.Tau == 0.1) ] 
y1 = filt1_df.loc[(filt1_df.MinMemKnow== 0.3) & (filt1_df.Strategy == "1-Top_Down")]       
y2 = filt1_df.loc[(filt1_df.MinMemKnow== 0.6) & (filt1_df.Strategy == "1-Top_Down")]
y3 = filt1_df.loc[(filt1_df.MinMemKnow== 0.9) & (filt1_df.Strategy == "1-Top_Down")]
y4 = filt1_df.loc[(filt1_df.MinMemKnow== 0.3) & (filt1_df.Strategy == "2-Self_Organising")]      
y5 = filt1_df.loc[(filt1_df.MinMemKnow== 0.6) & (filt1_df.Strategy == "2-Self_Organising")]
y6 = filt1_df.loc[(filt1_df.MinMemKnow== 0.9) & (filt1_df.Strategy == "2-Self_Organising")]

y1 = y1.sort_values(by=['MinKnow'],ascending=True)
x =  y1.MinKnow
yy1 = y1.AverageMotiv
yy2 = y2.AverageMotiv       
yy3 = y3.AverageMotiv 
yy4 = y4.AverageMotiv 
yy5 = y5.AverageMotiv       
yy6 = y6.AverageMotiv 
plt.ylim (0,0.5)   
plt.xlim(0.05,0.95)      
plt.plot(x,yy1,'.-',color='teal',linewidth=1)
plt.plot(x,yy2,'x--',color='teal',linewidth=1)
plt.plot(x,yy3,'*-.',color='teal',linewidth=1)
plt.plot(x,yy4,'.-',color='blue',linewidth=1)
plt.plot(x,yy5,'x--',color='blue',linewidth=1)
plt.plot(x,yy6,'*-.',color='blue',linewidth=1)

a = np.arange (0.1,1,0.1)
b = np.arange (0, 0.55, 0.1)
plt.legend(["$HoTA,TC=0.3$","$HoTA,TC=0.6$","$HoTA,TC=0.9$","$SoTA,TC=0.3$","$SoTA,TC=0.6$","$SoTA,TC=0.9$"],loc='upper right',ncol=2,fontsize=11)
plt.xlabel('Task Difficulty ($TK_H$)',fontsize=14)   
plt.ylabel('Group Satisfaction ($GS$)',fontsize=14)   
plt.xticks(a)
plt.yticks(b)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# ###part2#2D stacked bars ##compare the performance time under two different task allocation strategies
filt1_df = df.loc[(df.IOC == 0.1) & (df.IOA == 0.1) & (df.IOB == 0.1)& (df.MT == 0)& (df.MinMemKnow== 0.3) & (df.MinKnow == 0.9)& (df.Tau == 0.1)& (df.Steps >= 1)]
y1 = filt1_df.loc[filt1_df.Strategy == "1-Top_Down"]    
y2 = filt1_df.loc[filt1_df.Strategy == "2-Self_Organising"]
x =  y1.Steps
plt.figure(figsize=(6,4))
plt.ylim(10,160) 
plt.xlim(0.7,25.3)
yy11 = y1.AllocationTime 
yy12 = y1.ExecutionTime
yy13 = y1.PerformanceTime
plt.bar(x-0.15,yy11, width= 0.3, label= '$HoTA$ $T_{coor}$', color = 'darkgray',bottom=yy12)
plt.bar(x-0.15,yy12, width= 0.3, label= '$HoTA$ $T_{exec}$', color = 'gray')
plt.plot(x-0.15,yy13,'.-',label='$HoTA$ $T_{perf}$', color = 'gray')

yy21 = y2.AllocationTime 
yy22 = y2.ExecutionTime 
yy23 = y2.PerformanceTime 
plt.bar(x+0.15,yy21, width= 0.3,label= '$SoTA$ $T_{coor}$',color = 'dodgerblue',bottom=yy22) 
plt.bar(x+0.15,yy22, width= 0.3,label= '$SoTA$ $T_{exec}$',color = 'blue')
plt.plot(x+0.15,yy23,'x-',label= '$SoTA$ $T_{perf}$',color = 'blue')
a = range (1,26,2) 
b = range (10,161,20) 
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,2,3,1,4,5]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc='upper right',fontsize=12,ncol=2)   
plt.xlabel('Steps ($T$)',fontsize=14)                        
plt.ylabel('Performance Time ($T_{perf}$)',fontsize=14)     
plt.xticks(a)
plt.yticks(b)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

##part2###compare the group performanec under two different task allocation strategies
filt1_df = df.loc[(df.IOC == 0.1) & (df.IOA == 0.1) & (df.IOB == 0.1)& (df.MT == 0)& (df.MinMemKnow== 0.3) & (df.MinKnow == 0.9)& (df.Tau == 0.1)& (df.Steps >= 1)]
y1 = filt1_df.loc[filt1_df.Strategy == "1-Top_Down"]       
y2 = filt1_df.loc[filt1_df.Strategy == "2-Self_Organising"]
y1 = y1.sort_values(by=['Steps'],ascending=True)

x =  y1.Steps      
yy1 = y1.AverageMotiv  
yy2 = y2.AverageMotiv  
plt.figure(figsize=(6,4))
plt.ylim(0,0.7)      
plt.xlim(1,25)       
plt.plot(x,yy1,'.-',color='dimgrey',linewidth=1)
plt.plot(x,yy2,'x-',color='blue',linewidth=1)
a = range (1,26,2) 
b = np.arange (0,0.75,0.1)
plt.legend(["$HoTA$","$SoTA$"],loc='upper left',fontsize=12)
plt.xlabel('Steps ($T$)',fontsize=14)   
plt.ylabel('Group Satisfaction ($GS$)',fontsize=14)    
plt.xticks(a)
plt.yticks(b)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

########## 3D charts ##############
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

###Appendix part1# the relationships of task difficulty and team capability and performance time
filt_df = df.loc[(df.IOC == 0.1) & (df.IOA == 0.1) & (df.IOB == 0.1)& (df.MT == 0)& (df.Tau == 0.1) & (df.Strategy =="1-Top_Down") & (df.Steps == 5)]    
filt_df = filt_df.reset_index()                                                 
filt_df1=filt_df[["IOC","IOA","IOB","Tau","MT","Steps","MinMemKnow","MinKnow","AllocationTime","ExecutionTime","PerformanceTime","AverageMoC","AverageMoA","AverageMoB","AverageMotiv","RoTalk","Overallknow"]]
filt_df1=filt_df1.sort_values(by=["MinMemKnow","MinKnow"],ascending=True)
df = pd.DataFrame(filt_df1)                 

x = np.arange (0.2,1.1,0.1)                       
y = np.arange (0.05,1,0.05)               
X,Y = np.meshgrid(x,y,indexing = 'ij')
Z = filt_df1.PerformanceTime       
Z = np.expand_dims(Z,axis = 1)
Z = Z.reshape(9,19)
Z1 = filt_df1.RoTalk                              
Z1 = np.expand_dims(Z1,axis = 1)
C = Z1.reshape(9,19)
scamap = plt.cm.ScalarMappable(cmap='summer' )       
fcolors = scamap.to_rgba(C)

ax.plot_surface (X, Y, Z, facecolors=fcolors, cmap='summer' ,vmin=10, vmax=160)
clb = fig.colorbar(scamap,ax=[ax],location='right',pad = 0.05)
ax.view_init(30,380)
clb.set_label('Percentage of Coordination Time ($PoC$)(%)',fontsize=12) 
clb.ax.tick_params(labelsize=12)
ax.set_title('$HoTA$')                        
ax.set_xlabel('Team Capability ($TC$)',fontsize=12)
ax.set_ylabel('Task Difficulty ($TK_H$)',fontsize=12)
ax.set_zlabel('Performance Time ($T_{perf}$)',fontsize=12) 
ax.set_zlim(10,160)
ax.tick_params(labelsize=12)
plt.show()


###Appendix#4D# how performance time change with steps and task difficulty  under two task allocation strategies
filt_df = df.loc[ (df.MT ==0) & (df.IOC == 0.1) & (df.IOA == 0.1) & (df.IOB == 0.1)& (df.Tau == 0.1)& (df.MinMemKnow== 0.3)&(df.Strategy == "2-Self_Organising") & (df.Steps >= 1)]  
filt_df = filt_df.reset_index()                                                                          
filt_df1=filt_df[["Steps","MinKnow","AllocationTime","ExecutionTime","PerformanceTime","AverageMoC","AverageMoA","AverageMoB","AverageMotiv","RoTalk"]]
filt_df1=filt_df1.sort_values(by=['Steps','MinKnow'],ascending=True)          
y = np.arange (0.05,1,0.05)                 
x = range (1,31,1)                         
X,Y = np.meshgrid(x,y,indexing = 'ij')
Z = filt_df1.PerformanceTime               
Z = np.expand_dims(Z,axis = 1)
Z = Z.reshape(30,19)

Z1 = filt_df1.RoTalk                        
Z1 = np.expand_dims(Z1,axis = 1)
C = Z1.reshape(30,19)
scamap = plt.cm.ScalarMappable(cmap='winter')    
fcolors = scamap.to_rgba(C)
ax.plot_surface (X, Y, Z, facecolors=fcolors, cmap='winter',vmin=0, vmax=160)
clb = fig.colorbar(scamap,ax=[ax],location='left',pad = 0.05)
clb.set_label('Percentage of Coordination Time ($PoC$)(%)',fontsize=12)
clb.ax.tick_params(labelsize=12)
ax.view_init(20,330)
ax.set_xlabel('Steps ($T$)',fontsize=12)
ax.set_ylabel('Task Difficulty ($TK_H$)',fontsize=12)
ax.set_zlabel('Performance Time ($T_{perf}$)',fontsize=12)         
ax.set_zlim(10,160)     
scamap.set_clim(0,95)       
ax.tick_params(labelsize=12)
plt.show()

###Appendix##how group satisfaction change with the task difficulty and steps under two allocation strategies
filt_df = df.loc[(df.MT ==0) & (df.IOC == 0.1)&(df.IOA == 0.1) & (df.IOB == 0.1)& (df.Tau == 0.1)& (df.MinMemKnow == 0.9) & (df.Strategy == "1-Top_Down") & (df.Steps >= 1)] 
filt_df = filt_df.reset_index()                                                   
filt_df1=filt_df[["IOC","IOA","IOB","Tau","MT","Steps","MinKnow","AllocationTime","ExecutionTime","PerformanceTime","AverageMoC","AverageMoA","AverageMoB","AverageMotiv","A1Motiv","RoTalk"]]
filt_df1=filt_df1.sort_values(by=['Steps','MinKnow'],ascending=True) 
df = pd.DataFrame(filt_df1)  

y = np.arange (0.05,1,0.05)                 
x = range (1,31,1)                   
X,Y = np.meshgrid(x,y,indexing = 'ij')
Z = filt_df1.AverageMotiv                     
Z = np.expand_dims(Z,axis = 1)
Z = Z.reshape(30,19)
Surf = ax.plot_surface (X,Y,Z,cmap=plt.get_cmap("summer"),vmin=0, vmax=0.5) 
clb = plt.colorbar(Surf,ax=[ax], location='right')
clb.ax.tick_params(labelsize=12)
ax.view_init(20,220)
ax.set_xlabel('Steps ($T$)',fontsize=12)
ax.set_ylabel('Task Difficulty ($TK_H$)',fontsize=12) 
ax.set_zlabel ('Group Satisfaction ($GS$)',fontsize=12)   
ax.set_zlim(0,0.5)                          
ax.tick_params(labelsize=12)
plt.show()




