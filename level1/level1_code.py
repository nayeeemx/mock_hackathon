import math
import json

# Opening JSON file
f = open('Z:\hackathon\Input data\level1a.json')
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



node_and_distances = {}
#restaurance neightbou value
r=0
for i in item_generator(data, "neighbourhood_distance"):
    d="r"+str(r)
    ans = {d: i}
    node_and_distances.update(ans)
    r+=1

#neightbour value
n=0
for i in item_generator(data, "distances"):
    d = "n"+str(n)
    ans = {d: i}
    node_and_distances.update(ans)
    n+=1
#print(node_and_distances)

#restaurants and their capacity
order_quantity_nodes={}
r=0
d="r"+str(r)
ans={d:0}
order_quantity_nodes.update(ans)

#nodes and their capacity
n=0
for i in item_generator(data, "order_quantity"):
    d = "n"+str(n)
    ans = {d: i}
    order_quantity_nodes.update(ans)
    n+=1
#print(order_quantity_nodes)

#vehicles and their capacity
vehicle_capacities={}
r=0
for i in item_generator(data, "capacity"):
    d="v"+str(r)
    ans = {d: i}
    vehicle_capacities.update(ans)
    r+=1
#print(vehicle_capacities)


#finding the path
from queue import PriorityQueue

def shortest_path(vehicle_capacity, node_and_distances, order_and_capacity):
    total_nodes = len(node_and_distances)
    total_order = sum(order_and_capacity.values())
    unvisited_nodes = list(node_and_distances.keys())
    total_dist = {node: 0 for node in unvisited_nodes}
    result = {}
    iteration = 0

    while total_order >= vehicle_capacity:
        iteration += 1
        path = [None] * (2 * len(unvisited_nodes) + 1)
        path[0] = 'r0'
        index = 1
        priority_queue = PriorityQueue()
        for node in unvisited_nodes:
            priority_queue.put((total_dist[node], node))

        while not priority_queue.empty():
            dist, node = priority_queue.get()
            delivery_capacity = min(vehicle_capacity, order_and_capacity[node])
            path[index] = node
            index += 2
            total_dist[node] += node_and_distances[node][0] + node_and_distances[node][1]
            order_and_capacity[node] -= delivery_capacity
            if order_and_capacity[node] == 0:
                unvisited_nodes.remove(node)
        result[f"path{iteration}"] = list(filter(None, path))
        total_order -= vehicle_capacity

    return result

vehicle_capacity = vehicle_capacities["v0"]
print(vehicle_capacity)
shortest_path_with_max_capacity={}
shortest_path_with_max_capacity["v0"]=shortest_path(vehicle_capacity, node_and_distances, order_quantity_nodes)


with open("level1a_output.json", "w") as outfile: 
    json.dump(shortest_path_with_max_capacity, outfile)

f.close()
