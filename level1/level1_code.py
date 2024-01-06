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
print(node_and_distances)

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
print(order_quantity_nodes)

#vehicles and their capacity
vehicle_capacity={}
r=0
for i in item_generator(data, "capacity"):
    d="r"+str(r)
    ans = {d: i}
    vehicle_capacity.update(ans)
    r+=1
print(vehicle_capacity)


#finding the path





def find_nearest_neighbor(node, unvisited_nodes, distances):
    min_distance = float('inf')
    nearest_node = None
    
    for neighbor in unvisited_nodes:
        if distances[node][neighbor] < min_distance:
            min_distance = distances[node][neighbor]
            nearest_node = neighbor
            
    return nearest_node

def find_next_node(current_node, unvisited_nodes, distances, vehicle_capacity, current_capacity):
    nearest_neighbor = find_nearest_neighbor(current_node, unvisited_nodes, distances)
    if nearest_neighbor is None:
        return 'r0'
    
    if current_capacity + neighbors_capacity[nearest_neighbor] <= vehicle_capacity:
        return nearest_neighbor
    else:
        return 'r0'

def visit_all_nodes(distances, neighbors_capacity, vehicle_capacity):
    unvisited_nodes = set(distances.keys())
    unvisited_nodes.remove('r0')
    current_node = 'r0'
    current_capacity = 0
    path = ['r0']
    
    while unvisited_nodes:
        next_node = find_next_node(current_node, unvisited_nodes, distances, vehicle_capacity, current_capacity)
        
        if next_node == 'r0':
            path.append('r0')
            current_capacity = 0
        else:
            path.append(next_node)
            unvisited_nodes.remove(next_node)
            current_capacity += neighbors_capacity[next_node]
            
        current_node = next_node
    
    path.append('r0')
    return path






path = visit_all_nodes(node_and_distances, order_quantity_nodes, vehicle_capacity)
print("Path:", path)







f.close()
