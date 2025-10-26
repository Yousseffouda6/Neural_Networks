# Flower Evolution using Genetic Algorithm
## 📘 Project Overview
This project implements a **Genetic Algorithm (GA)** to simulate the evolution of a population of flowers.  
Each flower’s appearance is determined by its **DNA sequence**, and evolution is driven by **user interaction**—the longer the user hovers over a flower, the fitter it becomes.

---

## 🎯 Objectives
- Implement the fundamental operations of a genetic algorithm: **selection**, **crossover**, and **mutation**.  
- Simulate evolution based on user-defined fitness.  
- Visualize how flower traits evolve across generations.

---

## 🧬 DNA Structure
Each flower is represented by an **11-gene DNA sequence**:

| Trait | Number of Genes | Range / Type |
|-------|------------------|--------------|
| Center Size | 1 | Integer |
| Center Color (R, G, B) | 3 | 0–255 each |
| Petal Color (R, G, B) | 3 | 0–255 each |
| Stem Color (R, G, B) | 3 | 0–255 each |
| Number of Petals | 1 | 0–7 |

---

## ⚙️ Implementation Steps

1. **Initialize Population**  
   Create 8 flowers with random DNA sequences.

2. **Selection**  
   Choose flowers for reproduction based on user-assigned fitness.  
   Fitter flowers have a higher chance of selection.

3. **Crossover**  
   Combine genetic information from two parents to produce a child.  
   Crossover occurs with a probability of **65%**.

4. **Mutation**  
   Randomly alter genes to introduce variation.  
   Mutation rate: **5% (0.05)**.

5. **Evolution Process**  
   Evaluate → Select → Crossover → Mutate → Replace → Repeat.

6. **User Interaction**  
   Hover duration over each flower determines its fitness.

7. **Output**  
   For every generation, the program prints:
   - Initial population and characteristics  
   - Sorted population by fitness  
   - Selected parents  
   - Crossover results  
   - Mutation results  
   - Updated population  

---

## 🪷 Expected Output
- Visible evolution of flower traits over multiple generations.  
- Console output displaying intermediate steps.  
- Fitter flowers (those hovered over longer) dominate future generations.


© 2025 – German University in Cairo, Faculty of Media Engineering and Technology
