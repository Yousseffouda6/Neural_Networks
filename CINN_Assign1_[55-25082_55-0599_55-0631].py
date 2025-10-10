import math, random, sys, time
import pygame
POP_SIZE = 8
GENES_RANGES = [(10, 50), (0, 255), (0, 255), (0, 255), (0, 255), (0, 255), (0, 255), (0, 255), (0, 255), (0,255), (0, 7)]
class Flower:
    def __init__(self, dna=None):
        self.fitness = 0
        if dna is None:
            self.dna = self.genRandomDNA()
        else:
            self.dna = dna
        self.genes = self.getGenes()


    def genRandomDNA(self):
        dna = []
        for i,(min, max) in enumerate(GENES_RANGES):
            dna.append(random.randint(min, max))
        return dna


    def getGenes(self):
            return {
                "center_size": self.dna[0],
                "center_color": (self.dna[1], self.dna[2], self.dna[3]),
                "petal_color": (self.dna[4], self.dna[5], self.dna[6]),
                "stem_color": (self.dna[7], self.dna[8], self.dna[9]),
                "num_petals": self.dna[10],
            }
def initialize_population():
        population = []
        for i in range(8):
            population.append(Flower())
        print(f"--- Initial Population Created ---")
        return population

def get_fitness(flower):
        return flower.fitness


def populationDetails(population):

    print(f"--- Population Details ---")
def sorted_pop_by_fitness(population):
        
    print(f"--- Sorted Population By Fitness ---")
        

def selection(population):
        
    return


def crossover(parent1, parent2):
     
    return


def mutation(flower):
     
    return