# 1 questao

indice = 13
soma = 0
k = 0
while k<indice:
    k = k + 1
    soma = soma + k

print(soma)
#2 questao
numero = int(input("Digite um numero:"))
def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print("o valor é:",fibo(numero))

#3 questao
def af(fd):
    df=[valor for valor in fd if valor > 0]
    menor= min(df)
    maior=max(df)
    
    mm=sum(df)/len(df)
    dam= len([valor for valor in df if valor >mm])
    
    return menor,maior,mm,dam

fd = [10,100,15,50,101,105,12]
menor,maior,dam,mm=af(fd)

print(menor)
print(maior)
print(mm)
print(dam)

#5 questao
def inverter(string):
    invertido= ""
    for i in range(len(string)-1,-1,-1):
        invertido = invertido + string[i]
    return invertido

texto = input("digite o texto: ")
invertido = inverter(texto)

print(texto)
print(invertido)
        
