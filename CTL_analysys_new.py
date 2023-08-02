import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def Defect(Ed, Eb, u, q, Ef):
    return Ed-Eb+u+q*(Ef+4.2/2)+0.07298*q**2


data1 = pd.read_csv('CTL_Energy.txt',dtype=str,delim_whitespace=True, header=None, encoding='ISO-8859-1', engine='python',skiprows=0)
E0=data1.to_numpy()
Con=27.21138386
En=np.ones(5,dtype=float)

for i in range(5) :
    En[i]=np.multiply(float(E0[i]),float(Con))
    print('%.5f'%En[i])


plt.xlim(0, 4.2)
#plt.ylim(-15, 10)
x=np.arange(-5, 4.2, 0.01)

Eb=-426929.1728

y0=Defect(En[2], Eb, -433.99,0, x)
y1=Defect(En[3],Eb, -433.99,1, x)
y2=Defect(En[4], Eb, -433.99,2, x)
y_1=Defect(En[1], Eb, -433.99,-1, x)
y_2=Defect(En[0], Eb, -433.99,-2, x)

#CTLCal
y00=Defect(En[2], Eb, -433.99,0, 0)
y10=Defect(En[3],Eb, -433.99,1, 0)
y20=Defect(En[4], Eb, -433.99,2, 0)
y_10=Defect(En[1], Eb, -433.99,-1, 0)
y_20=Defect(En[0], Eb, -433.99,-2, 0)



q10=(y10-y00)/1
q20=(y20-y00)/2
q_10=(y_10-y00)/-1
q_20=(y_20-y00)/-2

CTL10=(q10+4.2)
CTL20=(q20+4.2)
CTL_10=(q_10+4.2)
CTL_20=(q_20+4.2)

plt.plot(x,y0, label="q=0", )
plt.plot(x,y1, label="q=+1", )
plt.plot(x,y2, label="q=+2", )
plt.plot(x,y_1, label="q=-1", )
plt.plot(x,y_2, label="q=-2", )


with open('CTL_sum.txt', 'w') as f:
      f.write('CTL20\t%5.2f\t'%CTL20)
      f.write('\nCTL10\t%5.2f\t'%CTL10)
      f.write('\nCTL_10\t%5.2f\t'%CTL_10)   
      f.write('\nCTL_20\t%5.2f\t'%CTL_20)
f.close()



plt.legend()
plt.savefig('Charge.png', dpi=150)




