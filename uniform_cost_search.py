key=['A','B','C','D','E','F','G','H','I','J']
inf=999
graph=[[0,1,4,inf,inf,inf,inf,inf,inf,inf],
[1,0,inf,3,2,inf,inf,inf,inf,inf],
[4,inf,0,inf,inf,inf,inf,5,inf,inf],
[inf,3,inf,0,inf,5,inf,inf,inf,inf],
[inf,2,inf,inf,0,inf,4,inf,3,inf],
[inf,inf,inf,5,inf,0,inf,inf,inf,5],
[inf,inf,inf,inf,4,inf,0,inf,inf,inf],
[inf,inf,5,inf,inf,inf,inf,0,inf,inf],
[inf,inf,inf,inf,3,inf,inf,inf,0,inf],
[inf,inf,inf,inf,inf,5,inf,inf,inf,0]]
goal=[key.index('H'),key.index('I'),key.index('J')]
path=[]
visited=[]

def ucs(graph,source):
    dynm=[[inf for _ in range(len(key))] for _ in range(len(key))]
    for i in range(len(key)):
	    dynm[i][source]=0
    i=0
    while len(visited)<len(key):
        mini=inf-1
        for j in range(len(key)):
            if dynm[i][j]<=mini and j not in visited:
                mini=dynm[i][j]
                node=j
        for j in range(len(key)):
            if graph[node][j]<inf and j not in visited:
                for k in range(i,len(key)):
                    if graph[node][j]+mini<dynm[k][j]:
                        dynm[k][j]=graph[node][j]+mini
        if node in goal:
            cost=dynm[i][node]
            visited.append(node)
            break
        visited.append(node)
        i=i+1
    nnode=visited.pop()
    path.append(nnode)
    for j in range(i-1,-1,-1):
        if dynm[j][nnode]==dynm[j-1][nnode] and j>0:
            visited.pop()
        else:
            nnode=visited.pop()
            path.append(nnode)
    n=len(path)
    print("The path is")
    for i in range(n):
        print(key[path.pop()])
    print("Cost:",cost)
ucs(graph,0)