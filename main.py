
idade_usuario = int(input("digite um número: "))

if idade_usuario < 0:
    print('impossível!')

if idade_usuario < 18: 
    print('não precisa se alistar.')

elif 18 < idade_usuario < 65:
    print('Não esqueça de votar na próxima eleição.')
    
elif idade_usuario > 65:
    print('Vá descansar.')

else:
    print('eita!')
