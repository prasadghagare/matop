class Matrix:
    def __init__(self,name,rows=1,columns=1):
        self.name = name
        self.no_of_rows = rows
        self.no_of_columns = columns
        self.mat_dict = {}
        for i in range(1,self.no_of_rows + 1):
            for j in range(1,self.no_of_columns + 1):
                self.mat_dict.update({(i,j):1})


#testing the class made
#making a 4*4 matrix with all elements 1
if __name__ == '__main__':
    matr_4_4 = Matrix("M",4,4)
    print matr_4_4.mat_dict