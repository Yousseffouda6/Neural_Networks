import math, random, sys, time

from numpy import size

GENES_RANGES = [(10, 50), (0, 255), (0, 255), (0, 255), (0, 255), (0, 255), (0, 255), (0, 255), (0, 255), (0, 255),
                (0, 7)]


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
        for i, (low, high ) in enumerate(GENES_RANGES):
            dna.append(random.randint(low, high))
        return dna

    def getGenes(self):
        return {
            "center_size": self.dna[0],
            "center_color": (self.dna[1], self.dna[2], self.dna[3]),
            "petal_color": (self.dna[4], self.dna[5], self.dna[6]),
            "stem_color": (self.dna[7], self.dna[8], self.dna[9]),
            "num_petals": self.dna[10],
        }
    def __str__(self):
        """Human-readable string representation (like Java's toString)"""
        return f"Flower(fitness={self.fitness:.2f}, genes={self.genes})"
    def __repr__(self):
        return (
            f"Flower("
            f"fitness={self.fitness:.2f}, "
            f"center_size={self.genes['center_size']}, "
            f"center_color={self.genes['center_color']}, "
            f"petal_color={self.genes['petal_color']}, "
            f"stem_color={self.genes['stem_color']}, "
            f"num_petals={self.genes['num_petals']}) "
        )

    
    def initialize_population(size=8):
        return [Flower() for _ in range(size)]