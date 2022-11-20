import random



# Constants
N = 5   #board size
P = 8   #population size
I = 12  #initial position
SEED = list(range(0, (N**2)))

# Class chromosomeso
class Chromosomes():

    # Create Random chromosomes
    def __init__(self):
        tmp = SEED.copy()
        random.shuffle(tmp)
        self.chromo = move_initial(tmp)
        self.set_valids()

    # Clone chromossome
    def clone(self):
        new_org = Chromosomes()
        new_org.chromo = self.chromo.copy()
        new_org.valids = self.valids
        return new_org

    # count valid position
    def set_valids(self):
        count = 0
        for i in range(0, (N**2)-1):
            if(is_valid(self.chromo[i], self.chromo[i+1])):
                count += 1
        self.valids = count

    # Correct chromossome after reproduction
    def correct(self):
        count = [0]*(N**2)
        for position in self.chromo:
            count[position] += 1
        i = 0
        for c in count:
            if c == 2:
                self.chromo.remove(i)
            if c == 0:
                self.chromo.append(i)
            i += 1
        self.chromo = move_initial(self.chromo)

        

    def __str__(self):
        return f'Genes: {self.chromo} | Valids: {self.valids}'
        


# Initialization
def initialize():

    population = []

    for i in range (0, P):
        tmp = Chromosomes()
        population.append(tmp)

    return population

# Selection
def random_selection(population):
    proportional_population = []

    # proportional population
    for chromosome in population:
        for i in range(0, chromosome.valids):
            tmp = chromosome.clone()
            proportional_population.append(tmp)

    # shuffle proportional population
    random.shuffle(proportional_population)

    # pick new population
    new_population = []
    for i in range(0, P):
        new_population.append(proportional_population[i])

    return new_population

def elitist_selection(population):
    sorted_population = sorted(population, key = lambda ch : ch.valids)

    for i in range(0, P//8):
        sorted_population.pop(0)

    for i in range(0, P//8):
        sorted_population.append(sorted_population[len(sorted_population)-1 - (i*2)])
    
    return sorted_population

# Reproduction
def fixed_point_crossover(population):
    new_population = population.copy()
    random.shuffle(new_population)

    for i in range(0, P, 2):
        crossover(new_population[i].chromo, new_population[i+1].chromo, (N**2)//2)

    for chromosome in new_population:
        chromosome.correct()
        chromosome.set_valids()

    return new_population


def random_point_crossover(population):
    new_population = population.copy()
    random.shuffle(new_population)

    x = random.randint(0, (N**2)-1)
    for i in range(0, P, 2):
        crossover(new_population[i].chromo, new_population[i+1].chromo, x)

    for chromosome in new_population:
        chromosome.correct()
        chromosome.set_valids()

    return new_population

# Mutation
def mutation(population):
    for chromossome in population:
        x = random.randint(0, (N**2)-1)
        y = random.randint(0, (N**2)-1)
        tmp = chromossome.chromo[x]
        chromossome.chromo[x] = chromossome.chromo[y]
        chromossome.chromo[y] = tmp
        chromossome.correct()
        chromossome.set_valids()

# Auxiliary Functions
# crossover 2 chromossomes using on point x
def crossover(c1, c2, x):
    for i in range(0,x):
        tmp = c1[i]
        c1[i] = c2[i]
        c2[i] = tmp

# move initial position to front
def move_initial(p):
    p.remove(I)
    p = [I]+p
    return p

# get 2d coord
def get_2d(p):
    row = p//N
    col = p%N
    return (row, col)

# check valid move
def is_valid(i, j):
    rowi, coli = get_2d(i)
    rowj, colj = get_2d(j)

    if (rowi+2 == rowj and coli+1 == colj):
        return True
    if (rowi+2 == rowj and coli-1 == colj):
        return True
    if (rowi-2 == rowj and coli+1 == colj):
        return True
    if (rowi-2 == rowj and coli-1 == colj):
        return True
    if (rowi+1 == rowj and coli+2 == colj):
        return True
    if (rowi+1 == rowj and coli-2 == colj):
        return True
    if (rowi-1 == rowj and coli+2 == colj):
        return True
    if (rowi-1 == rowj and coli-2 == colj):
        return True
    return False

# check optimal solution
def check_optimal(population):
    for chromossome in population:
        if (chromossome.valids == (N**2)-1):
            return True

    return False

# Main
if __name__ == "__main__":

    # Initialization
    pop = initialize()

    iterations = 10000
    found_optimal_solution = False

    while(iterations>0 and not found_optimal_solution):
        # Selection
        pop = random_selection(pop)
            # or
#         pop = elitist_selection(pop)

        # Reproduction
 #       pop = fixed_point_crossover(pop)
            # or
        pop = random_point_crossover(pop)

        # Mutation
        mutation(pop)

        # Check for Optimal solution
        found_optimal_solution = check_optimal(pop)

        iterations -= 1

    # show final population
    for chromossome in pop:
        print(chromossome)
    