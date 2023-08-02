
import numpy as np
#import matplotlib.mlab as mlab
#import matplotlib.tri as tri
import pandas as pd

########################################################## Q-2

data1 = pd.read_csv("O_288_q-2/GaO-k1-1.pdos",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2)
data1.columns = ['MO','Ev','Oc','s','p','d','f']

check=len(data1)

MO = np.array(check)
Ev = np.array(check)
Oc = np.array(check)
s = np.array(check)
p = np.array(check)
d = np.array(check)
f = np.array(check)

MO = data1['MO']
Ev = data1['Ev']
Oc = data1['Oc']
s = data1['s']
p = data1['p']
d = data1['d']
f = data1['f']

Con=27.21138386
Eq_2A1=(Ev[1756]-Ev[1755])*Con
Eq_2A2=(Ev[1757]-Ev[1755])*Con


########################################################## Q-1 Alpha
data1 = pd.read_csv("O_288_q-1/GaO-ALPHA_k1-1.pdos",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2)
data1.columns = ['MO','Ev','Oc','s','p','d','f']

check=len(data1)

MO = np.array(check)
Ev = np.array(check)
Oc = np.array(check)
s = np.array(check)
p = np.array(check)
d = np.array(check)
f = np.array(check)

MO = data1['MO']
Ev = data1['Ev']
Oc = data1['Oc']
s = data1['s']
p = data1['p']
d = data1['d']
f = data1['f']

Con=27.21138386
Eq_1A1=(Ev[1756]-Ev[1755])*Con
Eq_1A2=(Ev[1757]-Ev[1755])*Con

########################################################## Q-1 Beta
data1 = pd.read_csv("O_288_q-1/GaO-BETA_k1-1.pdos",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2)
data1.columns = ['MO','Ev','Oc','s','p','d','f']

check=len(data1)

MO = np.array(check)
Ev = np.array(check)
Oc = np.array(check)
s = np.array(check)
p = np.array(check)
d = np.array(check)
f = np.array(check)

MO = data1['MO']
Ev = data1['Ev']
Oc = data1['Oc']
s = data1['s']
p = data1['p']
d = data1['d']
f = data1['f']

Con=27.21138386
Eq_1B1=(Ev[1756]-Ev[1755])*Con
Eq_1B2=(Ev[1757]-Ev[1755])*Con



########################################################## Q-0

data1 = pd.read_csv("O_288_q0/GaO-k1-1.pdos",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2)
data1.columns = ['MO','Ev','Oc','s','p','d','f']

check=len(data1)

MO = np.array(check)
Ev = np.array(check)
Oc = np.array(check)
s = np.array(check)
p = np.array(check)
d = np.array(check)
f = np.array(check)

MO = data1['MO']
Ev = data1['Ev']
Oc = data1['Oc']
s = data1['s']
p = data1['p']
d = data1['d']
f = data1['f']

Con=27.21138386
Eq_0A1=(Ev[1756]-Ev[1755])*Con
Eq_0A2=(Ev[1757]-Ev[1755])*Con


########################################################## Q+1 Alpha
data1 = pd.read_csv("O_288_q+1/GaO-ALPHA_k1-1.pdos",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2)
data1.columns = ['MO','Ev','Oc','s','p','d','f']

check=len(data1)

MO = np.array(check)
Ev = np.array(check)
Oc = np.array(check)
s = np.array(check)
p = np.array(check)
d = np.array(check)
f = np.array(check)

MO = data1['MO']
Ev = data1['Ev']
Oc = data1['Oc']
s = data1['s']
p = data1['p']
d = data1['d']
f = data1['f']

Con=27.21138386
Eqp1A1=(Ev[1756]-Ev[1755])*Con
Eqp1A2=(Ev[1757]-Ev[1755])*Con

########################################################## Q+1 Beta
data1 = pd.read_csv("O_288_q+1/GaO-BETA_k1-1.pdos",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2)
data1.columns = ['MO','Ev','Oc','s','p','d','f']

check=len(data1)

