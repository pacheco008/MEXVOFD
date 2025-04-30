import numpy as np
import matplotlib.pyplot as plt

#Execute inside MEXVOFD/utils

svar = np.loadtxt("../results/svar_chen_bif_a.txt", delimiter=',')
xmax = np.loadtxt("../results/xmax_chen_bif_y1.txt", delimiter=',')


plt.figure(figsize=(5,4))
plt.scatter(svar,xmax, marker='.', s=1, color = 'black',linewidth=0.1)
plt.xlabel(r'$a$', fontsize=20)
plt.ylabel(r'$x_{1_{max}}$',fontsize=20)
plt.tight_layout()
plt.xticks(np.arange(40, 60 + 5, 5)) 
plt.xlim([40, 60])
plt.yticks(np.arange(-10, 25 + 5, 5)) 
plt.ylim([-10, 25])
plt.show(block=False)
input('Hit Enter To Close')
plt.close()
