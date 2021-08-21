from generators import find_generating_set

def run_experiment(
	group_elements = [],
	group_operation = lambda x, y: x * y,
	identity_element = 1,
	iterations = 1000
):
	return (sum(len(find_generating_set(group_elements, group_operation)) for _ in range(iterations)) / iterations,
		sum(len(find_generating_set(group_elements, group_operation, identity_element)) for _ in range(iterations)) / iterations)

def output_parameterised_experiment(
	group_elements = lambda n: [],
	group_operation = lambda n: lambda x, y: x * y,
	group_identity = lambda n: 1,
	min_n = 1,
	max_n = 100,
	parameters = None,
	iterations = 1000
):
	parameters = parameters or range(min_n, max_n)
	for n in parameters:
		without_id_op, with_id_op = run_experiment(
			group_elements(n),
			group_operation(n),
			group_identity(n),
			iterations
		)
		print(f"{n:10d}: {without_id_op:10.4f} {with_id_op:10.4f}")