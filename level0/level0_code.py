import sys

def nearest_neighbor(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    path = [0]  # Start from node 0
    visited[0] = True

    for _ in range(num_nodes - 1):
        current_node = path[-1]
        nearest = None
        min_distance = sys.maxsize

        # Find the nearest unvisited node
        for neighbor, distance in enumerate(graph[current_node]):
            if not visited[neighbor] and distance < min_distance:
                nearest = neighbor
                min_distance = distance

        # Mark the nearest node as visited and add to the path
        visited[nearest] = True
        path.append(nearest)

    # Add the starting node to complete the cycle
    path.append(0)
    return path

# Your graph dictionary

import json

# Opening JSON file
f = open('Z:\hackathon\Input data\level0.json')
data = json.load(f)


def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)



output = {}
n=0
for i in item_generator(data, "distances"):
    d = n
    ans = {d: i}
    output.update(ans)
    n+=1
#print(output)

# Find the path using the Nearest Neighbor Algorithm
result_path = nearest_neighbor(output)
start_node = result_path[0]  # Assuming the starting node is the first node in the path
level0_output = {start_node: {"path": result_path}}

print(f"The approximate shortest path is: {level0_output}")
f.close()
