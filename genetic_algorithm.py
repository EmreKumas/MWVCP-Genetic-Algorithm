import sys
import os.path
import re


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


if __name__ == '__main__':

    # Checking if the program has run with the CORRECT NUMBER of command-line arguments...
    if len(sys.argv) != 6:
        print("You didn't run the program with the CORRECT NUMBER of command-line arguments!")
        print("Usage: python genetic_algorithm.py graph_file num_generations pop_size crossover_prob mutation_prob")
        exit(-1)

    file_name, num_generations, pop_size, crossover_prob, mutation_prob = check_inputs()
