import collections

def bfs(graph,root):
    visited=set([root])
    queue=collections.deque([root])

    while queue:
        vertex=queue.popleft()
        print(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print(visited)

if __name__=="__main__":
    graph={0:[1,2],1:[0,2,4],2:[0,1,4,3],3:[0],4:[2]}
    bfs(graph,0)
    