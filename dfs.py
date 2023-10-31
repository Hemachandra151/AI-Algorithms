graph={'A':['B','C'],'B':['A','C','D'], 'C':['A','B','E'],'D':['B','E'],'E':['C','D']}
path=[]
def dfs(graph,start):
    path.append(start)
    if(len(path)!=len(graph)):
        for i in graph[start]:
            if i not in path:
                dfs(graph,i)
dfs(graph,'A')
print(path)