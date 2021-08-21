from itertools import repeat

class DisjointSet:
	def __init__(self, elements=[]):
		self._parents = dict(zip(elements, elements))
		self._ranks = dict(zip(elements, repeat(0)))
		self._components = len(self._parents)
	
	def find(self, x):
		if not x in self._parents:
			self._components += 1
			self._parents[x] = x
			self._ranks[x] = 0
			return x
		
		while not self._parents[x] == x:
			x, self._parents[x] = self._parents[x], self._parents[self._parents[x]]
		return x
	
	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)

		if x == y: return

		if self._ranks[x] < self._ranks[y]:
			x, y = y, x
		
		self._parents[y] = x

		if self._ranks[x] == self._ranks[y]:
			self._ranks[x] += 1

		self.components -= 1

	def components(self):
		return self._components
