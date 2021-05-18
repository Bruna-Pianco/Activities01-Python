dia_da_compra = input()
prazo_entegra = int(input())
dia_numero = 0

if dia_da_compra == 'domingo':
    dia_numero = 1
elif dia_da_compra == 'segunda':
    dia_numero  = 2  
elif dia_da_compra == 'terca':
    dia_numero  = 3        
elif dia_da_compra == 'quarta':
    dia_numero  = 4  
elif dia_da_compra == 'quinta':
    dia_numero  = 5  
elif dia_da_compra == 'sexta':
    dia_numero  = 6  
elif dia_da_compra == 'sabado':
    dia_numero  = 7  


dia_entrega = dia_numero + prazo_entegra
if dia_entrega > 6:
    dia_entrega -= 7 

if prazo_entegra == 0:
    print('chega hoje!') 
elif dia_entrega == 1:
    print('sera entregue domingo')
elif dia_entrega == 2:
    print('sera entregue segunda')
elif dia_entrega == 3:
    print ('sera entregue terca')
elif dia_entrega == 4:
    print ('sera entregue quarta')
elif dia_entrega == 5:
    print ('sera entregue quinta')    
elif dia_entrega == 6:
    print ('sera entregue sexta')
else:
    print ('sera entregue sabado')    
