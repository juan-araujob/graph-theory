import unittest
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

from meu_grafo_matriz_adjacencia_dir import MeuGrafo

paraiba = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])

# paraiba.adicionaAresta("a1", "J", "C")
# paraiba.adicionaAresta("a2", "C", "E")
# paraiba.adicionaAresta("a3", "C", "E")
# paraiba.adicionaAresta("a4", "C", "P")
# paraiba.adicionaAresta("a5", "C", "P")
# paraiba.adicionaAresta("a6", "C", "M")
# paraiba.adicionaAresta("a7", "C", "T")
# paraiba.adicionaAresta("a8", "M", "T")
# paraiba.adicionaAresta("a9", "T", "Z")
# print(paraiba)
# print(paraiba.warshall())
g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p.adicionaAresta('a1', 'J', 'C')
g_p.adicionaAresta('a2', 'C', 'E')
g_p.adicionaAresta('a3', 'C', 'E')
g_p.adicionaAresta('a4', 'P', 'C')
g_p.adicionaAresta('a5', 'P', 'C')
g_p.adicionaAresta('a6', 'T', 'C')
g_p.adicionaAresta('a7', 'M', 'C')
g_p.adicionaAresta('a8', 'M', 'T')
g_p.adicionaAresta('a9', 'T', 'Z')
print('GP:',g_p.warshall())

        # Grafo da Paraíba sem arestas paralelas
g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')
print('GP SP:',g_p_sem_paralelas.warshall())

        # Grafos completos
g_c = MeuGrafo(['J', 'C', 'E', 'P'])
g_c.adicionaAresta('a1','J','C')
g_c.adicionaAresta('a2', 'J', 'E')
g_c.adicionaAresta('a3', 'J', 'P')
g_c.adicionaAresta('a4', 'E', 'C')
g_c.adicionaAresta('a5', 'P', 'C')
g_c.adicionaAresta('a6', 'P', 'E')
print('GC:',g_c.warshall())

g_c2 = MeuGrafo(['Nina', 'Maria'])
g_c2.adicionaAresta('amiga', 'Nina', 'Maria')
print('GC2:',g_c2.warshall())

g_c3 = MeuGrafo(['J'])

        # Grafos com laco
g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('a1', 'A', 'A')
g_l1.adicionaAresta('a2', 'A', 'B')
g_l1.adicionaAresta('a3', 'A', 'A')
print('GL1:',g_l1.warshall())

g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l2.adicionaAresta('a1', 'A', 'B')
g_l2.adicionaAresta('a2', 'B', 'B')
g_l2.adicionaAresta('a3', 'B', 'A')
print('GL2:',g_l2.warshall())


g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l3.adicionaAresta('a1', 'C', 'A')
g_l3.adicionaAresta('a2', 'C', 'C')
g_l3.adicionaAresta('a3', 'D', 'D')
g_l3.adicionaAresta('a4', 'D', 'D')
print('GL3:',g_l3.warshall())


g_l4 = MeuGrafo(['D'])
g_l4.adicionaAresta('a1', 'D', 'D')
print('GL4:',g_l4.warshall())

g_l5 = MeuGrafo(['C', 'D'])
g_l5.adicionaAresta('a1', 'D', 'C')
g_l5.adicionaAresta('a2', 'C', 'C')
print('GL5:',g_l5.warshall())


        # Grafos desconexos
g_d = MeuGrafo(['A', 'B', 'C', 'D'])
g_d.adicionaAresta('asd', 'A', 'B')
print('GD:',g_d.warshall())


        # Grafos eulerianos
g_euler1 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T'])
g_euler1.adicionaAresta("a1", "J", "C")
g_euler1.adicionaAresta("a2", "C", "E")
g_euler1.adicionaAresta("a3", "C", "E")
g_euler1.adicionaAresta("a4", "C", "P")
g_euler1.adicionaAresta("a5", "C", "P")
g_euler1.adicionaAresta("a6", "C", "M")
g_euler1.adicionaAresta("a7", "C", "T")
g_euler1.adicionaAresta("a8", "M", "T")
print('GEULER1:',g_euler1.warshall())


g_euler2  = MeuGrafo(['0','1','2','3'])
g_euler2.adicionaAresta('a1','0','1')
g_euler2.adicionaAresta('a2','0','2')
g_euler2.adicionaAresta('a3','1','2')
g_euler2.adicionaAresta('a4','2','3')
print('GEULER2:',g_euler2.warshall())

g_euler3 = MeuGrafo(['0','1','2'])
g_euler3.adicionaAresta('a1','0','1')
g_euler3.adicionaAresta('a2','1','2')
g_euler3.adicionaAresta('a3','2','0')
print('GEULER3:',g_euler3.warshall())

g_euler4 = MeuGrafo(['0', '1', '2', '3', '4'])
g_euler4.adicionaAresta("a1", "1", "0")
g_euler4.adicionaAresta("a2", "0", "2")
g_euler4.adicionaAresta("a3", "2", "1")
g_euler4.adicionaAresta("a4", "0", "3")
g_euler4.adicionaAresta("a5", "3", "4")
g_euler4.adicionaAresta("a6", "3", "2")
g_euler4.adicionaAresta("a7", "3", "1")
g_euler4.adicionaAresta("a8", "2", "4")
print('GEULER4:',g_euler4.warshall())

