import random



# Constants
N = 5   #board size
P = 8   #population size
I = 12  #initial position
SEED = list(range(0, (N**2)))

# Class Organismo
class Organism():

    # Create Random Organism
    def __init__(self):
        tmp = SEED.copy()
        random.shuffle(tmp)
        self.org = move_initial(tmp)
        self.valids = count_valids(self.org)

    def clone(self):
        new_org = Organism()
        new_org.org = self.org.copy()
        new_org.valids = self.valids
        return new_org


# Initialization
def initialize():

    population = []

    for i in range (0, P):
        tmp = Organism()
        population.append(tmp)

    return population

# Selection
def random_selection(population):
    proportional_population = []

    # proportional population
    for organism in population:
        for i in range(0, organism.valids):
            tmp = organism.clone()
            proportional_population.append(tmp)

    # shuffle proportional population
    random.shuffle(proportional_population)

    # pick new population
    new_population = []
    for i in range(0, P):
        new_population.append(proportional_population[i])

    return new_population

def elitist_selection(population):
    pass





# Auxiliary Functions
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

# count valid position
def count_valids(p):
    count = 0
    for i in range(0, (N**2)-1):
        if(is_valid(p[i], p[i+1])):
            count += 1
    return count


a = initialize()
for organism in a:
    print(organism.org, organism.valids)
print()
b = random_selection(a)
for organism in b:
    print(organism.org, organism.valids)