MO = np.array(check)
Ev = np.array(check)
Oc = np.array(check)
s = np.array(check)
p = np.array(check)
d = np.array(check)
f = np.array(check)

MO = data1['MO']
Ev = data1['Ev']
Oc = data1['Oc']
s = data1['s']
p = data1['p']
d = data1['d']
f = data1['f']

Con=27.21138386
Eqp1B1=(Ev[1756]-Ev[1755])*Con
Eqp1B2=(Ev[1757]-Ev[1755])*Con


########################################################## Q+2

data1 = pd.read_csv("O_288_q+2/GaO-k1-1.pdos",delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=2)
data1.columns = ['MO','Ev','Oc','s','p','d','f']

check=len(data1)

MO = np.array(check)
Ev = np.array(check)
Oc = np.array(check)
s = np.array(check)
p = np.array(check)
d = np.array(check)
f = np.array(check)

MO = data1['MO']
Ev = data1['Ev']
Oc = data1['Oc']
s = data1['s']
p = data1['p']
d = data1['d']
f = data1['f']

Con=27.21138386
Eqp2A1=(Ev[1756]-Ev[1755])*Con
Eqp2A2=(Ev[1757]-Ev[1755])*Con


########################################################## Q+2


with open('SK_Energy.txt', 'w') as f:
    f.write('-2A\t%5.2f\n'%Eq_2A1)
    f.write('-2A\t%5.2f\n'%Eq_2A2)
    f.write('-1A\t%5.2f\n'%Eq_1A1)
    f.write('-1A\t%5.2f\n'%Eq_1A2)
    f.write('-1B\t%5.2f\n'%Eq_1B1)
    f.write('-1B\t%5.2f\n'%Eq_1B2)                        
    f.write('+0A\t%5.2f\n'%Eq_0A1)
    f.write('+0A\t%5.2f\n'%Eq_0A2)   
    f.write('+1A\t%5.2f\n'%Eqp1A1)
    f.write('+1A\t%5.2f\n'%Eqp1A2)
    f.write('+2A\t%5.2f\n'%Eqp1B1)
    f.write('+2A\t%5.2f\n'%Eqp1B2)      
f.close()

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
#x = np.arange(0, 1, 0.1)
VBM = 0
CBM = 4.2
BD1 = 1
BD2 = 10
plt.xticks([])
#plt.yticks([])
ax.axhline(VBM, xmin=0, xmax=1, color='r', label='')
ax.axhline(CBM, xmin=0, xmax=1, color='b', label='')



#Ov1
#plt.axhline(-0.5, xmin = 0.05, xmax = 0.5, color ='k', linestyle='-')
########q-2

#plt.text(1.4,1.3,r'$\alpha$,$\beta$',horizontalalignment='right')
plt.text(1.4,Eq_2A1+0.2,'%5.2f eV'%Eq_2A1,horizontalalignment='right')
plt.axhline(Eq_2A1, xmin = 0.02, xmax = 0.14, color ='k', linestyle='-')
ax.scatter(0.6, Eq_2A1, s=80, facecolors='k', edgecolors='k')
ax.scatter(1.,Eq_2A1, s=80, facecolors='k', edgecolors='k')

plt.text(1.4,Eq_2A2+0.2,'%5.2f eV'%Eq_2A2,horizontalalignment='right')
plt.axhline(Eq_2A2, xmin = 0.02, xmax = 0.14, color ='k', linestyle='-')
ax.scatter(0.6, Eq_2A2, s=80, facecolors='k', edgecolors='k')
ax.scatter(1.,Eq_2A2, s=80, facecolors='k', edgecolors='k')



########q-1
plt.text(3.4,Eq_1A1+0.2,'%5.2f eV'%Eq_1A1,horizontalalignment='right')
#plt.text(2.8,2.5,r'$\alpha$',horizontalalignment='right')
plt.axhline(Eq_1A1, xmin = 0.22, xmax = 0.34, color ='k', linestyle='-')
ax.scatter(2.6, Eq_1A1, s=80, facecolors='k', edgecolors='k')
ax.scatter(3, Eq_1A1, s=80, facecolors='k', edgecolors='k')

