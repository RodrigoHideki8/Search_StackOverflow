import re
import requests
from bs4 import BeautifulSoup
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def search_stackoverflow(mensagem_erro):
    links_stackoverflow = obter_links_stackoverflow(mensagem_erro)

    if not links_stackoverflow:
        return "Não foram encontrados links para o Stack Overflow."

    respostas_stackoverflow = obter_respostas_stackoverflow(links_stackoverflow)
    
    if not respostas_stackoverflow:
        return "Não foram encontradas respostas para a mensagem de erro."

    melhor_resposta = selecionar_melhor_resposta(respostas_stackoverflow)

    resumo_resposta = resumir_resposta(melhor_resposta)

    return resumo_resposta

def obter_links_stackoverflow(mensagem_erro):
    url_busca = f"https://www.google.com/search?q={mensagem_erro}+site:stackoverflow.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url_busca, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)

    links_stackoverflow = []
    for link in links:
        href = link['href']
        if href.find('https://stackoverflow.com/questions/') != -1:
            match = re.search(r'https://stackoverflow.com/questions/\d+/.+', href)
            if match:
                links_stackoverflow.append(match.group(0))

    return links_stackoverflow

def obter_respostas_stackoverflow(links_stackoverflow):
    respostas_stackoverflow = []
    for link_stackoverflow in links_stackoverflow[:3]:
        response_stackoverflow = requests.get(link_stackoverflow)
        if response_stackoverflow.status_code == 200:
            soup_stackoverflow = BeautifulSoup(response_stackoverflow.content, 'html.parser')
            accepted_answer_tag = soup_stackoverflow.find('div', itemprop='acceptedAnswer')
            if accepted_answer_tag:
                texto_resposta = accepted_answer_tag.get_text()
                respostas_stackoverflow.append((texto_resposta, 1, True))
            else:
                respostas = soup_stackoverflow.find_all('div', class_='answer')
                for resposta in respostas:
                    texto_resposta = resposta.get_text()
                    elemento_votos = resposta.find('span', class_='vote-count-post')
                    num_votos = elemento_votos.text if elemento_votos else "Número de votos não encontrado"
                    aceita = resposta.find('span', class_='vote-accepted-on')
                    respostas_stackoverflow.append((texto_resposta, int(num_votos), True if aceita else False))

    return respostas_stackoverflow

def selecionar_melhor_resposta(respostas_stackoverflow):
    respostas_ordenadas = sorted(respostas_stackoverflow, key=lambda x: (x[2], x[1]), reverse=True)
    return respostas_ordenadas[0][0]

def resumir_resposta(melhor_resposta):
    parser = HtmlParser.from_string(melhor_resposta, ' ', Tokenizer('english'))
    stemmer = Stemmer('english')
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words('english')
    resumo = ""
    for sentence in summarizer(parser.document, 3):  # 3 é o número de frases no resumo
        resumo += str(sentence)
    return resumo[:500]