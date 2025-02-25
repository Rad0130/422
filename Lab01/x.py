file1=open('input2.txt','r')
file2=open('output2.txt','w')

vertex,edge=map(int, file1.readline().split())
G={i: [] for i in range(1,vertex+1)}

for _ in range(edge):
    ui,vi=map(int, file1.readline().split())
    G[ui].append(vi)
    G[vi].append(ui)

def BFS(G, s):

    Q=[]

    state=[0]*(vertex+1)

    Q.append(s)
    state[s]=1

    Short_path=[]

    while len(Q)!=0:
        c=Q.pop(0)
        Short_path.append(c)
        
        for neighbour in G[c]:
            if state[neighbour]==0:
                Q.append(neighbour)
                state[neighbour]=1

    return (' '.join(map(str, Short_path)))

file2.write(BFS(G, s=1))


file1.close()
file2.close()