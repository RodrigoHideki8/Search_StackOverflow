import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


import unittest
from search_stackoverflow import search_stackoverflow

class TestBuscaStackOverflow(unittest.TestCase):
    def test_buscar_resposta_stackoverflow(self):
        mensagem_erro = "Erro ao acessar o banco de dados"

        resumo_resposta = search_stackoverflow(mensagem_erro)

        self.assertNotEqual(resumo_resposta, "")

if __name__ == '__main__':
    unittest.main()