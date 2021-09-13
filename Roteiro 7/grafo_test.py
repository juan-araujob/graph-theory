import unittest
from meu_grafo_matriz_adjacencia_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.g_djikstra = MeuGrafo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
        21,22,23,24,25,26,27,28,29,30,31,32,33])
        self.g_djikstra.adicionaAresta('a1', 1, 4)
        self.g_djikstra.adicionaAresta('a2', 1, 3)
        self.g_djikstra.adicionaAresta('a3', 1, 2)
        self.g_djikstra.adicionaAresta('a4', 2, 3)
        self.g_djikstra.adicionaAresta('a5', 2, 5)
        self.g_djikstra.adicionaAresta('a6', 3, 6)
        self.g_djikstra.adicionaAresta('a7', 4, 8)
        self.g_djikstra.adicionaAresta('a8', 4, 12)
        self.g_djikstra.adicionaAresta('a9', 5, 6)
        self.g_djikstra.adicionaAresta('a10', 5, 9)
        self.g_djikstra.adicionaAresta('a11', 6, 7)
        self.g_djikstra.adicionaAresta('a12', 6, 10)
        self.g_djikstra.adicionaAresta('a13', 6, 11)
        self.g_djikstra.adicionaAresta('a14', 7, 4)
        self.g_djikstra.adicionaAresta('a15', 7, 11)
        self.g_djikstra.adicionaAresta('a16', 8, 7)
        self.g_djikstra.adicionaAresta('a17', 9, 13)
        self.g_djikstra.adicionaAresta('a18', 10, 14)
        self.g_djikstra.adicionaAresta('a19', 11, 12)
        self.g_djikstra.adicionaAresta('a20', 11, 15)
        self.g_djikstra.adicionaAresta('a21', 12, 16)
        self.g_djikstra.adicionaAresta('a22', 13, 17)
        self.g_djikstra.adicionaAresta('a23', 14, 18)
        self.g_djikstra.adicionaAresta('a24', 15, 17)
        self.g_djikstra.adicionaAresta('a25', 15, 18)
        self.g_djikstra.adicionaAresta('a26', 15, 19)
        self.g_djikstra.adicionaAresta('a27', 16, 18)
        self.g_djikstra.adicionaAresta('a28', 16, 20)
        self.g_djikstra.adicionaAresta('a29', 18, 19)
        self.g_djikstra.adicionaAresta('a30', 18, 21)
        self.g_djikstra.adicionaAresta('a31', 19, 20)
        self.g_djikstra.adicionaAresta('a32', 19, 23)
        self.g_djikstra.adicionaAresta('a33', 20, 24)
        self.g_djikstra.adicionaAresta('a34', 21, 25)
        self.g_djikstra.adicionaAresta('a35', 21, 26)
        self.g_djikstra.adicionaAresta('a36', 22, 18)
        self.g_djikstra.adicionaAresta('a37', 23, 22)
        self.g_djikstra.adicionaAresta('a38', 23, 27)
        self.g_djikstra.adicionaAresta('a39', 23, 28)
        self.g_djikstra.adicionaAresta('a40', 24, 28)
        self.g_djikstra.adicionaAresta('a41', 24, 29)
        self.g_djikstra.adicionaAresta('a42', 26, 22)
        self.g_djikstra.adicionaAresta('a43', 26, 31)
        self.g_djikstra.adicionaAresta('a44', 29, 32)
        self.g_djikstra.adicionaAresta('a45', 31, 30)
        self.g_djikstra.adicionaAresta('a46', 31, 33)
        self.g_djikstra.adicionaAresta('a47', 32, 31)
        self.g_djikstra.adicionaAresta('a48', 17, 18)
        self.g_djikstra.adicionaAresta('a49', 33, 30)
    
    def test_dijkstra(self):
        self.assertEqual(self.g_djikstra.djikstra(1,30),[1, 4, 12, 16, 18, 21, 26, 31, 30])

    def test_dijkstra_modificada(self):
        self.assertEqual(self.g_djikstra.djikstra_modificada(1,30,3,3,[9,18,24,32]),[1, 2, 5, 9, 13, 17, 18, 19, 20, 24, 29, 32, 31, 30])