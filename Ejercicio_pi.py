


n=int(input("Escriba un # que representara el límite excluido de los enteros usados como denominador en la sumatoria."))
pi=0

for x in range(1,n,2):
  calculo_signo = (x-1)/2
  den=x
  if calculo_signo%2==0:
     signo=1
  else:
      signo=-1
  pi+= signo* (1/den)
    
   
   

pi= pi*4
print(pi)
