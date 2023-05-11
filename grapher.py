edges = []
nodes = 0
dirs = []

def maxof(line):
    if(line == "}\n"): return 0
    if(int(line[0]) >= int(line[5])):
        return int(line[0])
    else:
        return int(line[5])

with open("input.dot", 'r') as graph:
    line = graph.readline()
    line = graph.readline()
    line = graph.readline()
    while(line != "graph {" and line != ''):
        edges.append(line)
        temp = maxof(line)
        if(temp > nodes):
            nodes = temp
        line = graph.readline()
    edges.pop()

def attribute(a, b):
    if(((str(a)+" -- "+str(b)+"\n") in edges) or ((str(b)+" -- "+str(a)+"\n") in edges)):
        return " [style=\"bold\" color=\"blue\"]\n"
    else:
        return " [style=\"dashed\" color=\"red\"]\n"

for i in range(nodes):
    for j in range(nodes):
        if(i < j):
            dirs.append((str(i+1)+" -> "+str(j+1)+attribute(i+1, j+1)))

with open("output.dot", 'w') as dirg:
    dirg.write("digraph {\n")
    dirg.write("node [shape=\"plaintext\"]\n")
    for d in dirs:
        dirg.write(d)
    dirg.write("}\n")
