
def read(filename):
  file = open(filename, 'r')
  line = file.readline().split()

  n = int(line[0])
  e = int(line[1])

  graph = [[] for _ in range(n)]

  for _ in range(e):
    line = file.readline().split()

    u = int(line[0])
    v = int(line[1])

    graph[u].append(v)
    graph[v].append(u)

  return graph

def fitness(graph, solution):
  conflicts = 0

  n = len(graph)

  for i, u in enumerate(graph):
    color = solution[i]

    for v in graph[i]:
      if v > i and solution[v] is color:
        conflicts += 1

  return conflicts

def test():
  graph = read('data/gc_4_1')
  solutions = [
    [0, 1, 2, 2],
    [1, 1, 2, 2],
    [0, 1, 2, 1],
    [1, 1, 2, 1],
    [0, 1, 0, 0]
  ]

  print('graph {}'.format(graph))

  print('solution -> fitness -> number of colors')

  for solution in solutions:
    print ('{} {} {} {} {}'.format(solution, '->', fitness(graph, solution), '->', len(list(set(solution)))))

if __name__ == '__main__':
  test()
