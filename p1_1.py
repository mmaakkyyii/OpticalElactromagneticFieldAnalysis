import scipy as sp
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from scipy import pi,sin,cos,tan,arcsin,linspace
from matplotlib.pyplot import plot,show,xlabel,ylabel,title,legend,grid,axis,tight_layout


n1= 1
n2= 1.5

t1Deg = linspace(0,90,91)
print(t1Deg)
t1=t1Deg/180*pi
t2=arcsin((n1/n2)*sin(t1))
tp=2*n1*cos(t1)/(n2*cos(t1)+n1*cos(t2))
rp=(n2*cos(t1)-n1*cos(t2))/(n2*cos(t1)+n1*cos(t2))
ts=2*n1*cos(t1)/(n1*cos(t1)+n2*cos(t2))
rs=(n1*cos(t1)-n2*cos(t2))/(n1*cos(t1)+n2*cos(t2))

plt.figure(figsize=(8,6))
plot(t1Deg,rp, label=r"$r_{12}^{\rm{p}}$",linewidth=3.0,color='black',linestyle='dashed')
plot(t1Deg,tp, label=r"$t_{12}^{\rm{p}}$",linewidth=3.0,color='black')
plot(t1Deg,rs, label=r"$r_{12}^{\rm{s}}$",linewidth=3.0,color='gray',linestyle='dashed')
plot(t1Deg,ts, label=r"$t_{12}^{\rm{s}}$",linewidth=3.0,color='gray')

xlabel(r"$\theta_1$ (deg.)", fontsize=20)
ylabel(r"r, t", fontsize=20)
title("Reflection and Transmission Coeffieient",fontsize=18)
grid(True)
axis([0.0,90,-1,1])
legend(fontsize=20,loc='lower right')
plt.tick_params(labelsize=20)
tight_layout()

show()