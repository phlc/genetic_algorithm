import numpy as np

# Constants
N = 5   #board size
P = 8   #population size
I = 12  #initial position
SEED = np.arange(0, (N**2))


# Initialization
def initialize():

    population = []

    for i in range (0, P):
        tmp = SEED.copy()
        np.random.shuffle(tmp)
        tmp = np.delete(tmp, np.where(tmp == I))
        tmp = np.insert(tmp, 0, 12)
        population.append(tmp)

    return population

# Selection
def random_selection(population):
    new_population = []

    for organism in population:
        for i in range(0, count_valids(organism)):
            tmp = organism.copy()
            new_population.append(tmp)

    ######

def elitist_selection(population):
    pass





# Auxiliary Functions
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
