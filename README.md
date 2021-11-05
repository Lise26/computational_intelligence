# TSP problem

Proposition of code to solve the tsp problem. The algorithm is based on an iterated local search strategy.

That kind of algorithm aims to allow the escape from local optima. It starts by retrieving an initial solution and then apply local search on it to reach a local optimum. Next, this local minimum is somehow perturbed to reach a new solution and a local search procedure begins from this new candidate. Once a new local optimum has been found, an Accept procedure is launched to evaluate from which local minimum the search should continue. Then the Perturb-Local Search-Accept loop can iterate again and will continue until the termination criterion is reached.
