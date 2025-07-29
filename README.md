# Análise de Impressão 3D com Algoritmo Genético

Este projeto apresenta uma interface gráfica para análise e otimização de combinações de modelos 3D utilizando um algoritmo genético. O objetivo é encontrar conjuntos de modelos que maximizem o aproveitamento de filamento e minimizem custos e tempo de impressão.

## Objetivo
O script `AnaliseImpressao3D.py` permite simular, de forma visual, a evolução de combinações de modelos para impressão 3D, considerando diferentes parâmetros como quantidade de filamento, tempo de impressão, cor e preço do material. O algoritmo genético busca as melhores combinações de acordo com critérios de custo e eficiência.

## Como funciona o código?
O código implementa um algoritmo genético que gera, avalia e evolui conjuntos de modelos 3D para impressão. A interface gráfica (usando tkinter) permite acompanhar, em tempo real, a evolução das melhores soluções ao longo das gerações. O usuário pode visualizar os conjuntos mais eficientes encontrados, com detalhes de custo, tempo e uso de filamento para cada modelo selecionado.

O processo envolve:
- Geração de uma população inicial de combinações de modelos
- Avaliação do "fitness" de cada combinação, considerando custo e tempo
- Seleção, cruzamento e mutação para criar novas gerações
- Exibição dos melhores resultados e convergência do algoritmo

## Instalação das Dependências
O projeto utiliza apenas uma dependência externa:

```bash
pip install -r requirements.txt
```

> Obs.: As demais bibliotecas utilizadas (`tkinter`, `random`, `time`) já fazem parte da biblioteca padrão do Python.

## Como Executar
1. Certifique-se de estar em um ambiente virtual (opcional, mas recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```bash
   python AnaliseImpressao3D.py
   ```

A interface gráfica será aberta, permitindo visualizar a evolução das melhores combinações de modelos para impressão 3D.

## Observações
- O script foi desenvolvido para Python 3.x.
- O uso do `tkinter` requer que o Python tenha suporte à interface gráfica (em alguns sistemas, pode ser necessário instalar o pacote `python3-tk`).
- O arquivo `requirements.txt` inclui apenas as dependências externas necessárias.
