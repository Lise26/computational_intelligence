# TSP problem

Proposition of code to solve the tsp problem. The algorithm is based on an iterated local search strategy.

That kind of algorithm aims to allow the escape from local optima. It starts by retrieving an initial solution and then apply local search on it to reach a local optimum. Next, this local minimum is somehow perturbed to reach a new solution and a local search procedure begins from this new candidate. Once a new local optimum has been found, an Accept procedure is launched to evaluate from which local minimum the search should continue. Then the Perturb-Local Search-Accept loop can iterate again and will continue until the termination criterion is reached.

### Perturbation function

Let us present in more details the perturbation procedure as it is really central to the algorithm. If we recontextualise things a little, the goal of our algorithm is to find the optimal solution to a problem. This search is done in the entire solution space, which can be seen as a mountainous landscape with peaks representing maximums and cavities representing minimums, local minimums being cavities and the optimal solution being the deepest cavity in the valley. Once a local optimum is reached, a simple local search algorithm is said to be "stuck" around this minimum because all its neighbours have higher values than it and thus no improving solution can be reached, leading the algorithm to terminate. However, being in a valley cavity does not ensure that we are in the deepest one. This is why it is sometimes necessary to accept to go back to an intermediate solution that is not as good (or, in a more graphic version, to go up the slope) in order to be able to go back down again. This is exactly the purpose of the perturbation procedure. It will modify the current solution, which will lead to an increase in the value of the objective function, in order to allow a new local search procedure to start from this solution and possibly find a better minimum. This procedure must be properly balanced in the sense that too small perturbation would not allow one to escape from a local minimum, while too large perturbation would practically amount to a random restart of the search process.


### Acceptance criterion

Another important parameter on which we can play is the acceptance criterion which will decide from which local optimum the search should go on. This process will be achieved here by a simulated annealing type method which will accept worse solutions with a certain probability. The probability distribution used to select a worse solution corresponds to the Metropolis acceptance criterion. This criterion is quite convenient since it allows to always accept a new solution which is better but also permit to accept a worse one with a given probability.

