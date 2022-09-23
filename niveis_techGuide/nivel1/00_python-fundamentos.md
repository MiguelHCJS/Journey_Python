# Python - Fundamentos

Para manipular, precisamos abstrair/representar um dado ou informação. A abstração pode usar diferentes tipos de variáveis e estrutura de dados, algumas informações básicas:

Obs.: Todos os conceitos aqui, estão em um mini projeto: 

- [x] Conhecer os tipos primitivos:

  Tipo de dados é a característica do dado que está sendo representado de forma mais básica:

  - **str** é texto;
  - **int** são números inteiros, positivo ou negativo;
  - **bool** é o True e False(verdadeiro e falso, respectivamente);
  - **list** uma lista de dados, não necessariamente do mesmo tipo;
  - **tuple** parece uma lista, mas os dados são imutável;
  - **dict** grupo de dados com chave e valor;

- [x] Declarar variáveis, considerando os diferentes tipos

  - **Não** declarar começando com número(1var), apenas após o primeiro caractere(v1ar);
  - **Não** declarar com nome de palavras reservadas, como: int, list, def;
  - **Não** declarar com caractere especial(@!#&...), o único permitido é o underline _;
  - Nomes de variáveis com **letras minúsculas**
  - **Não** deve conter acentos

- [x] Usar estruturas **condicionais** ('if', 'elif', 'else')

- [x] Conhecer os operadores de **comparação**
  - **==** igual a...(o **=** é de atribuir valor a...)
  - **!=** diferente
  - **>** maior que
  - **>=** maior ou igual a...
  - **<** menor que
  - **<=** menor ou igual a...

  - [Demais operadores](https://www.devmedia.com.br/operadores-no-python/40693)

- [x] Usar estruturas de **repetição(de ações)** e laços ('while', 'for')

- [x] Usar funções, passando parâmetros e argumentos

  - [Funções *built-in* em python](https://docs.python.org/3/library/functions.html#built-in-functions)

- [x] Manipular métodos

  - Segundo o autor Allen B. Downey, um método é uma função associada a uma classe, sendo definido dentro de uma classe e invocado de forma diferente de uma função.

  - [Função VS Método](http://excript.com/python/introducao-funcoes-python.html#:~:text=FUN%C3%87%C3%83O%20vs%20M%C3%89TODO&text=Toda%20fun%C3%A7%C3%A3o%20%C3%A9%20um%20bloco,par%C3%A2metros%20e%20NUNCA%20retorna%20valores.)

  - [Classes e métodos](https://penseallen.github.io/PensePython2e/17-classes-metodos.html)

- [x] Manipular arrays e listas
Um array precisa ser importado da biblioteca Numpy, é mais rápido o acesso, usa menos memoria e os dados precisam ser todos do mesmo tipo. Já a lista não precisa ser dados do mesmo tipo, em comparação ao acesso em array é mais lenta, é acessada por índice que começa com 0 e é mutável.

- [ ] Obter dados de uma API

- [ ] Fazer chamadas assíncronas
  - Para a remoção de gargalos de aplicação, otimizando tarefas ao reduzir o seu tempo, tornando uma aplicação capaz de atender a múltiplas requisições de forma concorrente ou em paralelo. A mudança de contexto não ocorre por interrupção, mas sim por tempo de espera, espera de resposta de rede ou de I/O.

- [x] Criar construtores
  - É um método mágico ou de Dunder, o construtor é ligado a programação orientada a objeto, usando o `__init__`dentro da classe para instanciar um objeto.

- [x] Funções anônimas
  - Função lambda ou função anônima, nada mais é do que funções que não precisam ser definidas(`def nome_funcao: ...`), tornando a tarefa mais ágil e objetiva.

[Artigoes relacionados](https://techguide.sh/pt-BR/path/python/python-fundamentals/)