plt.text(3.4,Eq_1A2+0.2,'%5.2f eV'%Eq_1A2,horizontalalignment='right')
#plt.text(2.8,4.5,r'$\beta$',horizontalalignment='right')
plt.axhline(Eq_1A2, xmin = 0.22, xmax = 0.34, color ='k', linestyle='--')
ax.scatter(2.6, Eq_1A2, s=80, facecolors='k', edgecolors='k')

plt.text(3.4,Eq_1B2+0.4,'%5.2f eV'%Eq_1B2,horizontalalignment='right')
#plt.text(2.8,4.5,r'$\beta$',horizontalalignment='right')
plt.axhline(Eq_1B2, xmin = 0.22, xmax = 0.34, color ='k', linestyle='--')
#ax.scatter(2.5, Eq_1B2, s=80, facecolors='k', edgecolors='k')

########q0

plt.text(5.6,Eq_0A1+0.2,'%5.2f eV'%Eq_0A1,horizontalalignment='right')
#plt.text(4.5,Eq_0A1,r'$\alpha$,$\beta$',horizontalalignment='right')
plt.axhline(Eq_0A1, xmin = 0.44, xmax = 0.56, color ='k', linestyle='-')
ax.scatter(5.2, Eq_0A1, s=80, facecolors='k', edgecolors='k')
ax.scatter(4.8, Eq_0A1, s=80, facecolors='k', edgecolors='k')


plt.text(5.6,Eq_0A2+0.2,'%5.2f eV'%Eq_0A2,horizontalalignment='right')
#plt.text(4.5,Eq_0A1,r'$\alpha$,$\beta$',horizontalalignment='right')
plt.axhline(Eq_0A2, xmin = 0.44, xmax = 0.56, color ='k', linestyle='--')
#ax.scatter(4., Eq_0A2, s=80, facecolors='k', edgecolors='k')
#ax.scatter(4.4, Eq_0A2, s=80, facecolors='k', edgecolors='k')

########q-1

plt.text(7.6,Eqp1A1+0.2,'%5.2f eV'%Eqp1A1,horizontalalignment='right')
#plt.text(2.8,2.5,r'$\alpha$',horizontalalignment='right')
plt.axhline(Eqp1A1, xmin = 0.64, xmax = 0.76, color ='k', linestyle='-')
ax.scatter(6.8, Eqp1A1, s=80, facecolors='k', edgecolors='k')


plt.text(7.6,Eqp1A2+0.2,'%5.2f eV'%Eqp1A2,horizontalalignment='right')
#plt.text(2.8,4.5,r'$\beta$',horizontalalignment='right')
plt.axhline(Eqp1A2, xmin = 0.64, xmax = 0.76, color ='k', linestyle='--')

########q-2
plt.text(9.4,Eqp2A1+0.2,'%5.2f eV'%Eqp2A1,horizontalalignment='right')
#plt.text(2.8,4.5,r'$\beta$',horizontalalignment='right')
plt.axhline(Eqp2A1, xmin = 0.82, xmax = 0.94, color ='k', linestyle='--')



plt.text(6.7,-1.5,'Valence band states',horizontalalignment='right')
plt.text(6.7,5.5,'Conduction band states',horizontalalignment='right')
ax.set_xlim([0, 10])
plt.text(0.8,-0.3,'q=-2',horizontalalignment='center')
plt.text(2.8,-0.3,'q=-1',horizontalalignment='center')
plt.text(5,-0.3,'q=0',horizontalalignment='center')
plt.text(7,-0.3,'q=+1',horizontalalignment='center')
plt.text(9,-0.3,'q=+2',horizontalalignment='center')

ax.annotate('', xy=(0, 0), xytext=(0, 4.2),
            arrowprops={'arrowstyle': '-'})

plt.text(-0.5,1.5,'Energy (eV)',rotation=90,horizontalalignment='right')

#plt.show()
plt.box(False)
plt.savefig('KS_Ep1.jpeg', dpi=400)


