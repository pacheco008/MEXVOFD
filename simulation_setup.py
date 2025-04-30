import numpy as np
import math  as mt
from manager.sim_manager import *
from utils.plot_data import create_figure
#-------------------------------------------------------
@jit(nopython=True)
def chen_system(y,var=None):
	y1,y2,y3 = y
	a = 40
	b = 3
	c = 28
	Dqy1 = a*(y2-y1)
	Dqy2 = (c-a)*y1 - y1*y3 + c*y2
	Dqy3 = y1*y2 - b*y3
	return np.array([Dqy1,Dqy2,Dqy3])
#-------------------------------------------------------
vo_algorithm = v3_alg
h     = 0.005 # step size
t_sim = 30.0  # simulation time
y0    = np.array([ [1.0], [0.0], [1.0] ]) #Initial Conditions
Stime = np.arange(0, t_sim + h, h)        #Time span array
q     = 0.9 + 0.1*np.sin(mt.pi*Stime)     #Variable order
#-------------------------------------------------------

y   = vo_algorithm(chen_system,q,y0,h)
y1  = y[0,:]
y2  = y[1,:]
y3  = y[2,:]

path='results'
np.savetxt(f'{path}/v3_chen_y1.txt',y1,delimiter=',')
np.savetxt(f'{path}/v3_chen_y2.txt',y2,delimiter=',')
np.savetxt(f'{path}/v3_chen_y3.txt',y3,delimiter=',')

create_figure(data=(y1,y3), axis_names=('y1','y3'),figure_name='chen_y1y3_v3_type',path=path)
