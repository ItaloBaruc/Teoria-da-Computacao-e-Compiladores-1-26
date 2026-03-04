def uniao(A, B):
    aux = []
    for x in A:
        if x not in aux:
            aux.append(x)
    #print("loop A: o q tem no aux uniao:",aux)        

    for y in B:
        if y not in aux:
            aux.append(y)
    #print("loop B: o q tem no aux uniao:",y)            
    return aux
    
def intersecao(A, B):
    aux = []
    for x in A:
        #print(x)     
        if x in B and x not in aux:
            #print(x)                          
            aux.append(x)      
    return aux

A = [1, 2, 3]
B = [2, 3, 4]

print("União: ",uniao(A,B))
print("Interseção: ",intersecao(A,B))