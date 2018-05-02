import matplotlib.pyplot as plt

from config import *
from population import population
from chromosome import chromosome
from gene import gene

circle = [(39, 0),(51, 58), (30, 58), (10, 25), (69, 24), (20, 7), (66, 44),(59, 7),(14, 46)]
random_points = [(73, -94), (25, 73),(-98, 22),(-50, -43),(16, 46),(16, 13),(-27, -71),(-13, -23),(58, -81),(-75, 43),(95, -86),(-43, -70),(44, 45), (-19, -94),(-37, 45),(-59, 12),(33, -26),(-58, 85),(92, -97)]
random_points_2 = [(49, 19),(87, -69),(29, 45),(-50, 56),(-66, -33),(22, -33),(27, -72),(82, 61),(97, 33),(58, 18),(-9, -19),(50, 58),(-38, 67),(98, 3)]

if __name__ == '__main__':
# input is x PUT YOUR INPUT HERE
    x = circle
    #plotting initial 
    starting_population = population(x)
    starting_chromosome = chromosome([starting_population])
    starting_distance = starting_population._totaldistance()
    starting_chromosome._plot_chromosome_tour()
    
    #Applying Genetic Algorithm
    g = gene(x)
    
    #plotting best
    final_best_population = g.overall_best
    final_best_chromosome = chromosome([final_best_population])
    final_best_distance = final_best_population._totaldistance()
    final_best_chromosome._plot_chromosome_tour()
    print('================== Results of Optimization ============================')
    print('Initial Distance : ', starting_distance)
    print('Optimized final Distance :', final_best_distance)
    print(((starting_distance - final_best_distance)*100/starting_distance),'% distance reduced')
    plt.show()