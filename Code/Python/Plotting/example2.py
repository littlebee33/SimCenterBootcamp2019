import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

#plt.show()

plt.savefig('ex2.png')
plt.savefig('ex2.jpg')
plt.savefig('ex2.pdf')
plt.savefig('ex2b.png', dpi=300)