g_euler5 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
g_euler5.adicionaAresta('1', 'A', 'B')
g_euler5.adicionaAresta('2', 'B', 'C')
g_euler5.adicionaAresta('3', 'C', 'D')
g_euler5.adicionaAresta('4', 'D', 'E')
g_euler5.adicionaAresta('5', 'A', 'C')
g_euler5.adicionaAresta('6', 'A', 'D')
g_euler5.adicionaAresta('7', 'A', 'E')
g_euler5.adicionaAresta('8', 'B', 'D')
g_euler5.adicionaAresta('9', 'B', 'E')
g_euler5.adicionaAresta('10', 'C', 'E')
print('GEULER5:',g_euler5.warshall())

g_euler6 = MeuGrafo(['1','2','3','4','5'])
g_euler6.adicionaAresta('a1', '1', '2')
g_euler6.adicionaAresta('a2', '2', '3')
g_euler6.adicionaAresta('a3', '3', '4')
g_euler6.adicionaAresta('a4', '4', '2')
g_euler6.adicionaAresta('a5', '5', '2')
g_euler6.adicionaAresta('a6', '1', '5')
print('GEULER6:',g_euler6.warshall())

g_euler7 = MeuGrafo(['1','2','3','4','5'])
g_euler7.adicionaAresta('a1', '1', '2')
g_euler7.adicionaAresta('a2', '2', '3')
g_euler7.adicionaAresta('a3', '3', '4')
g_euler7.adicionaAresta('a4', '4', '5')
g_euler7.adicionaAresta('a5', '5', '1')
print('GEULER7:',g_euler7.warshall())

g_euler8 = MeuGrafo(['1','2','3','4','5'])
g_euler8.adicionaAresta('a1', '1', '3')
g_euler8.adicionaAresta('a2', '3', '4')
g_euler8.adicionaAresta('a3', '2', '4')
g_euler8.adicionaAresta('a4', '5', '3')
g_euler8.adicionaAresta('a5', '2', '3')
g_euler8.adicionaAresta('a6', '4', '1')
g_euler8.adicionaAresta('a7', '4', '5')
print('GEULER8:',g_euler8.warshall())

g_euler9 = MeuGrafo(['1','2','3','4','5'])
g_euler9.adicionaAresta('a1', '1', '2')
g_euler9.adicionaAresta('a2', '2', '3')
g_euler9.adicionaAresta('a3', '3', '4')
g_euler9.adicionaAresta('a4', '4', '5')
g_euler9.adicionaAresta('a5', '5', '1')
g_euler9.adicionaAresta('a6', '1', '4')
g_euler9.adicionaAresta('a7', '1', '3')
g_euler9.adicionaAresta('a8', '2', '5')
g_euler9.adicionaAresta('a9', '2', '4')
g_euler9.adicionaAresta('a10', '3', '5')
print('GEULER9:',g_euler9.warshall())

g_euler10 = MeuGrafo(['1','2','3','4','5','6'])
g_euler10.adicionaAresta('a1', '1', '2')
g_euler10.adicionaAresta('a2', '2', '6')
g_euler10.adicionaAresta('a3', '5', '6')
g_euler10.adicionaAresta('a4', '5', '4')
g_euler10.adicionaAresta('a5', '2', '3')
g_euler10.adicionaAresta('a6', '3', '4')
g_euler10.adicionaAresta('a7', '4', '1')
g_euler10.adicionaAresta('a8', '4', '2')
print('GEULER10:',g_euler10.warshall())

g_euler11 = MeuGrafo(['1','2','3','4','5','6'])
g_euler11.adicionaAresta('a1', '1', '2')
g_euler11.adicionaAresta('a2', '2', '5')
g_euler11.adicionaAresta('a3', '5', '3')
g_euler11.adicionaAresta('a4', '3', '4')
g_euler11.adicionaAresta('a5', '4', '5')
g_euler11.adicionaAresta('a6', '5', '6')
g_euler11.adicionaAresta('a7', '6', '1')
print('GEULER11:',g_euler11.warshall())

g_euler12 = MeuGrafo(['1','2','3','4','5','6'])
g_euler12.adicionaAresta('a1', '1', '2')
g_euler12.adicionaAresta('a2', '2', '3')
g_euler12.adicionaAresta('a3', '3', '4')
g_euler12.adicionaAresta('a4', '4', '5')
g_euler12.adicionaAresta('a5', '6', '2')
g_euler12.adicionaAresta('a6', '2', '4')
g_euler12.adicionaAresta('a7', '6', '4')
g_euler12.adicionaAresta('a8', '5', '6')
g_euler12.adicionaAresta('a9', '6', '1')
print('GEULER12:',g_euler12.warshall())

g_euler13 = MeuGrafo(['1','2','3','4','5','6','7'])
g_euler13.adicionaAresta('a1', '1', '2')
g_euler13.adicionaAresta('a2', '1', '3')
g_euler13.adicionaAresta('a3', '1', '4')
g_euler13.adicionaAresta('a4', '1', '6')
g_euler13.adicionaAresta('a5', '2', '3')
g_euler13.adicionaAresta('a6', '2', '5')
g_euler13.adicionaAresta('a7', '2', '7')
g_euler13.adicionaAresta('a8', '5', '6')
g_euler13.adicionaAresta('a9', '6', '7')
print('GEULER1:',g_euler13.warshall())
unittest.main()