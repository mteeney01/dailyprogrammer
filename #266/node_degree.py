fname = 'input.txt'
def node_degree():
    N = 0
    with open(fname) as f:
        N = int(f.readline())
        lines = [x.strip('\n') for x in f.readlines()]
    nodes = { n:0 for n in range(1, N+1) }
    adjacency = [[0 for n in range(0, N)] for _ in range(0,N)]
    for line in lines:
        p,c = map(int,line.strip().split())
        nodes[p] += 1
        nodes[c] += 1
        adjacency[p-1][c-1], adjacency[c-1][p-1] = 1,1

    for node in nodes:
        print("Node {} has a degree of {}".format(node, nodes[node]))

    print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in adjacency]))

node_degree()