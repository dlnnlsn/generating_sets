from disjoint_set import DisjointSet
from random import shuffle

def find_generating_set(group_elements = [], group_operation = lambda x, y: x * y, identity_element = None):
	components = DisjointSet(group_elements)
	shuffle(group_elements)
	candidates = iter(group_elements)
	generating_set = []
	while components.components > 1:
		candidate_element = next(candidates)
		if candidate_element == identity_element: continue
		generating_set.append(candidate_element)
		for element in group_elements:
			components.union(element, group_operation(candidate_element, element))
	return generating_set