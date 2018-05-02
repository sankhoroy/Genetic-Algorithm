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
from population import population



class chromosome:
    def __init__(self,x):
#         self.best = None
        self.populations = x
        self.fitness = []
        self.indexes = []
        self.total_fitness = 0
            
    def _normalizefitness(self):
        self.total_fitness = 0
#         print('population length : ',len(self.populations))
        for i in range(len(self.populations)):
            self.fitness.append(self.populations[i]._fitness())
            self.total_fitness += self.fitness[i]
#             self.populations[i]._print_population()
#             print(self.fitness[i])
        self.fitness = [x/self.total_fitness for x  in self.fitness]
#         [print(self.fitness[i]) for i in range(len(self.fitness))]
#         print('best population',np.argmax(self.fitness))
        self.best = self.populations[np.argmax(self.fitness)]
        return self.best
        
    def _plot_chromosome_tour(self):
        for i in range(len(self.populations)):
            self.populations[i]._plottour()
              
    def _print_generation_result(self):
        print('average fitness of generation :',np.average(self.fitness))
#         print('best population till now : ')
#         p1 = population(self.best.values)
#         p1._print_population()
#         self._plot_chromosome_tour()
    def selection(self):
        global population_size
        self.indexes = np.random.choice(population_size ,2, p = self.fitness)
       
    def crossover(self):
        global crossover_rate
        
        if np.random.random() > crossover_rate:
            replica = copy.deepcopy(self.populations[np.argmax(self.fitness)])
            return replica
        
        self.selection()
        f_index,m_index = self.indexes
#         print('selected indexes -zero based: ',f_index,m_index)
        f = self.populations[f_index].values
        m = self.populations[m_index].values
        
        slice_till = len(self.populations[f_index].values)//2 
#         randint(0, len(self.populations[f_index].values)-1)  # 
#         print('slice till -',slice_till)
        o = []
        o.append(f[0:slice_till])
        o = o[0]
        for i in range(len(m)):
            not_in_offspring = True
            for j in range(len(o)):
#                 print('m = ',i,m[i])
#                 print('o = ',j,o[j])
                if m[i] == o[j]:
                    not_in_offspring = False
                    break
    
            if not_in_offspring == True:
#                 print('added')
                o.append(m[i])
            else:
                pass
#                 print('not added')
#         print('resultant population - ',o)
#         self.mutation(o)
        p = population(o)
#         p._print_population()
        return p
    def mutation(self,x):
#         print(len(x.values))
        i = randint(0, len(x.values)-1)
        j = randint(0, len(x.values)-1)
        x.values[i],x.values[j] = x.values[j],x.values[i]
        return x