def calcula_valores(valor):
  soma = 0
  multiplicacao = 1
  
  for numero in valor:
    soma += int(numero)
    multiplicacao *= int(numero)
   
   
  
  print(soma)
  print(multiplicacao)
   
 
calcula_valores('3011392323012')