# Nível 1 — Estrutura de dados

    Conhecer as principais estruturas de dados

    Normalmente os dados são tratados em conjunto, existe varias formas de unir, relacionar, tratar, processar,
    chamados estrutura de dados.
    Essas estruturas têm seus métodos próprios de inserir, excluir, buscar, localizar, ordenar...
    Estruturas lineares ou não lineares, dados do mesmo tipo (homogêneas) ou de diferentes tipos(heterogêneas);
    Estáticos (tamanho/capacidade fixa) ou dinâmico(mutáveis).

    ## Pilhas

    O paradigma principal é por meio do LIFO — *Last In*, *First Out* (último a entrar, primeiro a sair),
    apenas dois métodos possíveis para manipular a pilha:

    1) Inserir elementos no topo da pilha;
    2) Remover elemento no topo da pilha;

        Ex:

        1

        2-1

        3-2-1

        2-1

        1

    ## Fila

    O paradigma principal é por meio do FIFO — First In, First Out(Primeiro a entrar, primeiro a sair),
    apenas dois métodos possíveis para manipular a fila:

    1) Inserir elemento no final da fila;
    2) Remover elemento no início da fila;

        Ex:

        1

        2-1

        3-2-1

        3-2

        3

    ## Deque

    É uma fila de duas pontas, ou seja, aceita inserir ou remover elementos tanto do início quanto do fim da fila.

        Ex:
        Maria
        Maria, Marta
        Joana, Maria, Marta
        Joana, Maria, Marta, Joao
        Joana, Maria, Marta
        Maria, Marta
        Marta

    ## Array

    Para ser declarados usando o modulo `array`. Lista de elementos que podem ser modificados, são dados do mesmo tipo.

        # Array_de_datas
        ([01/01/2000], [02/05/2005], [06/07/2008])

        # Array_de
        (['nome1'], ['nome2'], ['nome3'])

    ## Conjuntos

    Uma lista não ordenada de elementos **únicos**, dos quais não se é possível repetir. Em uma lista comum é possível
    repetir valores iguais, em um conjunto, não.

        lista = [1, 1, 1, 5, 7]

        set(lista)

        {1, 5, 7}

    ## Dicionários

    É um par de chave e valor, a chave no dicionário não se repete.
    
        dicionario = {'nome': 'valor', 'idade': valor}

    Implementar as principais estruturas de dados

[Artigos relacionados](https://techguide.sh/pt-BR/path/python/data-structures/)

[Referência — Alura](https://www.alura.com.br/artigos/estruturas-de-dados-introducao?gclid=CjwKCAjwm8WZBhBUEiwA178UnJ4j8AEgVf-iqVT7ewu21VlnDAlGs9nARlAiXAOgMYn22pwcC8a_BxoC5iUQAvD_BwE)

[Referência - algoritmosempython.com.br](https://algoritmosempython.com.br/cursos/algoritmos-python/intro/)
