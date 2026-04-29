#!/usr/bin/env python3
# slitherlink.py: Template para implementação do projeto de Inteligência Artificial 2025/2026.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 93:
# 113401 Afonso Mendes
# 114685 Francisco Chapouto

import random, copy
from sys import stdin
from collections import defaultdict

import utils
from utils import *

from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)


class SlitherlinkState:
    state_id = 0


    def __init__(self, board):
        self.board = board
        self.id = SlitherlinkState.state_id
        SlitherlinkState.state_id += 1
    
    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe

class Board:
    """Representação interna de um tabuleiro de Slitherlink."""

    def __init__(self, board):
        self.board = board
        

    def __str__(self):
        return str(self.board)

    def get_cell_value(self, cell: tuple) -> tuple:
        return self.board[(cell[0] * 2 + 1), (cell[1] * 2 + 1)]

    def adjacent_cell(self, cell:tuple) -> list:
        """Devolve uma lista das células que fazem
        fronteira com a célula enviada no argumento"""
        
        adj_cells = list()

        if cell[0] - 1 > 0:
            adj_cells.append((cell[0] - 1, cell[1]))
            if cell[1] - 1 > 0:
                adj_cells.append((cell[0] - 1, cell[1] - 1))
                adj_cells.append((cell[0], cell[1] - 1))



    def get_cell_edges(self, row:int, column:int) -> list:
        """Devolve os arestas da célula enviada no argumento"""
        
        edges = [(row - 1, column),(row + 1, column), (row, column - 1), (row, column + 1)]

        return [self.board[r,c] for r, c in edges]

    def get_active_edges(self, row:int, column:int) -> list:
        """Devolve o número de arestas ativas"""
        #TODO
        pass


    @staticmethod
    def parse_instance():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.
        """

        raw_board = []
        
        for line in stdin:

            edge_line = ['i'] * (2 * len(line.split()) + 1)
            raw_board.append(edge_line)

            content_line = []
            
            for char in line.split():
                content_line.append('i')
                content_line.append(char)
            content_line.append('i')
            raw_board.append(content_line)

            
        raw_board.append(edge_line)
        board = np.array(raw_board)

        return Board(board)

    # TODO: outros metodos da classe

class Slitherlink(Problem):
    def __init__(self, board: Board, gui=None):
        """O construtor especifica o estado inicial."""
        # TODO
        pass


    def actions(self, state: SlitherlinkState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        pass


    def result(self, state: SlitherlinkState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        pass

    def goal_test(self, state: SlitherlinkState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        # TODO
        pass

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass


if __name__ == "__main__":
    board = Board.parse_instance()
    print(board)


    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass







