valor = float(input())
quant = int(input())
total_sem_desconto = valor * quant
desconto_fixo = total_sem_desconto * 0.10
desconto_item = (total_sem_desconto * quant) * 0.01
desconto_final = desconto_fixo + desconto_item
total_final = total_sem_desconto - desconto_final

print (f'{total_sem_desconto:.2f}')
print (f'{total_final:.2f}')
