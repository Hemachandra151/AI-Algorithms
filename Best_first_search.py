graph={'S':['A','B','C'],'A':[],'B':['D','H'],'C':[],'D':[],'H':['F','G'],'F':[],'G':['E'],'E':[]}
key=['S','A','B','C','D','E','F','G','H']
h=[10,9,7,8,8,0,6,3,6]

def inclosed(goal,closed):
    for points in closed:
        if goal==points[0]:
            return True
    return False

def gbfs(graph,source,goal):
    opened=[]
    closed=[]
    opened.append((source,h[key.index(source)]))
    root=source
    while len(opened)!=0:
        for node in graph[opened[0][0]]:
            opened.append((node,h[key.index(node)]))
        if opened[0][0]!=source:
            root=opened.pop(0)
            closed.append((root[0],parent))
        else:
            root=opened.pop(0)
            closed.append((root[0],None))
        if inclosed(goal,closed):
            break
        parent=root[0]
        opened=sorted(opened, key=lambda x:x[1])
    if not inclosed(goal,closed):
        print('Best first search failed')
    else:
        path=[]
        k=closed.pop(len(closed)-1)
        path.append(k[0])
        while inclosed(source,closed):
            for tup in closed:
                if k[1]==tup[0]:
                    k=tup
                    closed.remove(tup)
                    break
            path.append(k[0])
        print(path[::-1])
gbfs(graph,'S','E')