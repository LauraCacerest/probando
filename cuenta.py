import numpy as np
import matplotlib.pyplot as plt

l=np.linspace(0,2*(np.pi))
c=[]

for i in l:
	c.append(np.cos(i))
	
plt.plot(l,c)
plt.savefig("Cosgit.png")

