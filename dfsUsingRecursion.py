import collections

def dfsRecursive(Graph,vertex,visited):
    visited.add(vertex)
    print(vertex)
    for w in Graph[vertex]:
        if w not in visited:
            dfsRecursive(Graph,w,visited)


if __name__=="__main__":
    graph={0:[1,2],1:[0,2,4],2:[0,1,4,3],3:[0],4:[7],7:[1]}
    visited=set()
    dfsRecursive(graph,0,visited)
    print(visited)
        
    
    