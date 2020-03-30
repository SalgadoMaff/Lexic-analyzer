import re
f=open("algoritmo_lalg.txt")
stringona=f.read()
tokens=[]
palavras=[]
linhas=[]
linha=1
identificar=0
i=0
linha=1
while( i <= len(stringona)-1):
    if(stringona[i]==" "):
        i+=1
        i-=1
    elif(stringona[i]=="\n"):
        linha+=1
    elif(stringona[i]=="{"):
        while(stringona[i]!="}"):
            i+=1
    elif(stringona[i]=="("):
        palavras.insert(identificar,"(")
        tokens.insert(identificar,"abre parenteses")

        identificar += 1
    elif(stringona[i]==","):
        palavras.insert(identificar,",")
        tokens.insert(identificar,"virgula")

        identificar += 1
    elif(stringona[i]==")"):
        palavras.insert(identificar,")")
        tokens.insert(identificar,"fecha parenteses")

        identificar += 1
    elif(stringona[i]=="+"):
        palavras.insert(identificar,"+")
        tokens.insert(identificar,"mais")        

        identificar += 1
    elif(stringona[i]=="-"):
        palavras.insert(identificar,"-")
        tokens.insert(identificar,"menos")        

        identificar += 1
    elif(stringona[i]=="*"):
        palavras.insert(identificar,"*")
        tokens.insert(identificar,"vezes")        

        identificar += 1
    elif(stringona[i]=="/"):
        palavras.insert(identificar,"/")
        tokens.insert(identificar,"divisao")        

        identificar += 1
    elif(stringona[i]=="="):
        palavras.insert(identificar,"=")
        tokens.insert(identificar,"igual")        

        identificar += 1
    elif(stringona[i]=="."):
        palavras.insert(identificar,".")
        tokens.insert(identificar,"ponto")        

        identificar += 1    
    elif(stringona[i]==":"):
        if(i+1<= len(stringona)):
            if(stringona[i+1]=="="):
                palavras.insert(identificar,":=")
                tokens.insert(identificar,"atribuição")        
        
                i+=1
            else:
                palavras.insert(identificar,":")
                tokens.insert(identificar,"dois pontos")        
        
        else:
            palavras.insert(identificar,":")
            tokens.insert(identificar,"dois pontos")        
    
        identificar += 1
    elif(stringona[i]==";"):
        palavras.insert(identificar,";")
        tokens.insert(identificar,"ponto e virgula")        

        identificar += 1
    elif(stringona[i]=="<"):
        if(i+1<= len(stringona)):
            if(stringona[i+1]=="="):
                palavras.insert(identificar,"<=")
                tokens.insert(identificar,"menor-igual")        
        
                i+=1
            elif(stringona[i+1]==">"):
                palavras.insert(identificar,"<>")
                tokens.insert(identificar,"diferente")        
        
                i+=1
            else:
                palavras.insert(identificar,"<")
                tokens.insert(identificar,"menor")
        
        else:
            palavras.insert(identificar,"<")
            tokens.insert(identificar,"menor")        
    
        identificar += 1
    elif(stringona[i]==">"):
        if(i+1<= len(stringona)):
            if(stringona[i+1]=="="):
                palavras.insert(identificar,">=")
                tokens.insert(identificar,"maior-igual")        
        
                i+=1
            else:
                palavras.insert(identificar,">")
                tokens.insert(identificar,"maior")        
        
        else:
            palavras.insert(identificar,">")
            tokens.insert(identificar,"maior")
    
        identificar += 1
    elif(stringona[i]=="p"):
        if(i+1<= len(stringona)):
            j=i+1
            palavra=stringona[i]
            
            while(stringona[j].isalpha() or stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            if(palavra=="program"):
                tokens.insert(identificar,"PROGRAMA")
            elif(palavra=="procedure"):
                tokens.insert(identificar,"PROCEDIMENTO")
            else:
                tokens.insert(identificar,"id")
            palavras.insert(identificar,palavra)        
    
            i=j-1
        else:
            palavras.insert(identificar,"p")
            tokens.insert(identificar,"id")        
    
        identificar += 1

    elif(stringona[i]=="v"):
        if(i+1<= len(stringona)):
            j=i+1
            palavra=stringona[i]
            while(stringona[j].isalpha() or stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            if(palavra=="var"):
                tokens.insert(identificar,"variavel")
            else:
                tokens.insert(identificar,"id")
            palavras.insert(identificar,palavra)           
             
            i=j-1
        else:
            palavras.insert(identificar,"v")
            tokens.insert(identificar,"id")
    
        identificar += 1
    elif(stringona[i]=="d"):
        if(i+1<= len(stringona)):
            j=i+1
            palavra=stringona[i]
            while(stringona[j].isalpha() or stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            if(palavra=="do"):
                tokens.insert(identificar,"faca")
            else:
                tokens.insert(identificar,"id")
            palavras.insert(identificar,palavra)        
    
            i=j-1
        else:
            palavras.insert(identificar,"d")
            tokens.insert(identificar,"id")
    
        identificar += 1
    elif(stringona[i]=="b"):
        if(i+1<= len(stringona)):
            j=i+1
            palavra=stringona[i]
            while(stringona[j].isalpha() or stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            if(palavra=="begin"):
                tokens.insert(identificar,"começo")
            else:
                tokens.insert(identificar,"id")
            palavras.insert(identificar,palavra)
    
            i=j-1
        else:
            palavras.insert(identificar,"b")
            tokens.insert(identificar,"id")
    
        identificar += 1
    elif(stringona[i]=="e"):
        if(i+1<= len(stringona)):
            j=i+1
            palavra=stringona[i]
            while(stringona[j].isalpha() or stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            if(palavra=="end"):
                tokens.insert(identificar,"fim")
            elif(palavra=="else"):
                tokens.insert(identificar,"senão")
            else:
                tokens.insert(identificar,"id")
            palavras.insert(identificar,palavra)
            i=j-1
        else:
            palavras.insert(identificar,"e")
            tokens.insert(identificar,"id")
        identificar += 1
    elif(stringona[i]=="w"):
        if(i+1<= len(stringona)):
            j=i+1
            palavra=stringona[i]
            while(stringona[j].isalpha() or stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            if(palavra=="while"):
                tokens.insert(identificar,"enquanto")
            elif(palavra=="write"):
                tokens.insert(identificar,"escreva")
            else:
                tokens.insert(identificar,"id")
            palavras.insert(identificar,palavra)
            i=j-1
        else:
            palavras.insert(identificar,"w")
            tokens.insert(identificar,"id")
        identificar += 1
    elif(stringona[i]=="i"):
        if(i+1<=len(stringona)):
            j=i+1
            palavra=stringona[i]
            while(stringona[j].isalpha() or stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            if(palavra=="integer"):
                tokens.insert(identificar,"INTEIRO")
            elif(palavra=="if"):
                tokens.insert(identificar,"se")
            else:
                tokens.insert(identificar,"id")
            palavras.insert(identificar,palavra)
            i=j-1
        else:
            palavras.insert(identificar,"i")
            tokens.insert(identificar,"id")
        identificar += 1
    elif(stringona[i]=="r"):
        if(i+1<=len(stringona)):
            j=i+1
            palavra=stringona[i]
            while(stringona[j].isalpha() or stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            if(palavra=="real"):
                tokens.insert(identificar,"REAL")
            elif(palavra=="read"):
                tokens.insert(identificar,"leia")
            else:
                tokens.insert(identificar,"id")
            palavras.insert(identificar,palavra)
            i=j-1
        else:
            palavras.insert(identificar,"r")
            tokens.insert(identificar,"id")
        identificar += 1
    elif(stringona[i]=="t"):
        if(i+1<=len(stringona)):
            j=i+1
            palavra=stringona[i]
            while(stringona[j].isalpha() or stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            if(palavra=="then"):
                tokens.insert(identificar,"entao")
            else:
                tokens.insert(identificar,"id")
            palavras.insert(identificar,palavra)
            i=j-1
        else:
            palavras.insert(identificar,"t")
            tokens.insert(identificar,"id")
        identificar += 1
    elif(stringona[i].isalpha()):
        if(i+1<=len(stringona)):
            j=i+1
            palavra=stringona[i]
            while(stringona[j].isalpha() or stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            palavras.insert(identificar,palavra)
            tokens.insert(identificar,"id")
            i=j-1
        else:
            palavras.insert(identificar,stringona[i])
            tokens.insert(identificar,"id")
        identificar += 1
    elif(stringona[i].isdigit()):
        if(i+1<=len(stringona)):
            palavra=stringona[i]
            j=i+1
            while(stringona[j].isdigit()):
                palavra=palavra+stringona[j]
                j+=1
                if(j>len(stringona)):
                    break
            if(j+1<len(stringona)):
                if(stringona[j]=="." and stringona[j+1].isdigit()):
                    palavra=palavra+stringona[j]
                    j+=1
                    while(stringona[j].isdigit()):
                        palavra=palavra+stringona[j]
                        j+=1
                        if(j>len(stringona)):
                            break
            palavras.insert(identificar,palavra)
            tokens.insert(identificar,"numero")
            i=j-1
        else:
            palavras.insert(identificar,stringona[i])
            tokens.insert(identificar,"numero")
        identificar += 1
    else:
        palavras.insert(identificar,stringona[i])
        tokens.insert(identificar,"erro")
        identificar += 1
    linhas.insert(identificar, linha)
    i+=1
for i in range(len(tokens)):
    print(str(palavras[i])+" | "+str(tokens[i])+" | linha:"+str(linhas[i]))    

f.close()
