import random

def f_respostas(qnt:int)->list:
    possibilidades = ["I", "S", "N"]
    respostas = list()

    for i in range(qnt):
        r = random.randint(0,2)
        respostas.append(possibilidades[r])

    return respostas
#------------------------------------------------
def f_dicionario(qnt:int, perguntas:int, letra:str)->dict:
    dici = dict()

    for i in range(qnt):
        lst_resp = f_respostas(perguntas)
        dici[letra + str(i+1)] = lst_resp

    return dici
#------------------------------------------------
def f_match(dictM:dict, dictF:dict):
    dic_casais = dict()

    for i in dictF:
        r1 = dictF[i]
        for j in dictM:
            r2 = dictM[j]
            pts = f_pontuacao(r1, r2)
            dic_casais[(i, j)] = pts

    return dic_casais
#-----------------------------------------------
def f_pontuacao(respostasF:list, respostasM:list)->int:
    pontuacao = 0
    
    for i in range(len(respostasF)):
        if  (respostasF[i] == respostasM[i] and respostasF[i] != "I"):
            pontuacao += 2
        elif    (respostasF[i] == "I" or respostasM[i] == "I"):
            pontuacao += 1

    return pontuacao
#------------------------------------------------
def f_imprime(casais:dict)->None:
    for chave in casais.keys():
        print(chave[0], chave[1], casais[chave])
