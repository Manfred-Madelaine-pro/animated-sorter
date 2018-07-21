
import os
import time
from random import randint
from random import choice

LIST_BAR = ['O', 'A', 'M', '7', 'D', 'S', '1', 'I', 'x', 'X']
LIST_VOID = [' ', '.', ':']


LIST_COLOR = [
	'\x1b[1;32;40m', '\x1b[2;32;40m', '\x1b[1;31;40m', 
	'\x1b[1;36;40m', '\x1b[2;36;40m', '\x1b[5;31;40m', 
]

MAX_SIZE_ELEM = 20
NB_ELEM = 20

CHANGE_COLOR = 20
NB_TEST = 10

C_BAR, C_VOID, C_COLOR = '', '', ''
BOARD, TAB_TO_SORT = [], []
COUNT_COL, NB_OP = 0, 0


def init_table():
	global TAB_TO_SORT, BOARD, NB_OP, C_BAR, C_VOID
	C_BAR, C_VOID = choice(LIST_BAR), choice(LIST_VOID)
	NB_OP = 0

	TAB_TO_SORT = [randint(1, MAX_SIZE_ELEM) for i in range(NB_ELEM)]
	BOARD = [[C_VOID for i in range(NB_ELEM)] for i in range(MAX_SIZE_ELEM)]

	for elem, size_elem in enumerate(TAB_TO_SORT):
		change_column(elem, size_elem)
	

def change_column(col_index, size_elem):
	born_sup = MAX_SIZE_ELEM-1
	for i in range (size_elem):
		BOARD[born_sup-i][col_index] = C_BAR

	for i in range(0, born_sup-i):
		BOARD[i][col_index] = C_VOID


def permute_col(col_i, col_j):
	global NB_OP
	change_column(col_j, TAB_TO_SORT[col_j])
	change_column(col_i, TAB_TO_SORT[col_i])
	print_table()
	NB_OP += 1


def print_colored(txt):
	global C_COLOR, COUNT_COL
	if (COUNT_COL == CHANGE_COLOR):
		COUNT_COL, C_COLOR = 0, choice(LIST_COLOR)
	else:
		COUNT_COL += 1
	print(C_COLOR + txt + '\x1b[0m')


def print_table():
	os.system('clear')
	txt, tabu = '\n', '    '
	for line in BOARD:
		txt += tabu + ' '.join(str(elem) + ' ' for elem in line) + '\n'

	size_elm = tabu + ' '.join(str(elem) + ' ' for elem in TAB_TO_SORT)

	print_colored(txt)
	print_colored(size_elm)
	time.sleep(0.2)


def sort_table():
	global TAB_TO_SORT
	for j in range(len(TAB_TO_SORT)):
		i = j
		while i > 0 and TAB_TO_SORT[i] < TAB_TO_SORT[i-1]:
			TAB_TO_SORT[i], TAB_TO_SORT[i-1] = TAB_TO_SORT[i-1], TAB_TO_SORT[i]
			permute_col(i, i-1)
			i-=1


def test():
	init_table()
	sort_table()
	print('nb of opperations : ', NB_OP)

# --------------------------------------
#               Main
# --------------------------------------

if __name__ == '__main__':
	for i in range(NB_TEST):
		test()
		if i != NB_TEST-1:
			time.sleep(2)
