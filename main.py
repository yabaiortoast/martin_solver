from graph import graph

def checker(graph, assignment, num, node): # backtracker
  """check if a number input is valid by checking if it is
  unique and has an absolute difference of greater than 1 to
  the nodes it is connected to"""
  if num in assignment.values():
      return False
  for neighbor in graph.get(node, num):
    if neighbor in assignment:
      if abs(num - assignment[neighbor]) <= 1:
          return False
  return True

def solver(graph, assignment):
  if len(assignment) == len(graph):
    for node in sorted(assignment):
      print(f"node {node} -> {assignment[node]}")
    return True

  empty_node = [node for node in graph if node not in assignment]

  if not empty_node:
      return False

  node = empty_node[0]

  for num in range (1,9):
      if checker(graph, assignment, num, node):
        assignment[node] = num

        if solver(graph, assignment):
            return True

        del assignment[node]

  return False

if __name__ == "__main__":
    solver(graph, {}) # execute with an empty assignment and graph as
                      # your arg input -- positional
