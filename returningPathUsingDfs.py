def dfs_path(graph, v, target, visited):
    if v == target:
        return [v]

    visited.add(v)

    for w in graph[v]:
        if w not in visited:
            path = dfs_path(graph, w, target, visited)
            if path:
                return [v] + path

    return None

if __name__=="__main__":
    graph={0:[1,2],1:[0,2,4],2:[0,1,4,3],3:[0],4:[7],7:[1]}
    visited=set()
    print(dfs_path(graph, 0, 3, set()))