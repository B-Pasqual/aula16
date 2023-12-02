def ehPrimo(numero):
  limite = numero + 1
  
  if numero == 0 or numero == 1:
    return False
  
  for valor in range(1,limite):
    if numero % valor == 0 and numero != valor and valor != 1:
      return False
  return True

def quantos_primos(numero):
  quantidade_primos = 0
 
  for valor in range(numero + 1):
    if ehPrimo(valor):
      quantidade_primos += 1
  
  return quantidade_primos

def calcula_soma_primos(numero):
    lista_primos = []
    contador = 2 
    soma = 0
    quantidade_primos = 10

    primos = 0

    while primos != quantidade_primos:
        if ehPrimo(contador):
            lista_primos.append(contador)
            soma += contador
            primos += 1
        contador += 1  

    print(f'soma dos primos: {soma}')
    return (f'lista de primos: {lista_primos}')

print(calcula_soma_primos(29))  