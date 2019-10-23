def widthSearch(init, inputs):
    vertices = {}
    
    for first, second in inputs:
        if first in vertices:
            vertices[first].add(second)
        else:
            vertices.update({first: {second}})
    
    _vertices = set(vertices.keys())
    res = set()
    width = -1
    current = {init}
    
    while current:
        old = current.copy()
        current = set()
        for vertex in old:
            current |= vertices.get(vertex, set())
        current -= res
        res |= current
        width += 1
    return width

# Tests
for i in '123':
    with open('ex'+i,'rb') as file:
        N, init = map(int, file.readline().split())
        inputs = tuple((map(int, file.readline().split()) for i in range(N)))
        print(f'file ex{i}:',widthSearch(init, inputs))
# Input
N, init = map(int, input('Your example:\n').split())
inputs = tuple((map(int, input().split()) for i in range(N)))
print(widthSearch(init, inputs))
