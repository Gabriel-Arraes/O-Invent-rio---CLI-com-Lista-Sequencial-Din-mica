O Inventário - Gerenciador CLI com Lista Sequencial

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen.svg)

Sobre o Projeto
  Este projeto é uma aplicação interativa de Linha de Comando (CLI) desenvolvida em Python. O objetivo principal foi recriar o funcionamento de uma Lista Sequencial Dinâmica (Dynamic Array) do zero, sem utilizar os métodos de alto nível embutidos da linguagem (como `.append()`, `.insert()` ou `.pop()`). 

  A aplicação simula o gerenciamento de uma mochila de um personagem de RPG, onde o controle de memória e o deslocamento de índices são feitos manualmente através de algoritmos.

Funcionalidades e Estruturas de Dados
  O coração da aplicação é a classe `Inventory`, que gerencia três variáveis principais: a capacidade máxima (`maxCapacity`), o tamanho atual (`currentSize`) e o bloco de memória (`List`). 

As operações implementadas incluem:
  Inserção (InsertAt): Lógica de deslocamento de índices (Shift) da direita para a esquerda em um laço `for` reverso, garantindo a inserção de elementos no meio da lista sem sobrescrever os vizinhos.
  Remoção (RemoveAt): Deslocamento de índices da esquerda para a direita para preencher "buracos" deixados por itens removidos, otimizando a estrutura.
  Redimensionamento Dinâmico: Monitoramento da capacidade limite. Quando o inventário atinge `maxCapacity`, o algoritmo cria um novo bloco de memória com o dobro do tamanho (`maxCapacity * 2`), copia os itens antigos e substitui a referência na memória.
  Game Loop (Interface): Um laço `while` infinito com tratamento de exceções (`try/except`) para interagir com o usuário via terminal.

Link post Linkedin testando a aplicação: https://lnkd.in/p/e5ue84S4
