#python code 
#estacio macapa

n1 = str(input('digite seu nome: '))
n1f = n1.title() 
peso = float(input('digite seu peso em kg: '))
alt = float(input('digite sua altura em metros: ' ))
result = (peso) / (alt * alt)
print('IMC: {:.1f}'.format(result))
if result <= 16.9 :
   print('atenção {}! você está muito abaixo do peso ideal '.format(n1f))
elif result > 16.9 and result <=18.4 :
   print('atenção {}! você está abaixo do peso ideal'.format(n1f))
elif result >= 18.5 and result <= 24.9 :
   print('atenção {}! você está com o peso ideal'.format(n1f)) 
elif result >= 25 and result <= 29.9 :
   print('atenção {}! você está acima do peso'.format(n1f))
elif result >= 30 and result <= 34.9 :
   print('atenção {}! você está com obesidade grau l'.format(n1f)) 
elif result >= 35 and result <= 40 :
   print('atenção {}! você está com obesidade grau Il'.format(n1f)) 
elif result > 40 :
   print('atenção {}! você está com obesidade grau IIl '.format(n1f)) 
n1 = str(input('digite seu nome: '))
n1f = n1.title() 
peso = float(input('digite seu peso em kg: '))
alt = float(input('digite sua altura em metros: ' ))
result = (peso) / (alt * alt)
print('IMC: {:.1f}'.format(result))
if result <= 16.9 :
   print('atenção {}! você está muito abaixo do peso ideal '.format(n1f))
elif result > 16.9 and result <=18.4 :
   print('atenção {}! você está abaixo do peso ideal'.format(n1f))
elif result >= 18.5 and result <= 24.9 :
   print('atenção {}! você está com o peso ideal'.format(n1f)) 
elif result >= 25 and result <= 29.9 :
   print('atenção {}! você está acima do peso'.format(n1f))
elif result >= 30 and result <= 34.9 :
   print('atenção {}! você está com obesidade grau l'.format(n1f)) 
elif result >= 35 and result <= 40 :
   print('atenção {}! você está com obesidade grau Il'.format(n1f)) 
elif result > 40 :
   print('atenção {}! você está com obesidade grau IIl '.format(n1f))
