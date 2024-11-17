import matplotlib.pyplot as plt
import numpy as np
x=[0.1,0.2,0.3,0.33,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y=[0.43,0.56,0.71,0.89,0.82,0.76,0.62,0.67,0.53,0.42,0.48]
plt.title('Efficiency for 3 stations')
plt.xlabel('Probability')
plt.ylabel('Efficiency')
plt.plot(x,y)
plt.grid(True)
print(len(y))