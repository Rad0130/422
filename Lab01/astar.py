file1=open('input.txt','r')
file2=open('output.txt','w')

lst=[]
for _ in file1:
    G={}
    parts=_.split()

    for i in range(0,len(parts),2):
        G[parts[i]]=int(parts[i+1])
    lst.append(G)

start=input('Enter the starting city:')
goal=input('Enter the goal city:')


import heapq

def astar(lst, start, goal):
    children={}
    heuristics={}

    for i in lst:
        city=list(i.keys())[0]
        heuristics[city]=i[city]
        children[city]={k:v for k,v in i.items() if k!=city}

    p_queue=[]
    heapq.heappush(p_queue, (heuristics[start], 0, start, [start]))

    visited=set()

    while p_queue:
        f,g,current_node,path=heapq.heappop(p_queue)

        if current_node==goal:
            return f"path: {'-->'.join(path)}\nTotal distance: {g} Km"
        if current_node in visited:
            continue
        visited.add(current_node)

        for child, cost in children[current_node].items():
            if child not in visited:
                new_g=g+cost
                new_f=new_g+heuristics[child]
                heapq.heappush(p_queue, (new_f, new_g, child, path+[child]))

    return "No path Found"

solution=astar(lst, start, goal)
file2.write(solution)


file1.close()
file2.close()


