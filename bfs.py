graph={'A':['B','C'],'B':['A','C','D'], 'C':['A','B','E'],'D':['B','E'],'E':['C','D']}
path=[]
visited=[]

def bfs(graph,start):
    path.append(start)
    while len(path)!=len(graph):
        for i in path:
            if i not in visited:
                for j in graph[i]:
                    if j not in path:
                        path.append(j)
                visited.append(i)
bfs(graph,'A')
print(path)