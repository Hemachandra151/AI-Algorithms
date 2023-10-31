graph={'A':['B','C'],'B':['A','C','D'], 'C':['A','B','E'],'D':['B','E'],'E':['C','D']}

def dls(graph,source,goal):
    limit=0
    root=source
    while True:
        lvl=[[]for _ in range(limit+1)]
        visited=[]
        i=0
        lvl[i].append(source)
        while i<=limit and goal not in visited:
            for root in lvl[i]:
                for node in graph[root]:
                    if node not in visited and node not in lvl[i] and i<limit:
                        lvl[i+1].append(node)
                visited.append(root)
                if goal in visited:
                    break
            i=i+1
        if goal in visited:
            break
        del lvl
        del visited
        limit=limit+1    
    if goal in visited:
        print(visited)
        print("At level ", limit)
    else:
        print("DLS failed")
dls(graph,'A','E')