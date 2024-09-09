def somar(a, b):
    soma = a + b    
    return soma


def subtrair(a, b):
    return a - b


#Esta função recebe outra função como terceiro parametro
def exibir_resutado(a, b, funcao):
    
    resultado = funcao(a, b)
    print(f'A soma entra {a} e {b} é iqual a {resultado}')


#chamando a função e passando seu parametros
exibir_resutado(10, 25, somar)
exibir_resutado(10, 25, subtrair)

#fazendo uma função de variavel/objeto
var_somar = somar

#Utilizando a variavel como uma função
print(var_somar(10, 10))
