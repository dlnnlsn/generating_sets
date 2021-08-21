from experiment import output_parameterised_experiment
from itertools import permutations

output_parameterised_experiment(
	lambda n: list(permutations(range(n))),
	lambda n: lambda x, y: tuple(x[y[i]] for i in range(n)),
	lambda n: tuple(range(n)),
	2,
	10,
	None,
	1000
)