import numpy as np
import matplotlib.pyplot as plt

nx,ny=1024,3072

tx=[]

tx1,tx2,tx3,tx4=0.406,0.308,0.227,0.236

ty=[]

tx.append(tx1),tx.append(tx2)
tx.append(tx3),tx.append(tx4)

ty.append(1024),ty.append(512)
ty.append(256),ty.append(128)

t1px,t1py=16,64
t2px,t2py=8,64
t3px,t3py=8,32
t4px,t4py=8,16
t5px,t5py=4,16

print('===========')
print(np.sqrt((t1px*t1py)))
print(np.sqrt(t2px*t2py))
print(np.sqrt(t3px*t3py))
print(np.sqrt(t4px*t4py))
print(np.sqrt(t5px*t5py))
print('===========')
print(np.sqrt((nx/t1px)*(ny/t1py)))
print(np.sqrt((nx/t2px)*(ny/t2py)))
print(np.sqrt((nx/t3px)*(ny/t3py)))
print(np.sqrt((nx/t4px)*(ny/t4py)))
print('===========')

plt.scatter(ty,tx)
plt.ylabel(r'$\mu$'+'[s]')
plt.yscale('log')
plt.xlabel('proc')
plt.xscale('log')
plt.show()
