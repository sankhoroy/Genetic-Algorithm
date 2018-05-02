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
from chromosome import chromosome



class gene:
    def __init__(self,x):
        self.populations = []
        self.new_populations = []
        global population_size
        for i in range(population_size):
            new_population = population(random.sample(x,len(x)))
            self.populations.append(new_population)
        self.generation = chromosome(self.populations)
        
        current_best = self.generation._normalizefitness()
        
        if current_best._totaldistance() < 9223372036854775807:
            self.overall_best = copy.deepcopy(current_best)
            
        self.generation._print_generation_result()
        self.driver()
    def driver(self):
        global iteration
        for i in range(iteration):
            self.evolution()
            self.generation = chromosome(self.populations)
            
            current_best = self.generation._normalizefitness()
            
            if current_best._totaldistance() < self.overall_best._totaldistance():
                self.overall_best = copy.deepcopy(current_best)
            
            print('generation no : ',i+1)
            self.generation._print_generation_result()
            
    def evolution(self):
        global mutation_rate
        global population_size
        self.new_populations  = []
        for i in range(population_size):
            new_population = self.generation.crossover()
            if(np.random.random() < mutation_rate ):
                new_population = self.generation.mutation(new_population)
#             new_population._print_population()
            self.new_populations.append(new_population)
        self.populations = copy.deepcopy(self.new_populations)
        self.new_populations = []