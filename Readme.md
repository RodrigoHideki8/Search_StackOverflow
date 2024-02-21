# Buscador de Respostas no Stack Overflow

Este projeto consiste em um buscador de respostas no Stack Overflow com base em mensagens de erro fornecidas pelo usuário. O objetivo é facilitar a busca por soluções para problemas de programação comuns.

## Funcionalidades

### Função `buscar_resposta_stackoverflow(mensagem_erro)`

Esta função é responsável por buscar uma resposta relevante no Stack Overflow com base em uma mensagem de erro fornecida como entrada.

1. **Obtenção de Links Relevantes:**
   - Utiliza a função `obter_links_stackoverflow()` para obter uma lista de links relevantes do Stack Overflow com base na mensagem de erro fornecida.
   - Verifica se a lista de links do Stack Overflow está vazia e retorna uma mensagem indicando que não foram encontrados links relevantes, se for o caso.

2. **Obtenção de Respostas Relevantes:**
   - Chama a função `obter_respostas_stackoverflow()` para obter respostas relevantes do Stack Overflow com base nos links obtidos.
   - Verifica se a lista de respostas do Stack Overflow está vazia e retorna uma mensagem indicando que não foram encontradas respostas relevantes, se for o caso.

3. **Seleção da Melhor Resposta:**
   - Chama a função `selecionar_melhor_resposta()` para selecionar a melhor resposta entre as respostas obtidas.

4. **Resumo da Resposta:**
   - Chama a função `resumir_resposta()` para resumir o conteúdo da melhor resposta obtida.

### Função `obter_links_stackoverflow(mensagem_erro)`

Esta função é responsável por realizar uma busca no Google com a mensagem de erro fornecida e extrair os links relevantes do Stack Overflow.

### Função `obter_respostas_stackoverflow(links_stackoverflow)`

Esta função é responsável por acessar os links relevantes do Stack Overflow e extrair as respostas disponíveis.

### Função `selecionar_melhor_resposta(respostas_stackoverflow)`

Esta função é responsável por selecionar a melhor resposta entre as respostas obtidas.

### Função `resumir_resposta(melhor_resposta)`

Esta função é responsável por resumir o conteúdo da melhor resposta obtida.

### Função `buscar_resposta()`

Esta função é chamada quando o botão "Buscar" é clicado na interface gráfica.

## Utilização

Para utilizar o buscador de respostas no Stack Overflow, basta fornecer a mensagem de erro desejada na interface gráfica e clicar no botão "Buscar".

## Dependências

- `requests`: Para fazer solicitações HTTP.
- `BeautifulSoup`: Para fazer parsing de HTML.
- `HtmlParser`: Para converter texto em um objeto HtmlParser.
- `LsaSummarizer`: Para realizar a sumarização de texto.

Certifique-se de ter todas as dependências instaladas antes de executar o código.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.
