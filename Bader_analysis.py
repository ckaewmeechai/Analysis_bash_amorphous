
import numpy as np
#import matplotlib.mlab as mlab
#import matplotlib.tri as tri
import pandas as pd



########################################################## Q-2
data1 = pd.read_csv("O_288_q-2/ACF.dat",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2,nrows=399)
data1.columns = ['No','X','Y','Z','CH','MI','VO']

check=399

No = np.array(check)
X = np.array(check)
Y = np.array(check)
Z = np.array(check)
CH = np.array(check)
MI = np.array(check)
VO = np.array(check)

No = data1['No']
X = data1['X']
Y = data1['Y']
Z = data1['Z']
CH = data1['CH']
MI = data1['MI']
VO = data1['VO']

Con=27.21138386
#Eq_2A1=(Ev[1756]-Ev[1755])*Con
#Eq_2A2=(Ev[1757]-Ev[1755])*Con
chargea=sum(CH[0:79])/79
Ga_2=np.zeros_like(CH)

with open('Bader_sum.txt', 'w') as f:
 for i in range(399):
    Ga_2[i]=13-CH[i]
    if Ga_2[i] <= 1.6:
            q=i+1
            print(Ga_2[i])
            f.write('%5.4s\t'%q)
            f.write('-2\t%5.2f\n'%Ga_2[i])
            q=0
############################################### Q-1
data1 = pd.read_csv("O_288_q-1/ACF.dat",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2,nrows=399)
data1.columns = ['No','X','Y','Z','CH','MI','VO']

check=399

No = np.array(check)
X = np.array(check)
Y = np.array(check)
Z = np.array(check)
CH = np.array(check)
MI = np.array(check)
VO = np.array(check)

No = data1['No']
X = data1['X']
Y = data1['Y']
Z = data1['Z']
CH = data1['CH']
MI = data1['MI']
VO = data1['VO']

Con=27.21138386
#Eq_2A1=(Ev[1756]-Ev[1755])*Con
#Eq_2A2=(Ev[1757]-Ev[1755])*Con
chargea=sum(CH[0:79])/79
Ga_2=np.zeros_like(CH)

with open('Bader_sum.txt', 'a') as f:
 for i in range(399):
    Ga_2[i]=13-CH[i]
    if Ga_2[i] <= 1.6:
            q=i+1
            print(Ga_2[i])
            f.write('%5.4s\t'%q)
            f.write('-1\t%5.2f\n'%Ga_2[i])
            q=0
############################################### Q0
data1 = pd.read_csv("O_288_q0/ACF.dat",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2,nrows=399)
data1.columns = ['No','X','Y','Z','CH','MI','VO']

check=399

No = np.array(check)
X = np.array(check)
Y = np.array(check)
Z = np.array(check)
CH = np.array(check)
MI = np.array(check)
VO = np.array(check)

No = data1['No']
X = data1['X']
Y = data1['Y']
Z = data1['Z']
CH = data1['CH']
MI = data1['MI']
VO = data1['VO']

Con=27.21138386
#Eq_2A1=(Ev[1756]-Ev[1755])*Con
#Eq_2A2=(Ev[1757]-Ev[1755])*Con
chargea=sum(CH[0:79])/79
Ga_2=np.zeros_like(CH)

with open('Bader_sum.txt', 'a') as f:
 for i in range(399):
    Ga_2[i]=13-CH[i]
    if Ga_2[i] <= 1.6:
            q=i+1
            print(Ga_2[i])
            f.write('%5.4s\t'%q)
            f.write('0\t%5.2f\n'%Ga_2[i])
            q=0
############################################### Q+1
data1 = pd.read_csv("O_288_q+1/ACF.dat",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2,nrows=399)
data1.columns = ['No','X','Y','Z','CH','MI','VO']

check=399

No = np.array(check)
X = np.array(check)
Y = np.array(check)
Z = np.array(check)
CH = np.array(check)
MI = np.array(check)
VO = np.array(check)

No = data1['No']
X = data1['X']
Y = data1['Y']
Z = data1['Z']
CH = data1['CH']
MI = data1['MI']
VO = data1['VO']

Con=27.21138386
#Eq_2A1=(Ev[1756]-Ev[1755])*Con
#Eq_2A2=(Ev[1757]-Ev[1755])*Con
chargea=sum(CH[0:159])/160
Ga_2=np.zeros_like(CH)
CHAGa=13-chargea
CHAGa98=13-(CH[98])
with open('Bader_sum.txt', 'a') as f:
 for i in range(399):
    Ga_2[i]=13-CH[i]
    if Ga_2[i] <= 1.9:
            q=i+1
            print(Ga_2[i])
            f.write('%5.4s\t'%q)
            f.write('+1\t%5.2f\n'%Ga_2[i])
            q=0
############################################### Q+2
data1 = pd.read_csv("O_288_q+2/ACF.dat",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2,nrows=399)
data1.columns = ['No','X','Y','Z','CH','MI','VO']

check=399

No = np.array(check)
X = np.array(check)
Y = np.array(check)
Z = np.array(check)
CH = np.array(check)
MI = np.array(check)
VO = np.array(check)

No = data1['No']
X = data1['X']
Y = data1['Y']
Z = data1['Z']
CH = data1['CH']
MI = data1['MI']
VO = data1['VO']

Con=27.21138386
#Eq_2A1=(Ev[1756]-Ev[1755])*Con
#Eq_2A2=(Ev[1757]-Ev[1755])*Con
chargea=sum(CH[0:79])/79
Ga_2=np.zeros_like(CH)
CHAGa=13-chargea
CHAGa98=13-(CH[98])
with open('Bader_sum.txt', 'a') as f:
 for i in range(399):
    Ga_2[i]=13-CH[i]
    if Ga_2[i] <= 1.9:
            q=i+1
            print(Ga_2[i])
            f.write('%5.4s\t'%q)
            f.write('-2\t%5.2f\n'%Ga_2[i])
            q=0
            
            
            
f.close()
