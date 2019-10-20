N, init = map(int, input().split())
inputs = tuple((map(int, input().split()) for i in range(N)))
vertices = {}

for first, second in inputs:
    if first in vertices:
        vertices[first].add(second)
    else:
        vertices.update({first: {second}})

_vertices = set(vertices.keys())
res_vertices = set()
width = -1
iter_vertices = {init}

while iter_vertices:
    old = iter_vertices.copy()
    iter_vertices = set()
    for vertex in old:
        iter_vertices |= vertices.get(vertex, set())
    iter_vertices -= res_vertices
    res_vertices |= iter_vertices
    width += 1
print(width)
