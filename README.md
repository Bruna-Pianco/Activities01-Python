<img src="https://img.icons8.com/color/48/000000/python.png"/>

### Conversão de Polegadas

Megan quer comprar um novíssimo *smartphone* e está muito empolgada com as possibilidades que uma tela de tantas polegadas pode oferecer para seu entretenimento. Mas há um problema, Megan percebeu que não sabe lidar com polegadas, afinal sempre realizou cálculos usando centímetros e gostaria de se basear nessa unidade de medida para imaginar o tamanho de tela que comprará. Você pode ajudar Megan?

Seu trabalho é construir um programa que receba como entrada um número real, simbolizando uma quantidade de polegadas, e exiba o equivalente em centímetros. Lembre-se que uma polegada equivale a 2,54 cm.



### Entrada

Um número real representando as polegadas.

### Saída

Um número real, com três casas decimais, representando a conversão das polegadas da entrada em centímetros.

<hr>

### Jogo do par ou ímpar

Você gosta de jogos? Silvio gosta! Ainda mais de jogos matemáticos e que precisam de raciocínio lógico. Como Silvio é muito criativo, criou um jogo para passar o tempo com seus amigos entre os intervalos das aulas. O jogo é simples, um de seus amigos diz em voz alta um número natural maior ou igual a dois e Silvio deve dizer rapidamente o número ímpar anterior e o par posterior ao número pronunciado.

Você é um programador que gosta de desafios, afinal todo programador encara desafios o tempo todo, e por isso se ofereceu para criar um programa para automatizar a resposta de Silvio, recebendo como entrada um número natural maior ou igual a dois e exibindo o ímpar anterior e o par posterior.

### Entrada

Um número natural maior ou igual a dois.

### Saída

Dois números naturais, separados por um espaço, em que o primeiro é o número ímpar que antecede o valor dado na entrada e o segundo é o par que sucede o valor dado na entrada.

<hr>

### Dia da Entrega

"Tempos modernos"… e não nos referimos ao clássico filme de Charles Chaplin, mas sim às facilidades que a tecnologia proporciona, inimagináveis há algumas décadas. Uma dessas tecnologias é a internet, que possibilitou as compras *online*.

Podemos comprar em *sites* de empresas e em poucos dias a mercadoria estará em nossas mãos. A Impacta Express, uma multinacional de comércio eletrônico e com sua própria logística de distribuição, quer revolucionar realizando qualquer entrega no prazo de até seis dias a partir da realização da compra.

Por participar de sites de programação como o URI Online Judge, o coordenador de TI da Impacta Express encontrou você entre os primeiros do *rank,* ficou fascinado com seu desempenho e te convidou para uma entrevista!

Como parte da entrevista, o coordenador solicitou um programa que receba como entrada dois valores: (I) uma *string* com um dia da semana (*'domingo'*, *'segunda'*, *'terca'*, *'quarta'*, *'quinta'*, *'sexta'* ou *'sabado'*), sem acentuação, que indica o dia que um cliente realizou a compra no site da empresa; (II) um número natural que pode variar de *0* a *6*, que indica a quantidade de dias, a partir da realização da compra, que o cliente deverá aguardar para receber a mercadoria. O programa deve exibir o dia da semana que a compra será entregue.

Note que um prazo de *zero dias* significa que a entrega será concluída no mesmo dia, assim como um prazo de *dois dias* significa que a entrega será concluída exatamente dois dias após a realização da compra. Por exemplo, se a compra foi realizada no *'sabado'* e o prazo é de *três dias*, o cliente receberá na *'terca'*. Cuidado com a acentuação, repare que ela não está presente nas entradas e nem nas saídas, nem mesmo o *'ç'* de terça.

### Entrada

A entrada é composta por duas linhas, a primeira conterá uma *string* que corresponde a um dia da semana, que poderá ser qualquer um destes: (*'domingo'*, *'segunda'*, '*terca'*, *'quarta'*, *'quinta'*, *'sexta'* ou *'sabado'*), sem acentuação e sem os apóstrofos, que representa o dia em que o cliente realizou a compra; a segunda linha contém um número natural entre *0* e *6* (inclusive os extremos), que indica o prazo que o cliente deve esperar até receber sua compra.

### Saída

Uma *string* que indica o dia que o usuário receberá sua compra. Caso o usuário receba no mesmo dia, deverá ser exibida a *string* *'chega hoje!'*, sem apóstrofos. Caso o usuário receba em algum dos seis dias posteriores à compra, deverá ser exibida a *string* *'sera entregue <dia>'*, em que *<dia>* será o dia correspondente, também sem apóstrofos e sem acentuação.

