import collections

def dfs(graph,root):
    visited=set([root])
    stack=[root]
    while stack:
        vertex=stack.pop()
        print(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
    print(visited)

if __name__=="__main__":
    graph={0:[1,2],1:[0,2,4],2:[0,1,4,3],3:[0],4:[2]}
    dfs(graph,0)
    