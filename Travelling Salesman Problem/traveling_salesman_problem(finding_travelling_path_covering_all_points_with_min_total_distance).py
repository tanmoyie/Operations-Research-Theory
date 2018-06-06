"""
A Python code to solve Travelling Salesman Problem.
"""
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

# Distance callback
class CreateDistanceCallback(object):
  """Create callback to calculate distances between points."""
  def __init__(self):
    """Array of distances between points."""

    self.matrix = [
    [  0, 290, 250,  230,  190,  334, 365,   40], # Dhaka
    [290,   0, 337,  453,  396,  560, 581,  244], # Syhlet
    [250, 337,   0,  495,  396,  540, 120,  240], # Chittagonj
    [230, 453, 495,    0,  360,  150, 595,  242], # Rajshahi
    [190, 396, 396,  360,    0,  356, 496,  253], # Jossore
    [334, 560, 540,  150,  356,    0, 674,  275], # Dinajpur
    [365, 581, 120,  595,  496,  674,   0,  397], # Coxsbazar
    [40,  244, 240,  242,  253,  275, 397,    0]] # Narsingdi
# distance between Dhaka to Syhlet is 290kms and so on
  def Distance(self, from_node, to_node):
    return int(self.matrix[from_node][to_node])
def main():
  # The order of the cities in the array is the following:
  # Cities
  city_names = ["Dhaka", "Syhlet", "Chittagonj", "Rajshahi", "Jossore", "Dinajpur", "Coxsbazar", "Narsingdi"]
  tsp_size = len(city_names)
  num_routes = 1    # The number of routes, which is 1 in the TSP.
  # Nodes are indexed from 0 to tsp_size - 1. The depot is the starting node of the route.
  depot = 0

  # Create routing model
  if tsp_size > 0:
    routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()

    # Create the distance callback, which takes two arguments (the from and to node indices)
    # and returns the distance between these nodes.
    dist_between_nodes = CreateDistanceCallback()
    dist_callback = dist_between_nodes.Distance
    routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
    # Solve, returns a solution if any.
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
      # Solution cost.
      print ("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")
      # Inspect solution.
      # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
      route_number = 0
      index = routing.Start(route_number) # Index of the variable for the starting node.
      route = ''
      while not routing.IsEnd(index):
        # Convert variable indices to node indices in the displayed route.
        route += str(city_names[routing.IndexToNode(index)]) + ' -> '
        index = assignment.Value(routing.NextVar(index))
      route += str(city_names[routing.IndexToNode(index)])
      print ("Route:\n\n" + route)
    else:
      print ('No solution found.')
  else:
    print ('Specify an instance greater than 0.')

if __name__ == '__main__':
  main()
# Source code: https://developers.google.com/optimization/routing/tsp
# Google Map: https://drive.google.com/open?id=18k6uA3KdLJGc2qQGUEXbtfG93KJj8Lty&usp=sharing
