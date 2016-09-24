import matrix as m

M = m.Matrix('M',2 , 2, '[2 3;3 5]')
B = m.Matrix('B',2 ,2, '[6 2;5 7]')
C = M + B
print C.mat_dict