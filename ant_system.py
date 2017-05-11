from random import random, randint
import coloring

def ant_system(graph, ants = 2, beta = 0.5, tao_init = 0.1, ro = 0.2, q0 = 0.5, q_decrease = 0.05, iterations = 2):
  n = len(graph)
  i = 1

  tao = []
  visited = []
  solutions = []

  for a in range(n):
    tao.append([tao_init for _ in range(n)])
    visited.append([0 for _ in range(n)])

  while i < iterations + 1:
    # print 'i ->', i

    paths = [[] for _ in range(ants)]
    ant_solutions = []

    for ant in range(ants):
      # print 'ant ->', ant

      # Initial color
      k = 0

      # print 'k ->', k

      # Missing vertex to color
      missing = [index for index in range(n)]
      # Array of colored vertex
      solution = [None for _ in range(n)]

      # Move ant to the initial vertex
      latest = randint(0, n - 1)
      # Add color to the vertex
      solution[latest] = k
      # Add vertex to the path
      paths[ant].append(latest)
      # Delete vertex from missing
      del missing[latest]

      # print 'path ->', paths[ant]
      # print 'partial solution ->', solution

      while len(missing) > 0:
        # print 'missing ->', missing

        # Find posibles vertex that can be coloured with the k color
        posibles, eta = uncoloured_vertices(graph, missing, solution, k)

        # print 'posibles ->', posibles

        if posibles:
          # Calculate the probability of each vertex
          p = probability(eta, tao, beta, posibles, latest)

          # print 'probability ->', p

          q = random()

          index = -1

          # Elitist selection
          if q < q0:
            index = p.index(max(p))

          # Random selection
          else:
            r = random()

            for ind, v in enumerate(p):
              if r < v:
                index = ind
                break

          # Move ant to the vertex
          latest = posibles[index]
          # Add color to the vertex
          solution[latest] = k
          # Add vertex to the path
          paths[ant].append(latest)
          # Delete vertex from missing
          del missing[missing.index(latest)]

          # print 'path ->', paths
          # print 'partial solution ->', solution

        # Increase color when there are not more posibles vertex to color with the same
        else:
          k += 1
          # print 'k ->', k

      # print 'missing ->', missing
      # print 'path ->', paths[ant]
      # print 'solution ->', solution

      # Increase visited path
      previous = paths[ant][-2]

      visited[latest][previous] += 1 / float(k)
      visited[previous][latest] += 1 / float(k)

      # Add solution and colors to ant solutions
      ant_solutions.append((solution, k + 1))

    # print 'visited ->', visited
    # print 'tao ->', tao

    # Update tao based on visited vertex
    for r_index, row in enumerate(tao):
      for c_index, value in enumerate(row):
        tao[r_index][c_index] = ro * value + visited[r_index][c_index]

    # print 'tao ->', tao

    # Append solutions of every ant
    solutions.append(ant_solutions)

    # Increase iteration
    i += 1
    # Simulated annealing (Enfriamiento simulado)
    q0 += q_decrease

  return solutions

# Find posible vertices that can be coloured with the k color and is not coloured
def uncoloured_vertices(graph, missing, colors, k):
  eta = []
  posibles = []

  for miss in missing:
    links = graph[miss]

    posible = True

    for l in links:
      if colors[l] is k:
        posible = False

    if posible:
      eta.append(len(links))
      posibles.append(miss)

  return posibles, eta

# Base on http://www.sciencedirect.com/science/article/pii/S0166218X07001321
def probability(eta, tao, beta, posibles, latest):
  n = len(posibles)
  p = [0 for _ in range(n)]
  tao_eta = []
  sum = 0

  # print 'eta ->', eta
  # print 'tao ->', tao
  # print 'beta ->', beta
  # print 'posibles ->', posibles

  # for index, vertex in enumerate(posibles):
  #   print 'index', index
  #   print 'eta', eta[index]
  #   print '1/eta', 1 / float(eta[index])
  #   print '(1/eta)**beta', (1/eta[index])**beta
  #   print '((1/eta)**beta)*tao', ((1/eta[index])**beta)*tao[vertex][latest]
  #   tao_eta.append(((1 / eta[index]) ** beta) * tao[vertex][latest])
  tao_eta = [(((1 / float(eta[index])) ** beta) * tao[vertex][latest]) for index, vertex in enumerate(posibles)]

  # print 'tao_eta ->', tao_eta

  for v in tao_eta:
    sum += v

  # print 'sum ->', sum

  for index in range(n):
    p[index] = (tao_eta[index] / sum) + p[index - 1]

  return p

if __name__ == '__main__':
  graph = coloring.read('data/gc_4_1')

  solutions = ant_system(graph, ants=10, iterations=5)

  print('results')

  for i, iteration in enumerate(solutions, start=1):
    print ('iteration {}'.format(i))

    for solution in iteration:
      print ('{} {} {}'.format(solution[0], '->', solution[1]))
  
  print(graph)
