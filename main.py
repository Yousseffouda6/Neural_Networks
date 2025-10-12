from population import Population
import random

def main():
    # 1. Create initial population
    pop = Population(size=8)

    # 2. Assign fake fitness values (simulate user hovering)
    print("\n--- Assigning random fitness values ---")
    for f in pop.flowers:
        f.fitness = random.uniform(0, 10)  # 0–10 hover time for testing

    # 3. Show initial details
    pop.sort_by_fitness()
    pop.populationDetails()

    # 4. Generate next generation
    print("\n--- Generating next generation ---")
    pop.generate_next_generation = lambda: None  # skip pygame for now
    parents = pop.selection_roulette(num_parents=4)
    print("Selected parents (fitness):", [p for p in parents])

    # 5. Test crossover & mutation manually
    print("\n--- Testing crossover and mutation ---")
    p1, p2 = parents[0], parents[1]
    print("Parent1 DNA:", p1.dna)
    print("Parent2 DNA:", p2.dna)

    child = pop.crossover(p1, p2, crossover_rate=0.65)
    print("Child DNA (after crossover):", child.dna)

    pop.mutation(child, mutation_rate=0.05)
    print("Child DNA (after mutation):", child.dna)
    print("Child genes:", child.genes)


if __name__ == "__main__":
    main()
