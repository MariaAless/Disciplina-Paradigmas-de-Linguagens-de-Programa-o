# 🧬 HormLang (DSL Fisiológica)

Uma Linguagem Específica de Domínio (DSL) desenvolvida em Python com a biblioteca **Lark** para modelar, simular e monitorar a dinâmica e os níveis hormonais no corpo humano.

---

## 📌 Visão Geral

A **HormLang** simplifica a escrita de simulações fisiológicas, permitindo expressar eventos de estresse, gatilhos hormonais, repetições de estímulos e checagens condicionais com uma sintaxe concisa, direta e orientada ao domínio biológico.

### Principais Recursos
* **Declaração e Controle Hormonal:** Inicialização e alteração direta de níveis hormonais (`aumentar`, `diminuir`, `resetar`).
* **Modularidade por Eventos:** Agrupamento e disparo de rotinas de eventos fisiológicos.
* **Estruturas de Repetição:** Execução contínua de blocos por ciclos definidos (`repetir`).
* **Condicionais e Avaliação Combinada:** Suporte a operadores relacionais e lógicos (`if`, `else`, `and`, `or`).
* **Sistema de Alertas:** Notificação direta na tela quando limiares hormonais são atingidos.

---

## 📁 Estrutura do Projeto

```text
hormlang/
├── grammar.py        # Especificação da gramática EBNF e inicialização do parser Lark
├── interpreter.py    # Avaliador de condições e interpretador da árvore de sintaxe
├── main.py           # Ponto de entrada 
└── README.md         
```

## Execução

### Crie e sincronize o ambiente virtual:
```
uv venv
uv pip sync pyproject.toml
```

### Execução do projeto
```
uv run main.py

```