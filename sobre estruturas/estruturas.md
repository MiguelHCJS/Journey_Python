# Estruturas de dados

## Métodos de lista

`append`
    Insere itens na lista
`clear`
    Limpa por completo a lista
`copy`
    Faz uma cópia da lista
`count`
    Conta a ocorrência de um item, na lista
`extend`
    Uni uma lista com outra
`index`
    Retorna em que index um item está, ou retorna um erro se não encontrar
`insert`
    Insere um item em uma posição específica
`pop`
    Remove um item de um determinado index, se não, retorna erro
`remove`
    Apaga um item específico
`reverse`
    Ordena a lista de forma decrescente
`sort`
    Ordena a lista de forma crescente

## Métodos de dicionário

`clear`
Zera todos os valores em um dicionário;
`copy`
Copia um dicionário para uma nova variável;
`fromkeys`
Itera índices em uma lista, ou cria uma vazia por padrão;
`get`
Retorna o valor da chave;
`items`
Retorna os itens da lista;
`keys`
Retorna as chaves da lista;
`pop`
Remove a chave e seu valor e retorna o valor, se não for passada a chave, ele remova no final.
`popitem`
Remove e retorna a chave e valor, por formato LIFO(Last in, First Out).
`setdefault`
Insere um valor padrão em uma chave existente, o valor sem padrão é None.
`update`
Atualiza o par de chave/valor, sobrescrevendo o valor das chaves: `dicionario.update(chave1 = 2, chave2 = 3)`
`values`
Retorna os valores da lista;
`del`
Deleta a tupla, chave:valor;
`dict`
Criar dicionário a partir de tuplas, dict([('nome': 'nome'), ('nome2': 'nome2')])
