from flower import Flower, GENES_RANGES
import random

class Population:
    def __init__(self, size=8):
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


    def selection(self, num_parents=4):
        """Select the top num_parents flowers with highest fitness."""
        if len(self.flowers) == 0:
            return []

        # Sort flowers by fitness descending
        sorted_flowers = sorted(self.flowers, key=lambda f: f.fitness, reverse=True)
        print("Population sorted by fitness:")
        for f in sorted_flowers:
            print(f)
        selected = sorted_flowers[:num_parents]

        print(f"--- Selected Top {num_parents} Parents by Fitness ---")
        for f in selected:
            print(f)
        return selected



    def crossover(self, parent1, parent2, crossover_rate=0.65):
        """Combine DNA of two parents to produce two children with detailed debugging."""
        print("\n--- Crossover Info ---")
        print(f"Parent 1 DNA: {parent1.dna}")
        print(f"Parent 2 DNA: {parent2.dna}")

        random_value = random.random()
        print(f"Generated random value: {random_value:.4f} (Crossover rate: {crossover_rate})")

        # No crossover → clone both parents
        if random_value > crossover_rate:
            print("Result: No crossover occurred — returning clones of both parents.")
            return Flower(dna=parent1.dna.copy()), Flower(dna=parent2.dna.copy())

        # Perform crossover
        point = random.randint(1, len(parent1.dna) - 1)
        print(f"Crossover point selected at index: {point}")

        child1_dna = parent1.dna[:point] + parent2.dna[point:]
        child2_dna = parent2.dna[:point] + parent1.dna[point:]

        print(f"Child 1 DNA (P1[:{point}] + P2[{point}:]): {child1_dna}")
        print(f"Child 2 DNA (P2[:{point}] + P1[{point}:]): {child2_dna}")

        # Display gene breakdown for clarity
        child1_genes = Flower(dna=child1_dna).genes
        child2_genes = Flower(dna=child2_dna).genes

        print("\n--- Resulting Children Genes ---")
        print(f"Child 1 genes: {child1_genes}")
        print(f"Child 2 genes: {child2_genes}")
        print("---------------------------------\n")

        return Flower(dna=child1_dna), Flower(dna=child2_dna)



    def mutation(self, flower, mutation_rate=0.05):
        """Mutate flower DNA with detailed debugging output."""
        print("\n--- Mutation Info ---")
        print(f"Original DNA: {flower.dna}")
        print(f"Mutation rate: {mutation_rate}")

        for i, (low, high) in enumerate(GENES_RANGES):
            random_value = random.random()
            print(f"Gene {i}: current value={flower.dna[i]}, random={random_value:.4f}, range=({low},{high})")

            if random_value < mutation_rate:
                old_value = flower.dna[i]
                new_value = random.randint(low, high)
                flower.dna[i] = new_value
                print(f" → Mutated gene {i} from {old_value} to {new_value}")
            else:
                print(f" → No mutation for gene {i}")

        flower.genes = flower.getGenes()
        print("Updated genes:", flower.genes)
        print("--- Mutation Complete ---\n")


    def evolve_population(self):
        parents = self.selection()
        new_flowers = []
        i = 0
        while len(new_flowers) < self.size:
            p1, p2 = parents[0], parents[1]
            p3, p4 = parents[2], parents[3]
            child1, child2 = self.crossover(p1, p2)
            child3, child4 = self.crossover(p3, p4)
            self.mutation(child1)
            self.mutation(child2)
            self.mutation(child3)
            self.mutation(child4)
            new_flowers.append(child1)
            new_flowers.append(child2)
            new_flowers.append(child3)
            new_flowers.append(child4)
            if (i == 0): print(f"--- Generated the first 4 children ---".center(160))
            else: print(f"--- Generated the second 4 children ---".center(160))
            print()
            print()
            i += 1


        self.flowers = new_flowers
        print("--- Updated Population ---")
        for i, flower in enumerate(self.flowers):
            print(f"Flower {i + 1}: {flower.genes} (fitness={flower.fitness:.2f})")


