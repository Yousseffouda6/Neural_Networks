from flower import Flower, GENES_RANGES
import random

class Population:
    def __init__(self, size):
        self.size = size
        self.flowers = [Flower() for _ in range(size)]
        print(f"--- Population Created ---")


    def get_best(self):
        return max(self.flowers, key=lambda f: f.fitness) #key to compare flowers by: fitness

    def sort_by_fitness(self):
        self.flowers.sort(key=lambda f: f.fitness, reverse=True) #key to sort by: fitness, reverse = True => Descending

    def populationDetails(self):
        print(f"--- Population Details ---")
        for i, flower in enumerate(self.flowers):
            print(f"Flower {i + 1}: {flower.genes} (fitness={flower.fitness:.2f})")


    def selection_roulette(self, num_parents=4):
        total_fitness = sum(flower.fitness for flower in self.flowers)
        if total_fitness == 0:
            return random.sample(self.flowers, num_parents) #first time => select random num_parents flowers
        selected_parents = []
        print("Total Fitness is",total_fitness)
        for _ in range(num_parents):
            # Spin the wheel — generate a random value between 0 and total fitness
            random_spin = random.uniform(0, total_fitness)
            print("Random Spin: ", random_spin)
            cumulative_probability = 0
            for flower in self.flowers:
                cumulative_probability += flower.fitness
                # When the spin value falls into this flower's range → select it
                if cumulative_probability >= random_spin:
                    selected_parents.append(flower)
                    print("Cumulative is", cumulative_probability,"Adding flower", flower)
                    break
        return selected_parents


    def crossover(self, parent1, parent2, crossover_rate):
        """Combine DNA of two parents"""
        #Perform crossover if the random number falls within 65% of the range (0 → 0.65).
        if random.random() > crossover_rate:
            return Flower(dna=parent1.dna.copy())

        point = random.randint(1, len(parent1.dna) - 1)
        child_dna = parent1.dna[:point] + parent2.dna[point:]
        return Flower(dna=child_dna)

    def mutation(self, flower, mutation_rate=0.1):
        for i, (low, high) in enumerate(GENES_RANGES):
            if random.random() < mutation_rate:
                flower.dna[i] = random.randint(low, high)
        flower.genes = flower.getGenes()
