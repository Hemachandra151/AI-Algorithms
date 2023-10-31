graph={'A':['B','C'],'B':['A','C','D'], 'C':['A','B','E'],'D':['B','E'],'E':['C','D']}
visited=[]

def dls(graph,source,limit,goal):
    lvl=[[]for _ in range(limit+1)]
    i=0
    lvl[i].append(source)
    while i<=limit and goal not in visited:
        for source in lvl[i]:
            for node in graph[source]:
                if node not in visited and node not in lvl[i] and i<limit:
                    lvl[i+1].append(node)
            visited.append(source)
            if goal in visited:
                break
        i=i+1
    if goal in visited:
        print(visited)
    else:
        print("DLS failed")
dls(graph,'A',2,'D')