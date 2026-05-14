# 🏢 Auditoria de Orçamentos Corporativos (Python)
 
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)]()
 
## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de programação de computadores do curso de Engenharia de Software. O objetivo do script é processar e calcular o orçamento de uma estrutura organizacional complexa (dicionários aninhados) de uma multinacional, aplicando regras de negócio dinâmicas e auditoria de execução.
 
A solução foi arquitetada utilizando conceitos avançados de Python para garantir flexibilidade, performance e rastreabilidade.
 
## 🚀 Funcionalidades
- **Cálculo Hierárquico:** Varredura completa da estrutura corporativa, independentemente do nível de profundidade.
- **Filtros Dinâmicos:** Capacidade de ignorar setores específicos e todos os seus subsetores na hora do cálculo financeiro.
- **Conversão de Câmbio:** Suporte a parâmetros opcionais para conversão de moedas em tempo de execução.
- **Sistema de Auditoria:** Monitoramento automatizado de tempo de execução e registro (logging) dos parâmetros utilizados na transação financeira.
 
## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto foi construído utilizando Python puro (Standard Library), com foco nos seguintes paradigmas e recursos:
* **Funções Recursivas (Recursion):** Utilizadas para a navegação na árvore de dados (dicionários aninhados).
* **Decorators:** Implementação do `@auditor` para injetar comportamentos de log e cronometragem sem modificar a lógica de negócios.
* **Empacotamento de Argumentos (`*args` e `**kwargs`):** Utilizados tanto no decorator quanto na função principal para permitir a passagem dinâmica de departamentos a serem ignorados e taxas de câmbio.
 
## ⚙️ Como Executar
 
### Pré-requisitos
* Python 3.8 ou superior instalado.

### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone (https://github.com/evandroaraujo250905-stack/portfolio-evandro-araujo-costa.git)
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```
 
## 🧠 Lógica e Estrutura do Código
Breve explicação de como o código foi organizado:
* Para construir a recursão, pensei na estrutura da empresa como uma árvore de departamentos, onde cada setor pode conter outros subsetores ou valores numéricos. A função percorre o dicionário e, quando encontra outro dicionário, chama a si mesma novamente para continuar a navegação até encontrar os valores finais, que são somados ao orçamento total. Também utilizei *args para ignorar departamentos específicos durante o cálculo. O decorator @auditor foi criado para separar a parte de auditoria da lógica principal, registrando os argumentos recebidos, o início e o fim da execução da função, além de medir o tempo total do processamento usando a biblioteca time.
* **Dados:** Os dados simulados da empresa foram estruturados em um dicionário aninhado, representando a hierarquia organizacional da empresa. A estrutura começa pela chave principal "Matriz", que representa a sede da empresa. Dentro dela existem vários departamentos, como "TI", "RH", "Financeiro" e "Logistica".
## 👤 Autor
 
* **Evandro Araujo Costa** * LinkedIn: https://linkedin.com/in/evandro-araújo-35699a400
* E-mail: evandroaraujo250905@gmail.com
 
---
*Projeto acadêmico com foco na aplicação prática de conceitos avançados da linguagem Python.*
