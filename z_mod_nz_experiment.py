from experiment import output_parameterised_experiment

output_parameterised_experiment(
	lambda n: list(range(n)),
	lambda n: lambda x, y: (x + y) % n,
	lambda n: 0,
	2,
	100,
	None,
	10000
)

gcd = lambda a, b: a if b == 0 else gcd(b, a % b)

print("""

Multiplicative
""")
output_parameterised_experiment(
	lambda n: [k for k in range(n) if gcd(k, n) == 1],
	lambda n: lambda x, y: (x * y) % n,
	lambda n: 1,
	2,
	100,
	None,
	10000
)