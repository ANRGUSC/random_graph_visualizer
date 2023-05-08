import sys
import networkx as nx
import matplotlib.pyplot as plt

# Function to generate a connected random graph with n nodes
def generate_connected_graph(n):
    while True:
        graph = nx.gnp_random_graph(n, 0.5)
        if nx.is_connected(graph):
            return graph
        
# Function to generate node labels A...Z, AA, ... AZ, BA, ... etc.         
def generate_label(index):
    label = ""
    while index >= 0:
        label = chr(ord('A') + (index % 26)) + label
        index = index // 26 - 1
    return label

   

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python graph_generator.py <number_of_nodes>")
        sys.exit(1)

    try:
        num_nodes = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide an integer value for the number of nodes.")
        sys.exit(1)

    if num_nodes <= 0:
        print("Error: Please provide a positive integer value for the number of nodes.")
        sys.exit(1)1

    # Generate a connected graph with num_nodes nodes
    graph = generate_connected_graph(num_nodes)
    
    # Relabel nodes from 0 to num_nodes-1 as A, B, C, etc.
    mapping = {i: generate_label(i) for i in range(num_nodes)}     
    graph = nx.relabel_nodes(graph, mapping)

    # Plot the graph
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=1000, node_color='lightblue', edge_color='gray', font_weight='bold')


    plt.show()
