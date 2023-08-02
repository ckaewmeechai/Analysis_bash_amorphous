
import numpy as np
#import matplotlib.mlab as mlab
#import matplotlib.tri as tri
import pandas as pd

# read data and keep it into T, x,y,z
data1 = pd.read_csv('GaO.xyz',delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2)
data1.columns = ["type",'x','y','z']

check=len(data1)

ntot=check
nGa=160
nO=240

T0 = data1['type']
x0 = data1['x']
y0 = data1['y']
z0 = data1['z']
x0 = np.array(x0)
y0 = np.array(y0)
z0 = np.array(z0)

R0= np.zeros(400)
##########################################################

data1 = pd.read_csv('GaO_f.xyz',delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2)
data1.columns = ["type",'x','y','z']

check=len(data1)

ntot=check
nGa=160
nO=240

T1 = data1['type']
x1 = data1['x']
y1 = data1['y']
z1 = data1['z']
x1 = np.array(x1)
y1 = np.array(y1)
z1 = np.array(z1)
R1= np.zeros(400)
C0= np.zeros(400)
########################################################

##################################
x2 = np.zeros(400)
y2 = np.zeros(400)
z2 = np.zeros(400)
t2 = np.zeros(400)


A = np.zeros(400)
##################################



# Classify atomic type 1 or 2
i=0
for i in range(ntot):
    if T1[i] == "Ga":  #Ga type 1
        T1[i] = 1
    else: 
        T1[i] = 2     #O type 2
        
# Classify atomic type 1 or 2
j=0
k=0
n1=0
n2 = np.zeros(400)
n2=160
count=0
sum2=0
sum3=0

gg=0
oo=0
p=0
with open('Ga_displacement.txt', 'w') as f:
    f.write(' Atom\tDisplacement\n')

    for j in range(398):
        k=k+1
        x2[j]=abs(((x1[j]-x0[j])**2+(y1[j]-y0[j])**2+(z1[j]-z0[j])**2)**0.5)

        if x2[j] >= 0.2:
           A[j]=1
           f.write('%5.5s\t'%k)
           f.write('%5.5f\t\n'%x2[j])
 
f.close()

q=0
r=0

k=0
with open('Bond-Ga-O.txt', 'w') as f:
 f.write('Atom1\tAtom2\tDispla1\tDispla2\tper\n')    
 for j in range(398):
    if A[j]>0:
        p=j
        for k in range(398):
            R0[k]=abs(((x0[p]-x0[k])**2+(y0[p]-y0[k])**2+(z0[p]-z0[k])**2)**0.5)
            R1[k]=abs(((x1[p]-x1[k])**2+(y1[p]-y1[k])**2+(z1[p]-z1[k])**2)**0.5)
            C0[k]=(R1[k]-R0[k])/R0[k]*100
            if  R0[k] > 0 and R0[k] < 2.4:
                 q=k+1
                 r=p+1
                 f.write('%5.4s'%q)
                 f.write('%5.4s\t'%r)
                 f.write('%5.2f\t'%R0[k])
                 f.write('%5.2f\t'%R1[k])
                 f.write('%5.2f\n'%C0[k])                         
            q=0
            r=0
f.close()




