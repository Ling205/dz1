#экспериментальная ветка
import numpy as np
import matplotlib.pyplot as plt
plt.title('График')
plt.xlabel('Кол-во TOYOTA (X1)')
plt.ylabel('Кол-во AUDI (X2)')
plt.xlim(0,70)
plt.ylim(0,50)
plt.plot([0, 60], [40, 0]) #график 1
plt.plot([0, 10], [19, 19]) #график 2
plt.plot([20, 17], [0, 25]) #график 3
plt.plot([0, 7], [7, 0]) #график 4
plt.arrow(0, 0, 3, 5, width= 0.27)
plt.text(1.5, 1, 'Z(3,4)',fontsize=10)
plt.text(17.5, 2, 'X1 <= 17',fontsize=10)
plt.text(2, 19.5, 'X2 <= 19',fontsize=10)
plt.text(27, 5, '4X1 + 5X2 <= 141',fontsize=10)
plt.grid()
plt.show()
#номер группы: 8