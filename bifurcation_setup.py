import numpy as np
import math  as mt
import matplotlib.pyplot as plt
from manager.sim_manager import *
from utils.plot_data import create_figure

@jit(nopython=True)
def chen_system(x,var):
	y1,y2,y3 = x
	a = var   
	b = 3  
	c = 28
	Dqy1 = a*(y2-y1)
	Dqy2 = (c-a)*y1 - y1*y3 + c*y2
	Dqy3 = y1*y2 - b*y3
	return np.array([Dqy1,Dqy2,Dqy3])
#-------------------------------------------------------
vo_algorithm = v3_bifurcation
h     = 0.005 # step size
t_sim = 30.0  # simulation time
Stime = np.arange(0, t_sim + h, h)        #Time span array
q     = 0.9 + 0.1*np.sin(mt.pi*Stime)     #Variable order
y0    = np.array([ [1.0], [0.0], [1.0] ]) #Initial Conditions
#-------------------------------------------------------
L_inf = 40
L_sup = 60
delta = 0.1
#-------------------------------------------------------
if __name__ == '__main__':
    X = bifurcation_process(v1_bifurcation,chen_system,q,y0,h,delta,L_inf,L_sup)
    #-------------------------------------------------------
    svar = X[0]
    xmax = X[1]

    path='results'
    np.savetxt(f'{path}/svar_chen_bif_a.txt',svar,delimiter=',')
    np.savetxt(f'{path}/xmax_chen_bif_y1.txt',xmax,delimiter=',')

    create_figure(data=(svar,xmax), axis_names=('a','x1_max'),figure_name='chen_bif_v3_ax1',path=path)