nota_atividade = float(input())
nota_prova =float(input())

media_final = (nota_atividade + nota_prova) /2
media_sub = (nota_atividade + 10) /2

if media_final >= 6:
    print ('aprovado')

elif media_sub >= 6:
    print ('talvez com a sub')

else:
    print('reprovado')

