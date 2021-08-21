from generators import find_generating_set

ITERATIONS = 1000

group_operation = lambda n: lambda x, y: (x + y) % n
group_elements = lambda n: list(range(n))

for n in range(2, 100):
	total_size_without_identity_optimisation = 0
	total_size_with_identity_optimisation = 0
	for _ in range(ITERATIONS):
		elements = group_elements(n)
		operation = group_operation(n)
		total_size_without_identity_optimisation += len(find_generating_set(elements, operation))
		total_size_with_identity_optimisation += len(find_generating_set(elements, operation, 0))
	print(f"{n:4d}: {total_size_without_identity_optimisation/ITERATIONS:10.6f} {total_size_with_identity_optimisation/ITERATIONS:10.6f}")