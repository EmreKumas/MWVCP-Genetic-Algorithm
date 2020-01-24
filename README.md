# MWVCP-Genetic-Algorithm

In ***MWVCP(Minimum Weighted Vertex Cover Problem)***, a member of *np-complete* family, it is required to find the **vertex cover** of a given graph such that the sum of the weights of the nodes is the minimum. A vertex cover of a graph is “a set of vertices such that each edge of the graph is *incident* to at least one vertex of the set”.

## Details

It would be easier to explain this problem over an example:

![img](https://i.ibb.co/ChswwzK/MWVCP-Example.jpg)

For this graph, lets select the nodes ***d, r, f, n and l*** with a weight of sum *15*. This may be not the minimum solution but it covers all the edges so we don't need to select the remaining nodes.

### How to write a solution

We need to think simple of how to write a solution. The easist way to do so is to write a ***sequence of binary numbers*** with the length of nodes. For example, for the graph above the solution's length must be 7 because we have 7 nodes. And simply we give each node an index and for the solution, if we include that node we write 1 otherwise we write 0.

- d : 0
- r : 1
- f : 2
- n : 3
- l : 4
- j : 5
- g : 6

Then, our solution becomes this: 1111100

### Input file

The input file you give to the program must contain these informations:

- Number of nodes
- Number of edges
- List of node weights (format: X W where W is the weight of node X)
- List of edges (format: X Y which indicates an edge from node X to node Y)

I've included three different graphs for this problem with densities 0.03, 0.15 and 0.3.

## Genetic Algorithm

The genetic algorithm is a search heuristic that is inspired by Charles Darwin’s theory of natural evolution. This algorithm reflects the process of natural selection where the fittest individuals are selected for reproduction in order to produce offspring of the next generation.

The biggest of advantage of using the genetic algorithm is that it always finds a solution. Because it uses a population of solutions, it could avoid being trapped in local optimal solution like in traditional methods. But the biggest disadvantage of the genetic algorithm is that, it is so slow. According to the parameters you set, you may wait hours even days for it to be completed.

### Command-line Arguments

There are four parameters that affect the solution of the genetic algorithm. These are the number of generations, population size, crossover probability and mutation probability. Every time you choose a different value for these parameters, you get different results. Whenever you start this program from the console, you should write your arguments firstly in this format:

`python genetic_algorithm.py graph_file num_generations pop_size crossover_prob mutation_prob`

### Output

While the program is running, it writes all the results to both to output file and the terminal. After each generation ends, it writes the best solution itself, best solution's fitness value, average fitness value and worst solution's fitness value. After the last generation ends, the program writes the overall best solution and its fitness value, lastly.