<hr>

### Quanto tempo?

"Não tem jeito!", Julius repete para si mesmo que o trânsito da cidade grande é o maior vilão de seus dias, fazendo com que gaste muito tempo no percurso entre sua casa e o primeiro emprego, entre seu primeiro emprego e o segundo emprego, e entre seu segundo emprego até o regresso a casa. Pois é, Julius tem dois empregos!

Julius é ótimo na realização de contas, mas como está sempre com pressa, nunca teve tempo para calcular o tempo total gasto no trânsito, desde o momento que sai de casa até o momento que regressa. Seu relógio é antigo, não possibilitando cronometrar um percurso, pausar e continuar a cronometragem no próximo, por isso só sabe o tempo gasto entre os percursos isoladamente, mas não o tempo gasto nos percursos somados. Até ofereceram um novo relógio com desconto para Julius, para ele respondeu ao vendedor que "não comprar o relógio daria um desconto maior".

Você, como um bom amigo, se ofereceu para criar um programa que recebe como entrada os tempos dos três percursos de Julius (de casa até o primeiro emprego, do primeiro emprego até o segundo e do segundo até a casa) e exibe o tempo total consumido.

Não se esqueça que os três tempos serão dados em minutos.

### Entrada

Três números inteiros, um por linha, representando os tempos (em minutos) gastos por Julius em seus percursos.

### Saída

O tempo total gasto por Julius seguido por um espaço em branco e pela palavra "minutos", sem aspas e em minúsculo, conforme exemplos.

<hr>

### Professor, mas é só 0,5

Como é bom estar matriculado em um curso relacionado à computação! Há muitas disciplinas interessantes e um mundo de descobertas! Porém, como quase tudo na vida, para ter sucesso é necessário comprometimento e esforço para aprender os conteúdos que são passados pelos professores, pois exigem atenção e estudo extraclasse.

Como em situações críticas também há compaixão, você resolveu criar um programa para ajudar seus colegas. Seu programa receberá como entrada dois números reais, o primeiro representando a *nota de trabalhos* e o segundo a *nota da prova regular*. Considerando que cada uma das duas notas representa 50% da média final, seu programa exibirá uma mensagem indicando a situação do aluno que poderá ser uma das três:



- b) Talvez com a prova substitutiva: se existir alguma nota possível na prova substitutiva que permita que a média final fique maior ou igual a seis. Lembrando que, assim como a nota de trabalhos e da prova regular, a nota máxima na prova substitutiva é dez e que ela pode substituir apenas a nota da prova regular, não a de trabalhos;





- c) Reprovado: se a média final for menor do que seis e não existir possibilidade de recuperação, mesmo com a nota máxima na prova substitutiva.



Obs.: O nome do problema é uma referência a clássica frase proferida no final do semestre pelos alunos que não estudam adequadamente.



#### Entrada

Dois números reais que podem variar de 0.00 à 10.00, um por linha, que representam a nota de trabalhos e a nota da prova regular, respectivamente.

### Saída

Uma frase indicando a situação do aluno a quem pertencem as notas da entrada. A situação pode ser *'aprovado'*, *'reprovado'* ou *'talvez com a sub'*, sem os apóstrofos e completamente em minúsculo. Veja nos exemplos como a saída deve ser exibida.

<hr>

### Comprando com desconto

Maria, além de comerciante, é também uma excelente negociante! Por isso, sempre consegue descontos em suas compras. Ao visitar uma loja, Maria recebeu a seguinte proposta de um vendedor: "Se comprar minha mercadoria concederei um desconto fixo de 10% e mais 1% a cada unidade comprada". Infelizmente, Maria está cansada de tanto trabalhar e não quer fazer os cálculos sozinha para descobrir qual será o valor da compra antes e depois do desconto, por isso pediu sua ajuda.

Você criará um programa que receberá como entradas um número real, indicando o preço da mercadoria comprada por Maria, e um número inteiro, indicando a quantidade de mercadoria comprada, e exibirá o valor da compra antes do desconto e o valor final, já com o desconto aplicado.

Observação: Para todos os efeitos, assuma que essa loja nunca vende mais do que 40 unidades de uma mesma mercadoria para a mesma pessoa. Repare que não é necessário verificar, basta assumir que isso é verdade.

### Entrada

Um número real positivo na primeira linha, indicando o preço da mercadoria, e um número inteiro positivo na segunda linha, indicando a quantidade comprada da mercadoria.

### Saída

Na primeira linha deve ser impresso um valor real com duas casas decimais, indicando o preço da compra sem o desconto e, na segunda linha, o preço final com o desconto aplicado, também com duas casas decimais.

