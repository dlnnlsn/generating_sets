from experiment import output_parameterised_experiment

output_parameterised_experiment(
	lambda n: list(range(n)),
	lambda n: lambda x, y: (x + y) % n,
	lambda n: 0,
	2,
	100,
	None,
	1000
)