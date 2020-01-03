import sys
import os.path
import re
import random
import copy


# GLOBAL VARIABLES
vertex_count = None
edge_count = None
vertex_weights = []
adjacency_matrix = [[]]


# noinspection PyUnusedLocal
def read_file(file_name):

    # Global variables...
    global vertex_count, edge_count, vertex_weights, adjacency_matrix
    file = open(file_name, 'r')

    # Read the file till the end...
    while True:
        # Read the line and remove the newline character at the end
        line = file.readline().rstrip('\n\r')
        if not line:
            # Means we reached to the end of file...
            break

        if vertex_count is None:
            # Then this is the line for indicating the number of vertices...
            vertex_count = int(line)

            # After we get the vertex count, we initialize adjacency matrix with zeros...
            adjacency_matrix = [[0 for i in range(vertex_count)] for i in range(vertex_count)]

        elif edge_count is None:
            # Then this is the line for indicating the number of edges...
            edge_count = int(float(line))
        elif len(vertex_weights) == 0:
            # These are the lines indicating vertex weights...
            for i in range(vertex_count):
                # Get only the second part of the string...
                _, _, line = line.partition(' ')
                # Convert comma separated values into dot separated...
                line = line.replace(',', '.')
                # Add the value into vertex weights list as float type...
                vertex_weights.append(float(line))

                # We will read the next line, if this is not the last vertex's weight...
                if i + 1 != vertex_count:
                    line = file.readline().rstrip('\n\r')
        else:
            # These are the lines indicating edges between vertices...
            line = line.split()
            # The first element of line is row and second element of line is column...
            adjacency_matrix[int(line[0])][int(line[1])] = 1

    # Close the file...
    file.close()


def check_inputs():
    file_name = sys.argv[1]

    # After getting the file name, we need to check if that file exists...
    if not os.path.isfile(file_name):
        print("Cannot found the graph file with the filename you provided!")
        exit(-1)

    # Checking if num_generations, pop_size, crossover_prob, mutation_prob are numbers...
    num_generations = sys.argv[2]
    pop_size = sys.argv[3]
    crossover_prob = sys.argv[4]
    mutation_prob = sys.argv[5]

    if re.search("[^0-9]", num_generations) or re.search("[^0-9]", pop_size) or \
            re.search("[^0-9.]", crossover_prob) or re.search("[^0-9.]", mutation_prob):

        print("You entered some inappropriate arguments!")
        exit(-1)
    else:
        num_generations = int(num_generations)
        pop_size = int(pop_size)
        crossover_prob = float(crossover_prob)
        mutation_prob = float(mutation_prob)

    return file_name, num_generations, pop_size, crossover_prob, mutation_prob


def generate_random_population(pop_size):
    global vertex_count

    population = []

    # Initializing population with strings full of zeros...
    for i in range(pop_size):
        population.append("0" * vertex_count)

    for i in range(pop_size):
        for j in range(vertex_count):

            # Generate a uniform random number between 0 and 1...
            random_number = random.uniform(0, 1)

            # If the random_number is greater than or equal to 0.5, we set that index to one...
            if random_number >= 0.5:
                population[i] = population[i][:j] + "1" + population[i][j+1:]

    return population


def repair_population(pop_size, population):
    global vertex_count

    # We will check each solution...
    for i in range(pop_size):

        # While this solution is not feasible, try to make it feasible...
        while not check_solution(population[i]):

            # Generate a uniform random number between 0 and vertex_count...
            random_number = random.uniform(0, vertex_count)

            # We will keep generating a random number, if that location of the solution is not zero...
            while population[i][int(random_number)] != "0":
                random_number = random.uniform(0, vertex_count)

            # When we found an index that is zero, we change it to one...
            population[i] = population[i][:int(random_number)] + "1" + population[i][int(random_number) + 1:]


def check_solution(solution):
    global vertex_count, adjacency_matrix

    # We will copy adjacency matrix, to preserve the original...
    new_adjacency_matrix = copy.deepcopy(adjacency_matrix)

    # We will convert all edges from one to zero for each included vertex...
    for row in range(vertex_count):

        # If that vertex is not included, move on...
        if solution[row] == '0':
            continue

        # Loop the row...
        for i in range(vertex_count):
            new_adjacency_matrix[row][i] = 0
        # Loop the column...
        for i in range(vertex_count):
            new_adjacency_matrix[i][row] = 0

    # Lastly, we will check if adjacency matrix contains ones...
    if 1 in (1 in i for i in new_adjacency_matrix):
        return False

    return True


def construct_mating_pool(pop_size, population):

    mating_pool = []

    for i in range(pop_size):

        # Generate a uniform random number between 0 and pop_size...
        random_number = random.uniform(0, pop_size)

        mating_pool.append(population[int(random_number)])

    return mating_pool


if __name__ == '__main__':

    # Checking if the program has run with the CORRECT NUMBER of command-line arguments...
    if len(sys.argv) != 6:
        print("You didn't run the program with the CORRECT NUMBER of command-line arguments!")
        print("Usage: python genetic_algorithm.py graph_file num_generations pop_size crossover_prob mutation_prob")
        exit(-1)

    # Validating inputs...
    file_name, num_generations, pop_size, crossover_prob, mutation_prob = check_inputs()

    # Read graph file and create adjacency matrix...
    read_file(file_name)

    # Generate random population...
    population = generate_random_population(pop_size)

    # Repairing infeasible solutions...
    repair_population(pop_size, population)

    # Construct mating pool...
    mating_pool = construct_mating_pool(pop_size, population)
