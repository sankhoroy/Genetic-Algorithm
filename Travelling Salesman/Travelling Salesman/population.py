import numpy as np
import random
import matplotlib.pyplot as plt
import copy
from pylab import *
from random import randint
import random
import copy
import numpy as np


from config import *



class population:
    def __init__(self,x):
        self.values = x
        
    def dist(self,p1,p2):
        return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    def _totaldistance(self):
#         print('inside total distance:',self.values)
        total = 0
        for i in range(len(self.values)-1):
            p1,p2 = self.values[i],self.values[i+1]
#             print(p1,p2)
            total += self.dist(p1,p2)
#         print(total)
        return total
    
    def _fitness(self):
#         print('inside _fitness function:',self.values)
        return 1/(self._totaldistance() + 1)
    def _print_population(self):
#         print('population : ',self.values)
        print('dist : ',self._totaldistance())
    def _plottour(self):
        x = []
        y  = []
        for  i in range(len(self.values)):
            x.append(self.values[i][0])
            y.append(self.values[i][1])
        plt.plot(x,y)