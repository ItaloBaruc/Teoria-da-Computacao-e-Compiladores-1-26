def Trava(senha):
    tentativa = senha.split('-')
    estado = 0
    for x in tentativa:
        if estado ==  0 and x == '1':       
            estado += 1
            #print(estado)     
        elif estado ==  1 and x == '2':
            estado += 1  
            #print(estado)                       
        elif estado == 2 and x == '3':
            estado += 1
            #print(estado)     
        else: 
            estado = 0
            break
    #print(estado)
    #print(tentativa)
    if estado == 3:
        print("Acesso Concedido!")
    else:
        print("Acesso Negado!")

senha = input("digita a senha(no formato ex:'1-2-3'): ")
Trava(senha)