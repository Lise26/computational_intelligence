# TSP problem

Proposition of code to solve the tsp problem. The algorithm is based on an iterated local search strategy.

That kind of algorithm aims to allow the escape from local optima. It starts by retrieving an initial solution and then apply local search on it to reach a local optimum. Next, this local minimum is somehow perturbed to reach a new solution and a local search procedure begins from this new candidate. Once a new local optimum has been found, an Accept procedure is launched to evaluate from which local minimum the search should continue. Then the Perturb-Local Search-Accept loop can iterate again and will continue until the termination criterion is reached.

### Perturbation function

Let us present in more details the perturbation procedure as it is really central to the algorithm. The search implemented in our algorithm is done in the entire solution space, which can be seen as a mountainous landscape with peaks representing maxima and cavities representing minima. Once a local optimum is reached, a simple local search algorithm is said to be "stuck" around this minimum because all its neighbours have higher costs. To allow the escape from local optima, we will use a perturbation procedure. It will allow to go back to an intermediate solution that is not as good as the current one (or, in a more graphic version, to go up the slope) in order to allow a new local search procedure to start from this solution and possibly find a better minimum. This procedure must be properly balanced in the sense that too small perturbation would not allow one to escape from a local minimum, while too large perturbation would practically amount to a random restart of the search process

### Acceptance criterion

Another important parameter on which we can play is the acceptance criterion which will decide from which local optimum the search should go on. This process will be achieved here by a simulated annealing type method which will accept worse solutions with a certain probability (following the Metropolis acceptance criterion). This criterion allows to always accept a new solution which is better but also permit to accept a worse one with a given probability.

