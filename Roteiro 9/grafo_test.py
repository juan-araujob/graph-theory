import unittest
from meu_grafo_matriz_adjacencia_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'E', 'C')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'C', 'P')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        # Grafos eulerianos
        self.g_euler1 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T'])
        self.g_euler1.adicionaAresta("a1", "J", "C")
        self.g_euler1.adicionaAresta("a2", "C", "E")
        self.g_euler1.adicionaAresta("a3", "E", "C")
        self.g_euler1.adicionaAresta("a4", "C", "P")
        self.g_euler1.adicionaAresta("a5", "P", "C")
        self.g_euler1.adicionaAresta("a6", "C", "M")
        self.g_euler1.adicionaAresta("a7", "C", "T")
        self.g_euler1.adicionaAresta("a8", "M", "T")

        self.g_euler2  = MeuGrafo(['0','1','2','3'])
        self.g_euler2.adicionaAresta('a1','0','1')
        self.g_euler2.adicionaAresta('a2','0','2')
        self.g_euler2.adicionaAresta('a3','1','2')
        self.g_euler2.adicionaAresta('a4','2','3')

        self.g_euler3 = MeuGrafo(['0','1','2'])
        self.g_euler3.adicionaAresta('a1','0','1')
        self.g_euler3.adicionaAresta('a2','1','2')
        self.g_euler3.adicionaAresta('a3','2','0')

        self.g_euler4 = MeuGrafo(['0', '1', '2', '3', '4'])
        self.g_euler4.adicionaAresta("a1", "1", "0")
        self.g_euler4.adicionaAresta("a2", "0", "2")
        self.g_euler4.adicionaAresta("a3", "2", "1")
        self.g_euler4.adicionaAresta("a4", "0", "3")
        self.g_euler4.adicionaAresta("a5", "3", "4")
        self.g_euler4.adicionaAresta("a6", "3", "2")
        self.g_euler4.adicionaAresta("a7", "3", "1")
        self.g_euler4.adicionaAresta("a8", "2", "4")

        self.g_euler5 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.g_euler5.adicionaAresta('1', 'A', 'B')
        self.g_euler5.adicionaAresta('2', 'B', 'C')
        self.g_euler5.adicionaAresta('3', 'C', 'D')
        self.g_euler5.adicionaAresta('4', 'D', 'E')
        self.g_euler5.adicionaAresta('5', 'A', 'C')
        self.g_euler5.adicionaAresta('6', 'A', 'D')
        self.g_euler5.adicionaAresta('7', 'A', 'E')
        self.g_euler5.adicionaAresta('8', 'B', 'D')
        self.g_euler5.adicionaAresta('9', 'B', 'E')
        self.g_euler5.adicionaAresta('10', 'C', 'E')

        self.g_euler6 = MeuGrafo(['1','2','3','4','5'])
        self.g_euler6.adicionaAresta('a1', '1', '2')
        self.g_euler6.adicionaAresta('a2', '2', '3')
        self.g_euler6.adicionaAresta('a3', '3', '4')
        self.g_euler6.adicionaAresta('a4', '4', '2')
        self.g_euler6.adicionaAresta('a5', '5', '2')
        self.g_euler6.adicionaAresta('a6', '1', '5')

        self.g_euler7 = MeuGrafo(['1','2','3','4','5'])
        self.g_euler7.adicionaAresta('a1', '1', '2')
        self.g_euler7.adicionaAresta('a2', '2', '3')
        self.g_euler7.adicionaAresta('a3', '3', '4')
        self.g_euler7.adicionaAresta('a4', '4', '5')
        self.g_euler7.adicionaAresta('a5', '5', '1')

        self.g_euler8 = MeuGrafo(['1','2','3','4','5'])
        self.g_euler8.adicionaAresta('a1', '1', '3')
        self.g_euler8.adicionaAresta('a2', '3', '4')
        self.g_euler8.adicionaAresta('a3', '2', '4')
        self.g_euler8.adicionaAresta('a4', '5', '3')
        self.g_euler8.adicionaAresta('a5', '2', '3')
        self.g_euler8.adicionaAresta('a6', '4', '1')
        self.g_euler8.adicionaAresta('a7', '4', '5')

        self.g_euler9 = MeuGrafo(['1','2','3','4','5'])
        self.g_euler9.adicionaAresta('a1', '1', '2')
        self.g_euler9.adicionaAresta('a2', '2', '3')
        self.g_euler9.adicionaAresta('a3', '3', '4')
        self.g_euler9.adicionaAresta('a4', '4', '5')
        self.g_euler9.adicionaAresta('a5', '5', '1')
        self.g_euler9.adicionaAresta('a6', '1', '4')
        self.g_euler9.adicionaAresta('a7', '1', '3')
        self.g_euler9.adicionaAresta('a8', '2', '5')
        self.g_euler9.adicionaAresta('a9', '2', '4')
        self.g_euler9.adicionaAresta('a10', '3', '5')

        self.g_euler10 = MeuGrafo(['1','2','3','4','5','6'])
        self.g_euler10.adicionaAresta('a1', '1', '2')
        self.g_euler10.adicionaAresta('a2', '2', '6')
        self.g_euler10.adicionaAresta('a3', '5', '6')
        self.g_euler10.adicionaAresta('a4', '5', '4')
        self.g_euler10.adicionaAresta('a5', '2', '3')
        self.g_euler10.adicionaAresta('a6', '3', '4')
        self.g_euler10.adicionaAresta('a7', '4', '1')
        self.g_euler10.adicionaAresta('a8', '4', '2')

        self.g_euler11 = MeuGrafo(['1','2','3','4','5','6'])
        self.g_euler11.adicionaAresta('a1', '1', '2')
        self.g_euler11.adicionaAresta('a2', '2', '5')
        self.g_euler11.adicionaAresta('a3', '5', '3')
        self.g_euler11.adicionaAresta('a4', '3', '4')
        self.g_euler11.adicionaAresta('a5', '4', '5')
        self.g_euler11.adicionaAresta('a6', '5', '6')
        self.g_euler11.adicionaAresta('a7', '6', '1')

        self.g_euler12 = MeuGrafo(['1','2','3','4','5','6'])
        self.g_euler12.adicionaAresta('a1', '1', '2')
        self.g_euler12.adicionaAresta('a2', '2', '3')
        self.g_euler12.adicionaAresta('a3', '3', '4')
        self.g_euler12.adicionaAresta('a4', '4', '5')
        self.g_euler12.adicionaAresta('a5', '6', '2')
        self.g_euler12.adicionaAresta('a6', '2', '4')
        self.g_euler12.adicionaAresta('a7', '6', '4')
        self.g_euler12.adicionaAresta('a8', '5', '6')
        self.g_euler12.adicionaAresta('a9', '6', '1')

        self.g_euler13 = MeuGrafo(['1','2','3','4','5','6','7'])
        self.g_euler13.adicionaAresta('a1', '1', '2')
        self.g_euler13.adicionaAresta('a2', '1', '3')
        self.g_euler13.adicionaAresta('a3', '1', '4')
        self.g_euler13.adicionaAresta('a4', '1', '6')
        self.g_euler13.adicionaAresta('a5', '2', '3')
        self.g_euler13.adicionaAresta('a6', '2', '5')
        self.g_euler13.adicionaAresta('a7', '2', '7')
        self.g_euler13.adicionaAresta('a8', '5', '6')
        self.g_euler13.adicionaAresta('a9', '6', '7')
    
    def test_warshall(self):
        self.assertEqual(self.g_p.warshall(), [[0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.g_p_sem_paralelas.warshall(), [[0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.g_c.warshall(), [[0, 1, 1, 1], [0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]])
        self.assertEqual(self.g_c2.warshall(), [[0, 1], [0, 0]])
        self.assertEqual(self.g_l1.warshall(), [[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(self.g_l2.warshall(), [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(self.g_l3.warshall(), [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1]])
        self.assertEqual(self.g_l4.warshall(), [[1]])
        self.assertEqual(self.g_l5.warshall(), [[1, 0], [1, 0]])
        self.assertEqual(self.g_d.warshall(), [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(self.g_euler1.warshall(),[[0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.g_euler2.warshall(),[[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
        self.assertEqual(self.g_euler3.warshall(),[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        self.assertEqual(self.g_euler4.warshall(),[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]])
        self.assertEqual(self.g_euler5.warshall(),[[0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]])
        self.assertEqual(self.g_euler6.warshall(),[[0, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0]])
        self.assertEqual(self.g_euler7.warshall(),[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
        self.assertEqual(self.g_euler8.warshall(),[[1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1]])
        self.assertEqual(self.g_euler9.warshall(),[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
        self.assertEqual(self.g_euler10.warshall(),[[1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.g_euler11.warshall(),[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])
        self.assertEqual(self.g_euler12.warshall(),[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])
        self.assertEqual(self.g_euler13.warshall(),[[0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]])
        